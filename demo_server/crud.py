from sqlalchemy.orm import Session

from demo_server.model import User, UserCreate


def get_user(db: Session, user_id: int):
    print(user_id)
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(name=user.name, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_raffles():
    raise NotImplementedError()


def get_raffle():
    raise NotImplementedError()


def create_raffle():
    raise NotImplementedError()


def get_site():
    raise NotImplementedError()


def get_google_sheet():
    raise NotImplementedError()


def create_google_sheet():
    raise NotImplementedError()
