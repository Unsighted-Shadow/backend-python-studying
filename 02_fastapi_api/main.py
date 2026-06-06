from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, User

app = FastAPI()

#Pydantic Model to validate the JSON from the client
class UserCreate(BaseModel):
    username: str
    email: str
    age: int
    
#The pipeline manager
def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        age=user_data.age
    )
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return {"message": "User successfully created!", "user": new_user}

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    
    all_users = db.query(User).offset(skip).limit(limit).all()
    
    return all_users
    
@app.get("/users/{user_id}")
def read_single_user(user_id: int, db: Session = Depends(get_db)):

    target_user = db.query(User).filter(User.id == user_id).first()
    
    if target_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return target_user
    
#PUT  method in python to update the db
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    
    target_user = db.query(User).filter(User.id == user_id).first()
    
    if target_user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
    target_user.username = user_data.username
    target_user.email = user_data.email
    target_user.age = user_data.age
    
    db.commit()
    db.refresh(target_user)
    
    return {"message": "User successfully updated!", "user": target_user}
    
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    target_user = db.query(User).filter(User.id == user_id).first()
    
    if target_user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
    db.delete(target_user)
    db.commit()
    
    return {"message": f"User {user_id} successfully deleted!"}
