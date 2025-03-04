import os
import glob
import yaml
import argparse

# --- Constants ---
MONOBEHAVIOUR_START = 'MonoBehaviour:'
YAML_SEPARATOR = '---'
TYPE_FIELD = 'type'
TEAM_FIELD = 'team'

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
    output_format = config.get('output_format', 'csv').lower()
    team_overrides = config.get('team_overrides', {})
    custom_headers = config.get('headers', {})

    # --- Build final headers, based on *actual* fields ---
    headers = []
    for field in fields_to_extract:  # No 'stats' here
        headers.append(custom_headers.get(field, field.capitalize()))

    if not card_type_mapping or not fields_to_extract:
        print("Error: 'card_types' or 'fields' missing in config.")
        return
    if output_format not in ('csv', 'table'):
        print("Error: Invalid 'output_format'. Must be 'csv' or 'table'.")
        return

    # --- Header check only for table format ---
    if output_format == 'table' and len(headers) != len(fields_to_extract): # No + 1
        print(f"Error: Number of custom headers ({len(headers)}) does not match the number of fields ({len(fields_to_extract)}).")
        return

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

                if line.startswith(MONOBEHAVIOUR_START):
                    in_mono_behaviour_block = True
                    continue

                if in_mono_behaviour_block:
                    if line.startswith(YAML_SEPARATOR):
                        break

                    parts = line.split(':', 1)
                    if len(parts) != 2:
                        continue

                    field = parts[0].strip()
                    value = parts[1].strip()

                    if field == TEAM_FIELD:
                        rel_path = os.path.relpath(os.path.dirname(asset_file), cards_root_dir)
                        team_name = os.path.basename(rel_path)
                        card_info[TEAM_FIELD] = team_overrides.get(team_name, team_name)
                        continue

                    if field == TYPE_FIELD and TYPE_FIELD in fields:
                        if '{' not in value and '}' not in value:
                            card_info[TYPE_FIELD] = card_types.get(value, f"Unknown ({value})")

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

    # --- FIX: Don't calculate 'stats' here ---
    # if all(stat in card_info for stat in ["mana", "attack", "hp"]):
    #     card_info['stats'] = f"{card_info['mana']} / {card_info['attack']} / {card_info['hp']}"

    required_fields = ["type", "team", "title", "text"]  # No 'stats' here
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
                # --- FIX:  Iterate only through 'fields' ---
                for field in fields:
                    value = card.get(field, "")
                    line_parts.append(str(value))
                f.write(", ".join(line_parts) + "\n")

        elif output_format == 'table':
            header_line = "| " + " | ".join(headers) + " |"
            separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
            f.write(header_line + "\n")
            f.write(separator_line + "\n")

            for card in card_data:
                row_parts = []
                # --- FIX: Iterate only through 'fields' ---
                for field in fields:
                    value = card.get(field, "")
                    row_parts.append(str(value))
                f.write("| " + " | ".join(row_parts) + " |\n")

    print(f"Finished writing to {output_file}")

def main():
    """Main function to handle command-line arguments and run the script."""

    parser = argparse.ArgumentParser(description="Generate a Markdown card list from Unity .asset files.")
    parser.add_argument("cards_root_dir", help="The root directory containing card definitions.")
    parser.add_argument("config_file", help="Path to the YAML configuration file.")
    parser.add_argument("output_md_file", help="Path to the output Markdown file.")
    args = parser.parse_args()

    generate_card_list(args.cards_root_dir, args.config_file, args.output_md_file)

if __name__ == "__main__":
    main() #Simplified, we call it using cmd arguments