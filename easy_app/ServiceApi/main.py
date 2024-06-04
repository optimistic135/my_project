from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from exts.config import SessionLocal
from exts.models import  User

app = FastAPI()

class base_user(BaseModel):
    username:str
    password:str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/register")
def adduser(user:base_user, db:Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.username == user.username).first()
    if exist_user:
        return {
            'code': 400,
            'detail': '用户已被注册'
        }
        # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="该用户已被注册")
    db_user = User()
    db_user.pwd = user.password
    db_user.username = user.username
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        'code': 200,
        'detail': '添加成功'
    }


@app.get("/nihaoapi")
def nihao():
    return {
        "code":"200",
        "detail":"nihao ya!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.10.103", port=8000)
    # uvicorn.run(app, host="10.253.134.230", port=8000)