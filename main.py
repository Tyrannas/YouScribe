from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from algo import init_data, recommend

app = FastAPI()


# Configuration des templates
templates = Jinja2Templates(directory="templates")
DS = init_data('./data')


class RecommendationRequest(BaseModel):
    book: str = None
    user: str = None


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "books": DS.books.titre.tolist()[0:1500], "users": DS.users.username.tolist()[0:1500]})


# @app.get("/users")
# async def get_users():
#     users = DS.users['username'].tolist()
#     return {"users": users}
#
#
# @app.get("/books")
# async def get_books():
#     books = DS.books['titre'].tolist()
#     return {"books": books}


@app.post("/recommend")
async def recommend_route(request: RecommendationRequest):
    if request.user:
        recommendations = recommend(user=request.user)
    elif request.book:
        recommendations = recommend(book=request.book)
    else:
        return {"error": "Please provide either a book or a user"}
    return recommendations
