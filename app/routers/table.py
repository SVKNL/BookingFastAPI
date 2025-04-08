from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.table import TableCreate, Table as TableSchema
from ..services.table import create_table, get_tables, delete_table


router = APIRouter()

@router.post("/tables/", response_model=TableSchema)
def create_new_table(table_data: TableCreate, db: Session = Depends(get_db)):
     return create_table(db=db, table_data=table_data)

@router.get("/tables/", response_model=list[TableSchema])
def read_tables(db: Session = Depends(get_db)):
     return get_tables(db=db)

@router.delete("/tables/{id}")
def remove_table(id: int, db: Session = Depends(get_db)):
     if not delete_table(db=db, table_id=id):
         raise HTTPException(status_code=404, detail="Table not found")