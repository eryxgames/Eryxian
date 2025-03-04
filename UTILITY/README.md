# Utility for Extracting Cards from Unity Project

- Eryxian TCG
- For internal use, card effects analysis

## Usage

Run in a folder with your Cards folder with cards in subfolders (Name of subfolders will affect the name of the factions in the table). You can set name overrides in config.yaml. Then:

```
python cardextractor.py
```

or:

```
python cardextractor.py Cards config.yaml output.md
```

You can set custom folders or configs:

```python
python cardextractor.py MyCards my_config.yaml my_output.md  # All custom
python cardextractor.py MyCards  # Custom cards dir, default config and output
python cardextractor.py  config2.yaml # Custom config, default cards and output.
python cardextractor.py  config2.yaml my_special_output.md #Custom config and output
```
