# routes
import logging
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, HTTPException, Form
from sqlalchemy.orm import Session

from demo_server.crud import get_user, create_user, create_google_sheet
from demo_server.database import get_db
from demo_server.model import User, UserDTO, UserCreate, RaffleDTO, RaffleCreate, Raffle, GoogleSheetCreate

logger = logging.getLogger(__name__)


def create_routes(app, templates):
    @app.get("/", response_class=HTMLResponse)
    def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "home"})

    # @app.get("/items/{item_id}")
    # def read_item(item_id: int, q: Optional[str] = None):
    #     return {"item_id": item_id, "q": q}

    @app.get("/execute", response_model=RaffleDTO, response_class=HTMLResponse)
    def read_exec(request: Request, url: str = Form(...), site: str = Form(...), db: Session = Depends(get_db)):
        raffle = RaffleCreate(url_raffle=url)
        db_new_raffle = Raffle(url=raffle.url_raffle)
        db.add(db_new_raffle)
        db.commit()
        return templates.TemplateResponse("index.html", {"request": request, "path": "home"})

    @app.get("/login", response_class=HTMLResponse)
    def read_login(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "login"})

    @app.get("/signup", response_class=HTMLResponse)
    def signup(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "path": "signup"})

    @app.get("/user", response_class=HTMLResponse)
    def read_user(request: Request, db: Session = Depends(get_db)):
        users = get_user(db, 23)
        return templates.TemplateResponse("index.html", {"request": request, "path": "user", "user": users})

    @app.post("/login/", response_model=UserDTO, response_class=HTMLResponse)
    def create_signup(request: Request, name: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
        user = UserCreate(name=name, password=password)
        db_new_user = create_user(db, user)
        return templates.TemplateResponse("index.html", {"request": request, "path": "home", "user": db_new_user.name})

    # @app.get("/user/settings")
    # def read_settings(google_sheet: str):
    #     return {"google_sheet": google_sheet}

    @app.post("/user/settings/", response_class=HTMLResponse)
    def create_settings(request: Request, url_google_sheet: str = Form(...), db: Session = Depends(get_db)):
        google_sheet = GoogleSheetCreate(url_google_sheet=url_google_sheet)
        db_new_google_sheet = create_google_sheet(db, google_sheet)
        return templates.TemplateResponse("index.html", {"request": request, "path": "user", "google_sheet": db_new_google_sheet.url_google_sheet})
