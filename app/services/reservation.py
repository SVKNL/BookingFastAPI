from datetime import timedelta, datetime
import pytz
from sqlalchemy import func, and_
from sqlalchemy.dialects.postgresql import INTERVAL
from sqlalchemy.orm import Session

from ..models.reservation import Reservation as ReservationModel


utc=pytz.UTC


def create_reservation(db: Session, reservation_data):
    #Проверка свободно ли время брони
    new_reservation_end = reservation_data.reservation_time + timedelta(
        minutes=reservation_data.duration_minutes)
    crossing_reservation = db.query(ReservationModel).filter(
        ReservationModel.table_id == reservation_data.table_id,
        and_(
            ReservationModel.reservation_time < new_reservation_end,
            (
                    ReservationModel.reservation_time +
                    (ReservationModel.duration_minutes *
                     func.cast('1 minute', INTERVAL))
            ) > reservation_data.reservation_time,
        )
    ).all()
    if crossing_reservation:
        raise ValueError("Table is booked at this time")
    #Проверка актуальности даты брони
    if (utc.localize(reservation_data.reservation_time) <
            utc.localize(datetime.now())):
        raise ValueError("Reservation time is in the past")
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
