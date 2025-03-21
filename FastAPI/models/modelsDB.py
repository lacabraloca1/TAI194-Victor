from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True , autoincrement="auto")
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    password = Column(String)
    def __repr__(self):
        return f'<User {self.name}>'