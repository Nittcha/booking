from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database URL
DATABASE_URL = "mysql+pymysql://root@localhost:3306/db_booking"

# Create engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Base declarative class
Base = declarative_base()

# Define models
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    guest_name = Column(String(100), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    room = relationship("Room", back_populates="bookings")

Room.bookings = relationship("Booking", order_by=Booking.id, back_populates="room")

# Create tables
Base.metadata.create_all(engine)

# Function to add a new room (example usage)
def add_room(name):
    session = SessionLocal()
    new_room = Room(name=name)
    session.add(new_room)
    session.commit()
    session.close()

# Function to print all rooms (example usage)
def print_rooms():
    session = SessionLocal()
    for room in session.query(Room).all():
        print(f'Room ID: {room.id}, Name: {room.name}')
    session.close()

# Automatically run these functions when the script is executed
if __name__ == "__main__":
    add_room("Elegant Suite")
    print_rooms()
