from fastapi import APIRouter, Depends, Response, status

from app.exceptions import IncorrectEmailOrPasswordException, UserAlreadyExistsException
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.dao import UsersDAO, UserAdminDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth, SUsers

router_auth = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

router_users = APIRouter(prefix="/users", tags=["Users"])


@router_auth.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user_data: SUserAuth) -> str:
    existing_user = await UsersDAO.select_all_filter_by(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    existing_user = await UserAdminDAO.select_all_filter_by(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_rows(email=user_data.email, hashed_password=hashed_password)

    return "Успешная регистрация"


@router_auth.post("/register_admin", status_code=status.HTTP_201_CREATED)
async def register_admin_user(user_data: SUserAuth) -> Response:
    existing_user = await UserAdminDAO.select_all_filter_by(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserAdminDAO.add_rows(email=user_data.email, hashed_password=hashed_password)

    return Response(status_code=status.HTTP_201_CREATED)


@router_auth.post("/login")
async def login_user(response: Response, user_data: SUserAuth) -> str:
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)

    return "Успешный вход"


@router_auth.post("/logout")
async def logout_user(response: Response) -> str:
    response.delete_cookie("booking_access_token")
    return "Успешный выход"


@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router_users.get("/all")
async def read_all_users(current_user: Users = Depends(get_current_user)) -> list[SUsers]:
    return await UsersDAO.select_all_filter()
