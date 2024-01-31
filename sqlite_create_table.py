from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
from config import my_conn # connection object to Database my_db.db 
def create_table():
       try:
        my_conn.execute(text('CREATE TABLE IF NOT EXISTS student_address(id integer primary key, \
                      name text, \
                      class text,\
                      mark integer,\
                      gender text,\
                      hostel text,\
                      address text)'))
        my_conn.commit()
        r_set=my_conn.execute(text("select name from sqlite_master where type = 'table'"))
        for row in r_set:
               print(row)
        print("Student_address Table created successfully")
       except SQLAlchemyError as e:
             error = str(e.__dict__['orig'])
             print(error)  
create_table()
