# CHANGELOG

## 1.3.0 - 2026-03-14
### Added
- Admin command `delete_user_balance` to reset a user's balance
- Debugging helpers with `OK`, `DEBUG`, and `FAIL` states
- Per-server JSON config for economy in `Configs/json/economy_general_configs.json`
- `Random` module with `botfetch` for visual bot status summary
- New per-server economy fields: `wallet` and `bank`
- Example file economy_general_configs.json.example to guide per-server configurations

### Changed
- Economy is now separated per server (`guild_id`) in database and services
- `set_economy_symbol` now stores the symbol per server in JSON
- `work` and `wallet` now use per-server symbols and balances tied to `guild_id`
- Cog loading messages now use the `OK` helper
- Console is cleared on startup and the `botfetch` summary is printed
- `.gitignore` expanded to ignore `*.db` and `*.sqlite*` files
- `.gitignore` now ignores `economy_general_configs.json`

### Removed
- `Economy_Symbol` config from `Configs/config.toml` (migrated to JSON)

---

## 1.2.0 - 2026-03-14
### Added
- Economy system with `SQLite` database (`Services/economy/economy_service.py`) for `balance`, `add_balance`, `remove_balance`, and `pay`
- Hybrid command `work` to generate configurable random earnings
- Hybrid command `wallet` to check the current balance with an embed
- Hybrid command `set_economy_symbol` to customize the economy symbol in `Configs/config.toml`
- Roleplay `slash commands`: `hug`, `kiss`, and `slap` with random GIFs
- Roleplay commands `pat_student` and `pat_teacher` with character selection (students and teachers)
- Roleplay content JSON files located in `Cogs/RolePlay/JSON`
- Slash command synchronization utility `syncSlash` with options `global`, `ts`, `clear_global`, `clear_ts`
- Helper utilities for automatic cog initialization (`MetaInit`) and economy symbol retrieval
- Centralized configuration in `Configs/config.toml` for `Prefix`, `Guild_Id`, `MIN_GAIN`, `MAX_GAIN`, and `Economy_Symbol`
- Token management using `.env` with an example file `.env.example`

### Changed
- Bot presence set to `Streaming` on startup
- Modular cog loading in `main.py` (`Economy`, `Utils`, `RolePlay`, `sync_slash`)

### Notes
- `Moderation` and `Fun` cogs reserved for future versions

--- 

## 1.1.0
### Added
- `requirements.txt` file in root
- `Cogs/` directory in root
- `Utils/` directory in `Cogs/`
- `ping.py` command in `Utils/`

- `Configs/` directory in root
- `config.toml` file in `Configs/`
- `toml_loader.py` in `Configs/`

- `Helpers/` directory in root
- `auto_init_metaclass.py` in `Helpers/`

### Changed
- Updated `main.py` adding better UX when initializing the bot
- Updated `.gitignore` adding commentaries

---

## 1.0.0
### Added
- `.gitignore` file
- `changelog.md` file
- `main.py` file
