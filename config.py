from sqlalchemy import create_engine
## Use one of the line below based on SQLite or MySQL database ##

#my_conn = create_engine("sqlite:///C:\\data\\my_db.db") # For SQLite Database  
my_conn = create_engine("mysql+mysqldb://id:pw@localhost/my_tutorial") # MySQL

my_conn=my_conn.connect()