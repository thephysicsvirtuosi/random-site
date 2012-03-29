""" Set up the initial database """
import sqlite3
con = sqlite3.connect("randomdata.db")
con.execute("CREATE TABLE randdat (id INTEGER PRIMARY KEY, digits char(100) NOT NULL, author char(100), timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
con.commit()