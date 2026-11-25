# ==========================================
# db.py  ->  Connection to the database
# ==========================================
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL server address. Format: mysql+pymysql://USERNAME:PASSWORD@HOST:PORT
# XAMPP: username is root and the password is empty
#SERVER_URL = "mysql+pymysql://root:root@localhost:3306"    #psycopg2

SERVER_URL = "postgresql+psycopg2://alchemybd_user:GVrCE9x578suKx8mI89zqHYPD7hnTJXL@dpg-dc36ia9ksfps7396g5sg-a.oregon-postgres.render.com/alchemybd"


# DB_NAME = "alchemydb"
#
# # Create the database automatically if it doesn't exist yet
# # (so you don't need phpMyAdmin to create it)
# try:
#     with create_engine(SERVER_URL).connect() as connection:
#         connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
# except Exception as error:
#     print("\n" + "=" * 60)
#     print(" ERROR: Could not connect to MySQL!")
#     print(" 1. Open XAMPP and click Start next to MySQL")
#     print(" 2. Check the username / password in SERVER_URL (db.py)")
#     print(" Details:", error)
#     print("=" * 60 + "\n")
#     raise SystemExit(1)
#
# # Full address of our database
# DATABASE_URL = f"{SERVER_URL}/{DB_NAME}"

engine = create_engine(SERVER_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


# Opens a database session for each request
# and closes it when the work is done.
# Used in routers like this:  db: Session = Depends(get_db)
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
