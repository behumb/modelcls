from sqlalchemy import Column, String
from .database import Base


class ImageClassification(Base):
    __tablename__ = "ImageClassification"

    id = Column(String, primary_key=True, index=True)
    label = Column(String)
