import sqlite3


try:
    with sqlite3.connect('test_db.sqlite') as conn:
        cur = conn.cursor()
        print(type(cur))

        cur.executescript("""
            create table users(
                login,
                password,
                email
            );
        """)

        conn.commit()

except sqlite3.DatabaseError as e:
    print(f"Ошибка работы с базой данных: {e}")