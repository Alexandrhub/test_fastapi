from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

from fastapi import FastAPI
from sqladmin import Admin, ModelView
from app.admin.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.admin.auth import authentication_backend

from app.bookings.router import router as router_bookings
from app.database import engine
from app.config import settings
from app.users.models import Users
from app.users.router import router_auth, router_users
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.pages.router import router as router_pages

from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis


app = FastAPI(
     title='Бронирование отелей',
     version='0.1.0',
)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_images)
app.include_router(router_pages)

app.mount("/static", StaticFiles(directory="app/static"), "static")



@app.on_event("startup")
def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
                               encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")






admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(RoomsAdmin)
admin.add_view(HotelsAdmin)




