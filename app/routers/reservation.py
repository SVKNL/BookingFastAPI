from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.reservation import (ReservationCreate,
                                   Reservation as ReservationSchema)
from ..services.reservation import (create_reservation,
                                    get_reservations,
                                    delete_reservation)

router = APIRouter()


@router.post("/reservations/", response_model=ReservationSchema)
def create_new_reservation(reservation_data: ReservationCreate,
                           db: Session = Depends(get_db)):
     try:
         return create_reservation(db=db, reservation_data=reservation_data)
     except ValueError as e:
         raise HTTPException(status_code=400, detail=str(e))


@router.get("/reservations/", response_model=list[ReservationSchema])
def read_reservations(db: Session = Depends(get_db)):
     return get_reservations(db=db)


@router.delete("/reservations/{id}")
def remove_reservation(id: int, db: Session = Depends(get_db)):
     if not delete_reservation(db=db, reservation_id=id):
         raise HTTPException(status_code=404, detail="Reservation not found")
