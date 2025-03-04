import os
import glob
import yaml
import argparse

# --- Constants ---
MONOBEHAVIOUR_START = 'MonoBehaviour:'
YAML_SEPARATOR = '---'
TYPE_FIELD = 'type'
TEAM_FIELD = 'team'

# --- Default Values ---
DEFAULT_CARDS_DIR = "Cards"
DEFAULT_CONFIG_FILE = "config.yaml"
DEFAULT_OUTPUT_FILE = "output.md"

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

    headers = []
    for field in fields_to_extract + (['stats'] if 'stats' in fields_to_extract else []):
        headers.append(custom_headers.get(field, field.capitalize()))


    if not card_type_mapping or not fields_to_extract:
        print("Error: 'card_types' or 'fields' missing in config.")
        return
    if output_format not in ('csv', 'table'):
        print("Error: Invalid 'output_format'. Must be 'csv' or 'table'.")
        return

    if output_format == 'table' and len(headers) != len(fields_to_extract) + ('stats' in fields_to_extract):
        print(f"Error: Number of custom headers ({len(headers)}) does not match the number of fields ({len(fields_to_extract) + ('stats' in fields_to_extract)}).")
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

    if 'stats' in fields:
        if all(stat in card_info for stat in ["mana", "attack", "hp"]):
            card_info['stats'] = f"{card_info['mana']} / {card_info['attack']} / {card_info['hp']}"
        else:
            print(f"Warning: Could not create 'stats' for {asset_file} (missing mana, attack, or hp).")
            card_info['stats'] = ''

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
                f.write(", ".join(line_parts) + "\n")

        elif output_format == 'table':
            header_line = "| " + " | ".join(headers) + " |"
            separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
            f.write(header_line + "\n")
            f.write(separator_line + "\n")

            for card in card_data:
                row_parts = []
                for field in fields:
                    value = card.get(field, "")
                    row_parts.append(str(value))
                f.write("| " + " | ".join(row_parts) + " |\n")

    print(f"Finished writing to {output_file}")

def main():
    """Main function with command-line argument parsing and default values."""

    parser = argparse.ArgumentParser(description="Generate a Markdown card list from Unity .asset files.")
    parser.add_argument("cards_root_dir", nargs='?', default=DEFAULT_CARDS_DIR,
                        help=f"The root directory containing card definitions (default: {DEFAULT_CARDS_DIR}).")
    parser.add_argument("config_file", nargs='?', default=DEFAULT_CONFIG_FILE,
                        help=f"Path to the YAML configuration file (default: {DEFAULT_CONFIG_FILE}).")
    parser.add_argument("output_md_file", nargs='?', default=DEFAULT_OUTPUT_FILE,
                        help=f"Path to the output Markdown file (default: {DEFAULT_OUTPUT_FILE}).")
    args = parser.parse_args()

    generate_card_list(args.cards_root_dir, args.config_file, args.output_md_file)

if __name__ == "__main__":
    # --- Example Usage (Creates dummy files ONLY if they don't exist) ---

    # Create a dummy "Cards" directory structure for testing
    if not os.path.exists(DEFAULT_CARDS_DIR):
        os.makedirs(os.path.join(DEFAULT_CARDS_DIR, "Ancients"))
        os.makedirs(os.path.join(DEFAULT_CARDS_DIR, "Fire"))
        os.makedirs(os.path.join(DEFAULT_CARDS_DIR, "Forest"))

    # --- Create dummy .asset files (ONLY if they don't exist) ---
    dummy_asset_content_octogoth = """
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 0}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 843a21f7f6f205741a0a7341aec8e84d, type: 3}
  m_Name: octogoth
  m_EditorClassIdentifier:
  id: octogoth
  title: Octogoth
  type: 10
  team: {fileID: 11400000, guid: 11bdd82310f039544ad50809833304f8, type: 2}
  mana: 4
  attack: 3
  hp: 3
  text: When attacking, roll a D6. On 4+ gain +6 attack.
"""
    octogoth_path = os.path.join(DEFAULT_CARDS_DIR, "Ancients", "octogoth.asset")
    if not os.path.exists(octogoth_path):
        with open(octogoth_path, "w", encoding="utf-8") as f:
            f.write(dummy_asset_content_octogoth)

    dummy_asset_content_fire = """
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 0}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 51285281531359749a8d6cf671798d52, type: 3}
  m_Name: "\u6218\u6597\u5DE5\u7A0B\u5E08"
  m_EditorClassIdentifier:
  id: "\u6218\u6597\u5DE5\u7A0B\u5E08"
  title: "Battle Engineer"
  type: 10
  team: {fileID: 0}
  mana: 3
  attack: 2
  hp: 5
  text: "Effect damage +1."
"""
    fire_path = os.path.join(DEFAULT_CARDS_DIR, "Fire", "battleengineer.asset")
    if not os.path.exists(fire_path):
        with open(fire_path, "w", encoding="utf-8") as f:
            f.write(dummy_asset_content_fire)

    dummy_asset_content_forest = """
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &11400000
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 0}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: 9f04e590a775638498d47d5695895922, type: 3}
  m_Name: "\u591C\u884C\u8005"
  m_EditorClassIdentifier:
  id: "\u591C\u884C\u8005"
  title: "Nightsinger"
  type: 10
  team: {fileID: 0}
  mana: 3
  attack: 2
  hp: 5
  text: "Regeneration. Poisonous when damaged."
"""
    forest_path = os.path.join(DEFAULT_CARDS_DIR, "Forest", "nightsinger.asset")
    if not os.path.exists(forest_path):
        with open(forest_path, "w", encoding="utf-8") as f:
            f.write(dummy_asset_content_forest)


    # --- Create a config.yaml file (ONLY if it doesn't exist) ---
    default_config_content = """
card_types:
  "10": "Character"
  "50": "Equipment"
  "30": "Artifact"
  "20": "Spell"
  "40": "Secret"
  "5": "Hero"

fields:
  - type
  - team
  - title
  - text
  - mana
  - attack
  - hp

output_format: table

team_overrides:
  "Fire": "Humans"
  "Forest": "Eryxians"
  "Ancients": "The Ancients"

headers:
  "type": "Card Type"
  "team": "Faction"
  "title": "Card Name"
  "text": "Card Text"
  "mana": "Cost"
  "attack": "Attack"
  "hp": "HP"
"""
    if not os.path.exists(DEFAULT_CONFIG_FILE):
        with open(DEFAULT_CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write(default_config_content)

    main()