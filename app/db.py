"""Database functions"""

import os
import pandas as pd

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
import psycopg2

router = APIRouter()

"""
This file will contain functions, classes, and logic regarding the database connection to the AWS RDS Database.
It will define the two classes, Case() and Judge(), that will be used to construct records for 
sending to store on the db.

It will also contain the function for obtaining the connection to the database.
"""

# Import environment variables for connecting to the db
def get_db_connection():
    """
    FUNCTION: When called, will return a connection to the AWS RDS database
    being used for the HRFAsylum project

    RETURNS: Cursor Object
    """
    # Credentials for connecting to the database
    rds_username = os.getenv('rds_username')
    rds_password = os.getenv('rds_password')
    rds_endpoint = os.getenv('DATABASE_URL')
    port = '5432'
    database_name = 'hrfasyluma'
    
    
    return psycopg2.connect(host=rds_endpoint, user=rds_username, password=rds_password)


# async def get_db() -> sqlalchemy.engine.base.Connection:
#     """Get a SQLAlchemy database connection.
    
#     Uses this environment variable if it exists:  
#     DATABASE_URL=dialect://user:password@host/dbname

#     Otherwise uses a SQLite database for initial local development.
#     """
#     load_dotenv()
#     database_url = os.getenv('DATABASE_URL')
#     engine = sqlalchemy.create_engine(database_url)
#     connection = engine.connect()
#     try:
#         yield connection
#     finally:
#         connection.close()


# @router.get('/info')
# async def get_url(connection=Depends(get_db)):
#     """Verify we can connect to the database, 
#     and return the database URL in this format:

#     dialect://user:password@host/dbname

#     The password will be hidden with ***
#     """
#     url_without_password = repr(connection.engine.url)
#     return {'database_url': url_without_password}




