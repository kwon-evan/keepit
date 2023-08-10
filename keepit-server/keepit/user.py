from fastapi import APIRouter
from .dummy_users import users

user = APIRouter(prefix="/user")


# get all users
@user.get("/")
async def get_users():
    return users


# get user by id
@user.get("/{id}")
async def get_user(id: int):
    return users[id]
