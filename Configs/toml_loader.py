import tomllib
from pathlib import Path
config_path = Path(__file__).parent / "config.toml"
with open(config_path,"rb") as f:
    bot_config = tomllib.load(f)