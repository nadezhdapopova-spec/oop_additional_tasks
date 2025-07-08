import json
import os

from src.tasks import Task
from src.user import User


def read_json(path: str) -> list[dict]:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf8") as f:
        data = json.load(f)

    return data


def create_objects_from_json(users_json: list[dict]) -> list:
    users = []
    for user in users_json:
        tasks = []
        for task in user["task_list"]:
            tasks.append(Task(**task))
        user["task_list"] = tasks
        users.append(User(**user))

    return users


if __name__ == "__main__":
    json_users = read_json(r"../data/data.json")
    obj_users = create_objects_from_json(json_users)
    print(obj_users[0].username)
    print(obj_users[0].task_list)
