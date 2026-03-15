from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "economy.db"
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users(
    guild_id INTEGER,
    user_id INTEGER,
    wallet INTEGER DEFAULT 0,
    bank INTEGER DEFAULT 0,
    PRIMARY KEY (guild_id, user_id)
    ) """)
conn.commit()

#~ ---------------------
#~ Economy Service Logic
#~ ---------------------

def get_balance(guild_id, user_id):
    c.execute("SELECT wallet FROM users WHERE guild_id=? AND user_id=?", (guild_id, user_id))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        c.execute("INSERT INTO users (guild_id, user_id, wallet) VALUES (?, ?, 0)", (guild_id, user_id))
        conn.commit()
        return 0

def add_balance(guild_id, user_id, amount):
    c.execute(
        "INSERT OR IGNORE INTO users (guild_id, user_id) VALUES (?, ?)",
        (guild_id, user_id)
    )
    c.execute(
        "UPDATE users SET wallet = wallet + ? WHERE guild_id=? AND user_id=?",
        (amount, guild_id, user_id)
    )
    conn.commit()

def remove_balance(guild_id, user_id, amount):

    c.execute(
        """UPDATE users 
        SET wallet = MAX(wallet - ?, 0) 
        WHERE guild_id=? AND user_id=?""",
        (amount, guild_id, user_id)
    )

    conn.commit()

def pay(guild_id, from_user_id, to_user_id, amount):
    if get_balance(guild_id, from_user_id) >= amount:
        remove_balance(guild_id, from_user_id, amount)
        add_balance(guild_id, to_user_id, amount)
        return True
    return False

def delete_balance(guild_id, user_id):
    c.execute(
        """UPDATE users
        SET wallet = 0
        WHERE guild_id = ? AND user_id = ?""",
        (guild_id, user_id)
    )
    conn.commit()