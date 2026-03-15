from pathlib import Path
import tomllib

CONFIG_PATH = Path(__file__).parent.parent / "Configs" / "config.toml"

def get_economy_symbol():
    with open(CONFIG_PATH, "rb") as f:
        config = tomllib.load(f)
    return config["Economy"]["Economy_Symbol"]