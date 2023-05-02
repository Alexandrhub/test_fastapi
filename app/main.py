from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router_auth, router_users

from app.pages.router import router as router_pages


app = FastAPI(
     title='Бронирование отелей',
     version='0.1.0',
)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_bookings)


app.include_router(router_pages)


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int]=Query(None, ge=1, le=5),
            has_spa: Optional[bool]=None,
        ):
            self.location = location
            self.date_from = date_from
            self.date_to = date_to
            self.stars = stars
            self.has_spa = has_spa



@app.get('/hotels/')
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
):
    return search_args




