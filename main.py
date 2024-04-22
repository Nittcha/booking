from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Booking, Room


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]        

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/rooms/")
def create_room(name: str, db: Session = Depends(get_db)):
    new_room = Room(name=name)
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return {"id": new_room.id, "name": new_room.name}

@app.get("/bookings/{booking_id}")
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking is None:
        return {"error": "Booking not found"}
    return booking

@app.post("/bookings/")
def create_booking(guest_name: str, room_id: int, db: Session = Depends(get_db)):
    new_booking = Booking(guest_name=guest_name, room_id=room_id)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return {"id": new_booking.id, "guest_name": new_booking.guest_name, "room_id": new_booking.room_id}


@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking is None:
        return {"error": "Booking not found"}
    db.delete(booking)
    db.commit()
    return {"message": "Booking deleted successfully"}

