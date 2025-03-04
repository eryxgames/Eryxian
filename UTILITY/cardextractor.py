import os
import glob
import yaml

def generate_card_list(cards_root_dir, config_file, output_md_file):
    """Generates a Markdown card list from .asset files using text parsing."""

    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error loading config file: {e}")
        return

    card_type_mapping = config.get('card_types', {})
    fields_to_extract = config.get('fields', [])
    if not card_type_mapping or not fields_to_extract:
        print("Error: 'card_types' or 'fields' missing in config.")
        return

    card_data = []

    for asset_file in glob.glob(os.path.join(cards_root_dir, "**/*.asset"), recursive=True):
        print(f"Processing file: {asset_file}")
        try:
            card_info = extract_card_info_text(asset_file, fields_to_extract, card_type_mapping, cards_root_dir)
            if card_info:
                print(f"  Extracted card info: {card_info}")
                card_data.append(card_info)
            else:
                print(f"  No card info extracted from: {asset_file}")
        except Exception as e:
            print(f"Error processing {asset_file}: {e}")
            continue

    write_to_markdown(card_data, output_md_file, fields_to_extract)
    print(f"Card list generated: {output_md_file}")

def extract_card_info_text(asset_file, fields, card_types, cards_root_dir):
    """Extracts card information from a .asset file using text parsing."""

    card_info = {}
    in_mono_behaviour_block = False

    try:
        with open(asset_file, 'r') as f:
            for line in f:
                line = line.strip()

                if line.startswith('MonoBehaviour:'):
                    in_mono_behaviour_block = True
                    continue

                if in_mono_behaviour_block:
                    if line.startswith('---'):  # End of MonoBehaviour block
                        break

                    parts = line.split(':', 1)  # Split only on the first colon
                    if len(parts) != 2:
                        continue  # Skip lines without a colon

                    field = parts[0].strip()
                    value = parts[1].strip()

                    if field == 'team':
                        rel_path = os.path.relpath(os.path.dirname(asset_file), cards_root_dir)
                        card_info['team'] = os.path.basename(rel_path)
                        continue # Team extraction, as before

                    if field == 'type' and 'type' in fields:
                        # *** KEY CHANGE: Check for simple type line ***
                        # Ensure it's a simple "type: value" line, not part of another structure
                        if '{' not in value and '}' not in value:
                            card_info['type'] = card_types.get(value, f"Unknown ({value})")

                    elif field in fields:
                        card_info[field] = value #All other fields


    except FileNotFoundError:
        print(f"  File not found: {asset_file}")
        return None
    except Exception as e:
        print(f"Error during text extraction from {asset_file}: {e}")
        return None

    if not in_mono_behaviour_block:
        print(f"MonoBehaviour not found in file {asset_file}")
        return None

    if not all(field in card_info for field in ["type", "team", "title", "text", "mana", "attack", "hp"]):
        print(f"Warning: Some required fields are missing in {asset_file}")

    return card_info
def write_to_markdown(card_data, output_file, fields):
    """Writes the extracted card data to a Markdown file."""

    with open(output_file, 'w') as f:
        for card in card_data:
            print(f"Writing card to file: {card}")
            line_parts = []
            for field in fields:
                if field in ("mana", "attack", "hp"):
                    continue
                value = card.get(field, "")
                line_parts.append(str(value))

            mana = card.get("mana", "")
            attack = card.get("attack", "")
            hp = card.get("hp", "")
            stats_str = f"{mana} / {attack} / {hp}"
            line_parts.append(stats_str)

            f.write(", ".join(line_parts) + "\n")
    print(f"Finished writing to {output_file}")



# --- Example Usage ---
#Create a dummy "Cards" directory structure for testing
if not os.path.exists("Cards/Ancients"):
    os.makedirs("Cards/Ancients")

# Create a dummy .asset file (replace with your actual file)
dummy_asset_content = """
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
  art_full: {fileID: -6722439110943477826, guid: 926b7edbed2a7554f9aeaf4ac045d301,
    type: 3}
  art_board: {fileID: -4578692458917776166, guid: 7667eeb1b4e541648b42bb799393f960,
    type: 3}
  type: 10
  team: {fileID: 11400000, guid: 11bdd82310f039544ad50809833304f8, type: 2}
  rarity: {fileID: 11400000, guid: 13b592f40b7cd424c966f5d7eef425aa, type: 2}
  mana: 4
  attack: 3
  hp: 3
  traits: []
  stats: []
  abilities:
  - {fileID: 11400000, guid: 82579e30cd586544c999e6cb08a69c91, type: 2}
  text: When attacking, roll a D6. On 4+ gain +6 attack.
  desc:
  spawn_fx: {fileID: 2106287953758554471, guid: a1e1ec86d02e969408bf2a6c17010f46,
    type: 3}
  death_fx: {fileID: 0}
  attack_fx: {fileID: 0}
  damage_fx: {fileID: 0}
  idle_fx: {fileID: 0}
  spawn_audio: {fileID: 0}
  death_audio: {fileID: 0}
  attack_audio: {fileID: 0}
  damage_audio: {fileID: 0}
  deckbuilding: 1
  cost: 100
  packs:
  - {fileID: 11400000, guid: bafca3757bf537c43b1d2ba696456e2c, type: 2}
  - {fileID: 11400000, guid: 2db0d9f08bdfa57419101c08b8598c1a, type: 2}
"""
with open("Cards/Ancients/octogoth.asset", "w") as f:
    f.write(dummy_asset_content)

# Create a config.yaml file
config_content = """
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
"""
with open("config.yaml", "w") as f:
    f.write(config_content)

# Run the script
generate_card_list("Cards", "config.yaml", "output.md")

#Check output
with  open("output.md", "r") as file:
    print("File content: \n"+file.read())