import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

# create table Novels
con.execute("CREATE TABLE novels (name STRING, genre TEXT, Author TEXT, year INTEGER)")


con.commit()
