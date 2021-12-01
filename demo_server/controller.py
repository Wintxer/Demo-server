# routes
import logging
from fastapi.responses import HTMLResponse
from fastapi import Request

logger = logging.getLogger(__name__)


def create_routes(app, templates):
    @app.get("/", response_class=HTMLResponse)
    def read_root(request: Request):
        logger.warning(HTMLResponse)
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

    @app.get("/user/settings/{data}")
    def read_settings(data: int):
        return {"data": data}
