from datetime import datetime

from pydantic import BaseModel, validator


class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

    @validator('duration_minutes')
    def check_duration_positive(cls, value):
        if value <= 0:
            raise ValueError("Длительность бронирования "
                             "должна быть положительной.")
        return value


class Reservation(ReservationCreate):
    id: int

    class Config:
        orm_mode = True
