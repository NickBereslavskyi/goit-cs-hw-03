import psycopg2

# Параметри підключення
conn = psycopg2.connect(
    dbname="tasks_db",   # заміни на назву своєї БД
    user="postgres",     # заміни на свого користувача
    password="your_password",  # введи свій пароль
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Видаляємо таблиці, якщо існують
cur.execute("DROP TABLE IF EXISTS tasks CASCADE;")
cur.execute("DROP TABLE IF EXISTS users CASCADE;")
cur.execute("DROP TABLE IF EXISTS status CASCADE;")

# Таблиця users
cur.execute("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
""")

# Таблиця status
cur.execute("""
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
""")

# Таблиця tasks
cur.execute("""
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INT REFERENCES status(id) ON DELETE SET NULL,
    user_id INT REFERENCES users(id) ON DELETE CASCADE
);
""")

# Початкові статуси
cur.execute("""
INSERT INTO status (name) VALUES
('new'),
('in progress'),
('completed');
""")

conn.commit()
cur.close()
conn.close()

print("Tables created successfully")