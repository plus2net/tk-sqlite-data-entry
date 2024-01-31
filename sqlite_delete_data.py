from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
from config import my_conn # connection object to Database my_db.db 
def delete_data():
       try:
        my_conn.execute(text('DELETE FROM student_address'))
        my_conn.commit()
        r_set=my_conn.execute(text("select name from sqlite_master where type = 'table'"))
        for row in r_set:
               print(row)
        print("Student_address data deleted successfully")
        
       except SQLAlchemyError as e:
             error = str(e.__dict__['orig'])
             print(error)  
delete_data()
