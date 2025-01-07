from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime
    friends: list[int] = []


external_data = {
    'id': '123',
    'name': 'John Doe',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, 2, b'3'],
}

user = User(**external_data)
print(user)

print(user.id)