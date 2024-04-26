from tortoise.contrib.pydantic import pydantic_model_creator

from src.core.models import User

UserInSchema = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
UserOutSchema = pydantic_model_creator(
    User,
    name='UserOut',
    exclude=[
        'password',
        'active',
        'superuser',
        'creadate',
        'modate',
    ],
)
UserDatabaseSchema = pydantic_model_creator(User, name='User', exclude=['creadate', 'modate'])
