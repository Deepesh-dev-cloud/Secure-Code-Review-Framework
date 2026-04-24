import subprocess
import sqlite3
import hashlib
import os

password = os.getenv("APP_PASSWORD")

user_input = input("Enter command: ")
subprocess.run(["cmd", "/c", user_input], shell=False)

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

name = input("Enter name: ")
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))

data = "hello"
hash_value = hashlib.sha256(data.encode()).hexdigest()

print("Safe input handled")