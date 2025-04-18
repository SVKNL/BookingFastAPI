from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..models.reservation import Table as TableModel


def create_table(db: Session, table_data):
    try:
        db_table = TableModel(**table_data.dict())
        db.add(db_table)
        db.commit()
        db.refresh(db_table)
        return db_table
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,
                            detail=f"Стол с именем '{table_data.name}'"
                                   f" уже существует.")


def get_tables(db: Session):
    return db.query(TableModel).all()


def delete_table(db: Session, table_id: int):
    db_table = db.query(TableModel).filter(TableModel.id == table_id).first()
    if db_table:
        db.delete(db_table)
        db.commit()
        return True
    return False
