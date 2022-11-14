import pandas
from sqlalchemy import create_engine

class DB:
	def __init__(self, user : str, passwd : str, db : str, host : str):
		self.engine = create_engine("mariadb:///?User={user}&;Password={passwd}&Database={db}&Server={host}}&Port=3306".format(user=user, passwd=passwd, db=db, host=host))
	def execute(query : str):
		return pandas.read_sql(query, engine)