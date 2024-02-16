from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship
from models.db.db_setup import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    pwd = Column(String(250))
    client_id = Column(Integer, ForeignKey("type_clients.id"), nullable=True)
    client = relationship("TypeClient", back_populates="users")
    projects = relationship("ProjectModel", back_populates="user")


class TypeClient(Base):
    __tablename__ = "type_clients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client = Column(String(50), unique=True)
    users = relationship("UserModel", back_populates="client")