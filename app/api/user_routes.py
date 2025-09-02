from fastapi import APIRouter, Depends, HTTPException, status,Response,Request
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, Token
from app.core import security
from app.deps import get_db
from app.db.user import User
from app.core.security import get_password_hash,verify_password
from app.core.security import create_token,get_current_User,verify_token
from app.core.security import auth2_schema
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(prefix="/users",          
    tags=["Authentication"] )

@router.post("/register",response_model=UserRead)
def register(user:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Already register")
    hashed_pwd=get_password_hash(user.password)
    new_user=User(
        email=user.email,
        hashed_password=hashed_pwd
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_token({"email": user.email})

    response.set_cookie(
    key="access_token",
    value=token,
    httponly=True,
    samesite="lax",
    max_age=1800,
    expires=1800
    )


    # Return the expected response model
    return {"access_token": token, "token_type": "bearer"}



@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_User)  # ensure only logged-in users can delete
):
    # Only allow users to delete themselves
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this user")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return None # 204 No Content: success, no body


@router.get("/me")
def get_current_user(request:Request,db:Session=Depends(get_db)):
    token=request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    email = verify_token(token)  # use your verify_token function
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return {"email": user.email}



