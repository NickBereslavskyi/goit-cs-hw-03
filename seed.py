import psycopg2
from faker import Faker
import random

fake = Faker()

# Параметри підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="tasks_db",   # заміни на свою БД
    user="postgres",     # свій користувач
    password="your_password",  # пароль
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Створимо 10 користувачів
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Вибираємо id статусів
cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Вибираємо id користувачів
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

# Створимо 30 завдань
for _ in range(30):
    title = fake.sentence(nb_words=4)
    description = fake.text(max_nb_chars=200)
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
        (title, description, status_id, user_id)
    )

conn.commit()
cur.close()
conn.close()

print("Database seeded successfully")