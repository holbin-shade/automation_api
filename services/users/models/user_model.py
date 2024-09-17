from pydantic import BaseModel, field_validator

class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str
    avatar_url: str

    # @field_validator("email", "name", "nickname", "uuid", "avatar_url")
    # def fields_are_not_empty(cls, value):
    #     if value == "" or value is None:
    #         raise ValueError("Fiels is empty")
    #     else:
    #         return value