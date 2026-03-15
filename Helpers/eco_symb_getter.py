from pathlib import Path
import json

CONFIG_PATH = Path(__file__).parent.parent / "Configs" / "json" / "economy_general_configs.json"

def get_economy_symbol(guild_id):
    with open(CONFIG_PATH, "rb") as f:
        config = json.load(f)
    return config["guilds"].get(str(guild_id), {}).get("symbol", "$")