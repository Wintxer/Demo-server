# routes
import logging
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, HTTPException
from sqlalchemy.orm import Session

from demo_server import model
from demo_server.database import SessionLocal

logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_routes(app, templates):
    @app.get("/", response_class=HTMLResponse)
    def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "home"})

    # @app.get("/items/{item_id}")
    # def read_item(item_id: int, q: Optional[str] = None):
    #     return {"item_id": item_id, "q": q}

    @app.get("/execute", response_class=HTMLResponse)
    def read_exec(request: Request, url: str, site: str):
        print(url + " " + site);
        return templates.TemplateResponse("index.html", {"request": request, "path": "home"})

    @app.get("/login", response_class=HTMLResponse)
    def read_login(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "login"})

    @app.get("/signup", response_class=HTMLResponse)
    def signup(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "signup"})

    @app.get("/user", response_class=HTMLResponse)
    def read_user(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "user"})

    @app.post("/signup/", response_model=model.UserDTO, response_class=HTMLResponse)
    def create(request: Request, user: model.UserCreate, db: Session = Depends(get_db)):
        db_user = model.User(name=user.name).to_dto()
        if db_user:
            raise HTTPException(status_code=400, detail="Name already registered")
        db_new_user = model.User(name=user.name, password=user.password)
        db.add(db_new_user)
        db.commit()
        db.refresh(db_new_user)
        return templates.TemplateResponse("index.html", {"request": request, "path": "home", "user": db_new_user.name})

    @app.get("/user/settings/{data}")
    def read_settings(data: int):
        return {"data": data}
