from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Base class for our classes
Base = declarative_base()

# Class definitions
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_name = Column(String(100), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    room = relationship("Room", back_populates="bookings")

Room.bookings = relationship("Booking", order_by=Booking.id, back_populates="room")
