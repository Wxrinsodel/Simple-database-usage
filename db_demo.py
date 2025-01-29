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
#con.execute("INSERT INTO Novels (name, genre) VALUES ('Heaven Officials Blessing', 'Dark romantic')")
#con.execute("INSERT INTO Novels (name, genre) VALUES ('CAT OWNS', 'Lovely Fantasy')")
#con.execute("INSERT INTO Novels (name, genre) VALUES ('My Invisible Twin', 'Dark romantic')")

#insert Author and year in Novels
con.execute("INSERT INTO Novels (Author, year) VALUES ('Mo Xiang Tong Xiu', '2017')")
con.execute("INSERT INTO Novels (Author, year) VALUES ('cat black n white coin', '2022')")
con.execute("INSERT INTO Novels (Author, year) VALUES ('Organic purple cabbage garden', '2020')")


#insert data in Webtoon
#con.execute("INSERT INTO Webtoon (name, genre) VALUES ('Trash of count family', 'Fantasy')")
#con.execute("INSERT INTO Webtoon (name, genre) VALUES ('S class', 'Fantasy')")
#con.execute("INSERT INTO Webtoon (name, genre) VALUES ('The most beautiful count in Siam', 'Historical comady')")


#insert Author and year in Webtoon
con.execute("INSERT INTO Webtoon (Author, year) VALUES ('Yoo_Ryeo_Han', '2018')")
con.execute("INSERT INTO Webtoon (Author, year) VALUES ('Geunsoo', '2018')")
con.execute("INSERT INTO Webtoon (Author, year) VALUES ('Yuen Kin Pakka Thi Than Phra', '2022')")


#insert data in Anime
#con.execute("INSERT INTO Anime (name, genre) VALUES ('Haikyuu', 'Sport')")
#con.execute("INSERT INTO Anime (name, genre) VALUES ('Bungou Stray dogs', 'I dont know (maybe fantasy)')")
#con.execute("INSERT INTO Anime (name, genre) VALUES ('Given', 'Drama musical')")


#insert Author and year in Anime
con.execute("INSERT INTO Anime (studio, year) VALUES ('Production I.G,', '2014')")
con.execute("INSERT INTO Anime (studio, year) VALUES ('Bones', '2016')")
con.execute("INSERT INTO Anime (studio, year) VALUES ('Dice Entertainment', '2020')")



con.commit()
