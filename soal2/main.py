import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields 
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model 

app = FastAPI()



JWT_SECRET = 'jwtauth'

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password = fields.CharField(128)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

User_ = pydantic_model_creator(User, name='User')
User_In = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False 
    if not user.verify_password(password):
        return False
    return user 

@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid username or password'
        )

    user_obj = await User_.from_tortoise_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return {'access_token' : token, 'token_type' : 'bearer'}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid username or password'
        )

    return await User_.from_tortoise_orm(user)


@app.post('/users', response_model=User_)
async def create_user(user: User_In):
    user_obj = User(username=user.username, password=bcrypt.hash(user.password))
    await user_obj.save()
    return await User_.from_tortoise_orm(user_obj)

@app.get('/users/me', response_model=User_)
async def get_user(user: User_ = Depends(get_current_user)):
    return user    

# Database
DATABASE_URL = "mysql://root@localhost:3306/user"

register_tortoise(
    app, 
    db_url=DATABASE_URL,
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)
