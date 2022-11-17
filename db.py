import pandas
from sqlalchemy import create_engine
class DB:
	def __init__(self, user : str, passwd : str, db : str, host : str):
		self.engine = create_engine("mysql://{}:{}@{}/{}".format(user, passwd, host, db))
	def execute(self, query : str):
		return pandas.read_sql(query, self.engine)
db = DB('lupercio', 'richieirvingaxelcuceiperro', 'ferreteria', 'moralestorres.dev')