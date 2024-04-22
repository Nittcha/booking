from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_name = Column(String(100), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)