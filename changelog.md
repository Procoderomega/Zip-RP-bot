# CHANGELOG

## 1.5.0 - 2026-04-4
### Added
- Hybrid admin command `add_balance` to add money directly to a member's wallet balance
- Admin slash command `show_user_balance` to inspect another member's current wallet balance
- Public slash command `bank` to check the current bank/card balance
- Public slash command `steal` to steal a random amount from another member when they have money available
- Admin slash command `add_balanceto_card` to deposit money directly into a member's bank/card balance
- Bank/card balance service helpers `add_balance_card` and `get_balance_card`

### Changed
- Economy cog files are now reorganized into `public`, `mod`, and `admin` folders
- `Cogs/Economy/__init__.py` now registers the expanded economy command set from the new folder structure
- `Services/__init__.py` now exports the new bank/card balance helpers
- `Services/economy/economy_service.py` now separates wallet logic from bank/card logic
- `set_economy_symbol` now logs a clearer debug message after updating the server currency symbol
- `.env.example` now includes a reminder to rename the file before use

### Notes
- This release expands the economy system with bank/card support, a stealing command, and broader admin balance-management tooling

## 1.4.0 - 2026-03-21
### Added
- Hybrid admin command `add_balance` to add money directly to a member's balance
- Admin slash command `show_user_balance` to inspect another member's current balance
- Economy cog registration for the new admin balance-management commands in `Cogs/Economy/__init__.py`

### Changed
- `set_economy_symbol` now logs a clearer debug message after updating the server currency symbol

### Notes
- This release strengthens admin tooling for per-server economy moderation and support

---

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


# NOTES
- So this changelog is fully developed by AI cuz me lazy to write all the changes, so if anything doesnt look like the changelog is 100% AIs fault not mine tehe-....