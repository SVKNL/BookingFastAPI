from sqlalchemy.orm import Session

from ..models.reservation import Table as TableModel


def create_table(db: Session, table_data):
    db_table = TableModel(**table_data.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def get_tables(db: Session):
    return db.query(TableModel).all()


def delete_table(db: Session, table_id: int):
    db_table = db.query(TableModel).filter(TableModel.id == table_id).first()
    if db_table:
        db.delete(db_table)
        db.commit()
        return True
    return False