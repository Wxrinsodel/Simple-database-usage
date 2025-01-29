import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

# create table Novels
#con.execute("CREATE TABLE Novels (name STRING, genre TEXT, Author TEXT, year INTEGER)")
#con.execute("CREATE TABLE Webtoon (name STRING, genre TEXT, Author TEXT, year INTEGER)")
#con.execute("CREATE TABLE Anime (name STRING, genre TEXT, studio STRING, year INTEGER)")

#insert data in Novels
con.execute("INSERT INTO novels (name, genre) VALUES ('Heaven Officials Blessing', 'Dark romantic')")
con.execute("INSERT INTO novels (name, genre) VALUES ('CAT OWNS', 'Lovely Fantasy')")
con.execute("INSERT INTO novels (name, genre) VALUES ('My Invisible Twin', 'Dark romantic')")

#insert data in Webtoon
con.execute("INSERT INTO Webtoon (name, genre) VALUES ('Trash of count family', 'Fantasy')")
con.execute("INSERT INTO Webtoon (name, genre) VALUES ('S class', 'Fantasy')")
con.execute("INSERT INTO Webtoon (name, genre) VALUES ('The most beautiful count in Siam', 'Historical comady')")


#insert data in Anime
con.execute("INSERT INTO Anime (name, genre) VALUES ('Haikyuu', 'Sport')")
con.execute("INSERT INTO Anime (name, genre) VALUES ('Bungou Stray dogs', 'I dont know (maybe fantasy)')")
con.execute("INSERT INTO Anime (name, genre) VALUES ('Given', 'Drama musical')")


con.commit()
