from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/user")
meta = MetaData(bind=engine)

conn = engine.connect()
