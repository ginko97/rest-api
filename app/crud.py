from sqlalchemy.orm import Session
from . import models, schemas

def get_task(db: Session, task_id: int):
    # This 'Read' logic finds one task by its ID
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    # This 'Create' logic turns Schema data into a Database Model
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    # 1. Find the task first
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    # 2. If it exists, delete it
    if db_task:
        db.delete(db_task)
        db.commit()
    
    return db_task