import os
import glob
import yaml

def generate_card_list(cards_root_dir, config_file, output_md_file):
    """Generates a Markdown card list from .asset files."""

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error loading config file: {e}")
        return

    card_type_mapping = config.get('card_types', {})
    fields_to_extract = config.get('fields', [])
    output_format = config.get('output_format', 'csv').lower()  # Default to CSV
    team_overrides = config.get('team_overrides', {})
    
    # FIX: Always include stats, and ensure headers match
    standard_fields = fields_to_extract + ['stats']
    headers = config.get('headers', standard_fields)

    if not card_type_mapping or not fields_to_extract:
        print("Error: 'card_types' or 'fields' missing in config.")
        return
    if output_format not in ('csv', 'table'):
        print("Error: Invalid 'output_format'. Must be 'csv' or 'table'.")
        return

    # FIX: More flexible headers check
    if output_format == 'table':
        if headers is None:
            # Generate default headers if not provided
            headers = [field.capitalize() for field in standard_fields]
        elif len(headers) != len(standard_fields):
            print(f"Warning: Headers count ({len(headers)}) does not match fields count ({len(standard_fields)}). Using default headers.")
            headers = [field.capitalize() for field in standard_fields]

    card_data = []

    for asset_file in glob.glob(os.path.join(cards_root_dir, "**/*.asset"), recursive=True):
        print(f"Processing file: {asset_file}")
        try:
            card_info = extract_card_info_text(asset_file, fields_to_extract, card_type_mapping, cards_root_dir, team_overrides)
            if card_info:
                print(f"  Extracted card info: {card_info}")
                card_data.append(card_info)
            else:
                print(f"  No card info extracted from: {asset_file}")
        except Exception as e:
            print(f"Error processing {asset_file}: {e}")
            continue

    write_to_markdown(card_data, output_md_file, fields_to_extract, output_format, headers)
    print(f"Card list generated: {output_md_file}")

def extract_card_info_text(asset_file, fields, card_types, cards_root_dir, team_overrides):
    """Extracts card information from a .asset file using text parsing."""

    card_info = {}
    in_mono_behaviour_block = False

    try:
        with open(asset_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                if line.startswith('MonoBehaviour:'):
                    in_mono_behaviour_block = True
                    continue

                if in_mono_behaviour_block:
                    if line.startswith('---'):  # End of MonoBehaviour block
                        break

                    parts = line.split(':', 1)
                    if len(parts) != 2:
                        continue

                    field = parts[0].strip()
                    value = parts[1].strip()

                    if field == 'team':
                        rel_path = os.path.relpath(os.path.dirname(asset_file), cards_root_dir)
                        team_name = os.path.basename(rel_path)
                        # Apply team overrides
                        card_info['team'] = team_overrides.get(team_name, team_name)
                        continue

                    if field == 'type' and 'type' in fields:
                        if '{' not in value and '}' not in value:
                            card_info['type'] = card_types.get(value, f"Unknown ({value})")

                    elif field in fields:
                        card_info[field] = value

    except FileNotFoundError:
        print(f"  File not found: {asset_file}")
        return None
    except Exception as e:
        print(f"Error during text extraction from {asset_file}: {e}")
        return None

    if not in_mono_behaviour_block:
        print(f"MonoBehaviour not found in file {asset_file}")
        return None

    # Combine stats into a single string
    if all(stat in card_info for stat in ["mana", "attack", "hp"]):
        card_info['stats'] = f"{card_info['mana']} / {card_info['attack']} / {card_info['hp']}"

    # Add a check for required fields with a bit more flexibility
    required_fields = ["type", "team", "title", "text"]
    if not all(field in card_info for field in required_fields):
        print(f"Warning: Some required fields are missing in {asset_file}")
        return None

    return card_info

def write_to_markdown(card_data, output_file, fields, output_format, headers):
    """Writes the extracted card data to a Markdown file."""

    with open(output_file, 'w', encoding='utf-8') as f:
        if output_format == 'csv':
            for card in card_data:
                line_parts = []
                for field in fields:
                    value = card.get(field, "")
                    line_parts.append(str(value))

                # Add stats at the end
                stats_str = card.get('stats', '')
                line_parts.append(stats_str)

                f.write(", ".join(line_parts) + "\n")

        elif output_format == 'table':
            # Write table header and separator
            header_line = "| " + " | ".join(headers) + " |"
            separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
            f.write(header_line + "\n")
            f.write(separator_line + "\n")

            # Write table rows
            for card in card_data:
                row_parts = []
                for field in fields:
                    value = card.get(field, "")
                    row_parts.append(str(value))

                # Add stats at the end
                stats_str = card.get('stats', '')
                row_parts.append(stats_str)

                f.write("| " + " | ".join(row_parts) + " |\n")

    print(f"Finished writing to {output_file}")

# Main execution remains the same
if __name__ == "__main__":
    # Existing directory and file creation code...
    generate_card_list("Cards", "config.yaml", "output.md")
    
    # Read and print the output file
    with open("output.md", "r", encoding="utf-8") as file:
        print("File content: \n" + file.read())