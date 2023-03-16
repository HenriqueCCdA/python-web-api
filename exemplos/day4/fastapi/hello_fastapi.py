from  enum import Enum
from fastapi import FastAPI


app = FastAPI()


class ListOption(str, Enum):
    user = "user"
    department = "department"
    account = "account"



@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption):

    if list_option == ListOption.user:
        data = ["jim", "pam", "dwight"]
    elif list_option == ListOption.department:
        data = ["Sales", "Menagement", "IT"]
    elif list_option == ListOption.account:
        data = [1234, 8888, 9898]

    return {list_option: data}


@app.get("/user/list")
async def user_list():
    return {"users": ["jim", "pam", "dwight"]}

@app.get("/user/{username}")
async def user_profile(username: str):
    return {"data": username}


@app.get("/acount/{number}")
async def acount_detail(number: int):
    return {"acount": number}

@app.get("/import/{filepath:path}")
async def import_file(filepath: str):
    return {"importing": filepath}
