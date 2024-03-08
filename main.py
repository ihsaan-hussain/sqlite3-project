import sqlite3
from tkinter import *

class Database:

	def __init__(self):

		self.conn = sqlite3.connect('Stats.db')
		self.c = self.conn.cursor()

	def create_table(self):
		try:
			self.c.execute("""CREATE TABLE IF NOT EXISTS players (
				name text,
				goals int,
				assists int)
				""")
			print("Table created\n")
		except:
			print("There was an error")

	def add_record(self):
		self.name = input("Name of player: ")
		self.goals = int(input("Amount of goals: "))
		self.assists = int(input("Amount of assists: "))
		#self.c.execute("""
			""")