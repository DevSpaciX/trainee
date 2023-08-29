
from db.engine import SessionLocal


#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_user_by_login(login: str, db: Session = Depends(get_db)):
#     return db.query(User).filter(User.login == login).first()

# Dependency to get database session
