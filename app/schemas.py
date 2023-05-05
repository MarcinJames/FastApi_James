from __future__ import annotations # Spróbuj dodać to: from __future__ adnotacje importu na górze pliku Pythona, bezpośrednio pod linią nagłówka: „”„ To jest linia nagłówka.”
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr



class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

