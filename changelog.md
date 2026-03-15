# CHANGELOG

## 1.2.0 - 2026-03-14
### Added
- Sistema de economía con base de datos `SQLite` (`Services/economy/economy_service.py`) para `balance`, `add_balance`, `remove_balance` y `pay`
- Comando híbrido `work` para generar ganancias aleatorias configurables
- Comando híbrido `wallet` para consultar el balance actual con embed
- Comando híbrido `set_economy_symbol` para personalizar el símbolo de la economía en `Configs/config.toml`
- Comandos de roleplay con `slash commands`: `hug`, `kiss` y `slap` con GIFs aleatorios
- Comandos de roleplay `pat_student` y `pat_teacher` con selección de personajes (estudiantes y maestros)
- JSONs de contenido para roleplay en `Cogs/RolePlay/JSON`
- Utilidad de sincronización de slash commands `syncSlash` con opciones `global`, `ts`, `clear_global`, `clear_ts`
- Helpers para autoinicialización de cogs (`MetaInit`) y lectura del símbolo de economía
- Configuración centralizada en `Configs/config.toml` para `Prefix`, `Guild_Id`, `MIN_GAIN`, `MAX_GAIN` y `Economy_Symbol`
- Gestión de token por `.env` y ejemplo en `.env.example`

### Changed
- Presencia del bot en modo `Streaming` al iniciar
- Carga modular de cogs en `main.py` (`Economy`, `Utils`, `RolePlay`, `sync_slash`)

### Notes
- Cogs de `Moderation` y `Fun` reservados para futuras versiones

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
