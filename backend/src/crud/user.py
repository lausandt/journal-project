from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.contrib.pydantic import PydanticModel
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.core.models import User
from src.schemas.token import Status
from src.schemas.user import UserOutSchema

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


async def get_user(username: str) -> type[PydanticModel]:
    return await UserOutSchema.from_queryset_single(User.get(username=username))


async def get_users() -> list[type[PydanticModel]]:
    return await UserOutSchema.from_queryset(User.all())


async def create_user(user) -> type[PydanticModel]:
    user.password = pwd_context.hash(user.password)

    try:
        user_obj = await User.create(**user.model_dump(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(
            status_code=401, detail=f'Sorry, username {user.username} already exists.'
        )

    return await UserOutSchema.from_tortoise_orm(user_obj)


async def delete_user(user_id: int, current_user: User) -> Status:  # add current user
    try:
        db_user = await UserOutSchema.from_queryset_single(User.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')

    if db_user.id == current_user.id | current_user.superuser:
        del_user = await User.filter(id=user_id).delete()
        if not del_user:
            raise HTTPException(status_code=404, detail=f'User {user_id} not found')
        return Status(f'Deleted user {user_id}')

    raise HTTPException(status_code=403, detail='Not authorized to delete')
