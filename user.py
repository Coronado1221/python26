import json
import os
from typing import Optional

USERS_FILE = "users.json"

class User:
    def __init__(self, user_id: int, name: str, nickname: Optional[str] = None):
        self.id = user_id
        self.name = name
        self.nickname = nickname or name

    def to_dict(self):
        return {"id": self.id, "name": self.name, "nickname": self.nickname}

    @staticmethod
    def from_dict(data):
        return User(user_id=data["id"], name=data["name"], nickname=data.get("nickname"))


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return [User.from_dict(u) for u in json.load(f)]

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=2)

def get_user_by_name(name: str, users):
    for user in users:
        if user.name.lower() == name.lower():
            return user
    return None

def get_next_user_id(users):
    if not users:
        return 1
    return max(u.id for u in users) + 1

def register_or_get_user(name: str, nickname: Optional[str] = None):
    users = load_users()
    user = get_user_by_name(name, users)
    if user:
        return user
    new_id = get_next_user_id(users)
    user = User(user_id=new_id, name=name, nickname=nickname)
    users.append(user)
    save_users(users)
    return user
