from sqlalchemy.orm import Session
from models.user import UserModel
from schemas.user_schema import UserCreate
from fastapi import HTTPException, status

class AuthService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):
        existing = db.query(UserModel).filter(UserModel.username == user_data.username).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="اسم المستخدم مسجل مسبقاً.")
        new_user = UserModel(
            username=user_data.username, hashed_password=user_data.password, role=user_data.role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
