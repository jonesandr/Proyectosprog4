
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Palabra(Base):
  __tablename__ = "palabra"

  nombre = Column(String(50), primary_key=True)
  significado = Column(String(255), nullable=False)

  def __repr__(self) -> str:
    return f'Nombre: {self.nombre}\nSignificado: {self.significado}'