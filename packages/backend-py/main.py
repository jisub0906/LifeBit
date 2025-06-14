# packages/backend-py/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import engine, get_db

# 애플리케이션 시작 시 테이블 생성
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/api/py/hello")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.post("/api/py/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/api/py/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items