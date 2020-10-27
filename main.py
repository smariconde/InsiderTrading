from InsiderTrading import insider_trading
from sqlalchemy import create_engine
import pandas as pd
import datetime as dt

sql_engine = create_engine('mysql+pymysql://root:@localhost/equity')
sql_conn = sql_engine.connect()

hoy = dt.datetime.now().date().isoformat()

tickers = pd.read_sql('finviz', sql_conn).Ticker

insider = insider_trading(tickers)

insider.to_sql(con=sql_conn, name = 'insiders', if_exists = 'replace')
