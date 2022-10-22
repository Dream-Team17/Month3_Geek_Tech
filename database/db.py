import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('Data base is connected!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors"
               "(id INTEGER PRIMARY KEY, "
               "name TEXT, department TEXT, "
               "age INTEGER, groups TEXT)")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(f"INSERT INTO mentors(name, department, age, groups) VALUES(?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_random(message):
    results = cursor.execute("SELECT * FROM mentors").fetchall()
    random_mentor = random.choice(results)
    await bot.send_message(message.from_user.id,
        f" Name: {random_mentor[1]}\nDepartment: {random_mentor[2]}\n"
        f"Age: {random_mentor[3]}\nGroup: {random_mentor[4]}")

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()

async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id=?", (id, ))
    db.commit()
