from sqlalchemy import (Column, Integer, String, Float, ForeignKey)
from sqlalchemy.orm import relationship
from models.db.db_setup import Base


class ProjectModel(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(250))
    budget_amount = Column(Float)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("UserModel", back_populates="projects")