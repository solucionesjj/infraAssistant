from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
def index():
    return "InfraAssistant API Working."

# import os
# from fastapi import FastAPI, status
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import mysql

# # Retrieve database connection string from environment variable
# # DB_CONN_STR = os.environ.get("DB_CONN_STR")
# DB_CONN_STR = mysql.connector.connect(user="uDbInfraAssistant", password="Q4xvc6sc", host="infra-assistant-db.mysql.database.azure.com", port=3306, database="{your_database}", ssl_ca="{ca-cert filename}", ssl_disabled=False)
# # Create a SQLAlchemy engine
# engine = create_engine(DB_CONN_STR)

# # Define a declarative base model for SQLAlchemy
# Base = declarative_base()

# # Define a model for your data
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     description = Column(String)

# # Create a session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create a FastAPI app
# app = FastAPI()

# # Define a Pydantic model for incoming data
# class ItemRequest(BaseModel):
#     name: str
#     description: str

# # Create a route for a POST request to store a record
# @app.post("/items", status_code=status.HTTP_201_CREATED)
# async def create_item(item: ItemRequest):
#     # Create a new database session
#     db = SessionLocal()

#     # Create a new Item instance
#     new_item = Item(name=item.name, description=item.description)

#     # Add the item to the database session
#     db.add(new_item)

#     # Commit the changes to the database
#     try:
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         raise e

#     # Close the database session
#     db.close()

#     return {"id": new_item.id, "name": new_item.name, "description": new_item.description}
