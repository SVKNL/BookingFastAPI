from datetime import timedelta
from sqlalchemy import func, and_
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.orm import Session

from ..models.reservation import Reservation as ReservationModel


def create_reservation(db: Session, reservation_data):
    new_reservation_end = reservation_data.reservation_time + timedelta(
        minutes=reservation_data.duration_minutes)

    existing_reservation = db.query(ReservationModel).filter(
        ReservationModel.table_id == reservation_data.table_id,
        and_(
            ReservationModel.reservation_time < new_reservation_end,
            (ReservationModel.reservation_time +
             (ReservationModel.duration_minutes * func.cast(
                 '1 minute', INTERVAL
             ))) > reservation_data.reservation_time,)
    ).all()
    if existing_reservation:
        raise ValueError("Table is booked at this time")

    db_reservation = ReservationModel(**reservation_data.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservations(db: Session):
     return db.query(ReservationModel).all()


def delete_reservation(db: Session, reservation_id: int):
     db_reservation = db.query(ReservationModel).filter(
         ReservationModel.id == reservation_id).first()
     if db_reservation:
         db.delete(db_reservation)
         db.commit()
         return True
     return False
