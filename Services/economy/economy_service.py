from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "economy.db"
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0
    ) """)
conn.commit()

#~ ---------------------
#~ Economy Service Logic
#~ ---------------------

def get_balance(user_id):
    c.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        c.execute("INSERT INTO users (user_id, balance) VALUES (?,?)",(user_id, 0))
        conn.commit()
        return 0

def add_balance(user_id, amount):
    """Suma dinero al usuario"""
    bal = get_balance(user_id)
    bal += amount
    c.execute("UPDATE users SET balance = ? WHERE user_id = ?", (bal, user_id))
    conn.commit()

def remove_balance(user_id, amount):
    """Resta dinero al usuario, nunca negativo"""
    bal = get_balance(user_id)
    bal -= amount
    if bal < 0: bal = 0
    c.execute("UPDATE users SET balance = ? WHERE user_id = ?", (bal, user_id))
    conn.commit()

def pay(from_user_id, to_user_id, amount):
    """Transferencia entre usuarios"""
    if get_balance(from_user_id) >= amount:
        remove_balance(from_user_id, amount)
        add_balance(to_user_id, amount)
        return True
    return False