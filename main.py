from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    admin = 'admin'
    manager = 'manager'
    hr = 'hr'
    staff = 'staff'

app= FastAPI()

# Simple hello
@app.get('/')
async def root():
    return{
        'message': 'Hello World'
    }


# User info with path
@app.get('/info/')
async def info():
    return{
        'name': 'Naeem',
        'roll': 12546,
        'department': 'CSE',
        'Intake': 36
    }


# using path parameter
@app.get('/rest/{rest_id}')
async def rest(rest_id: int):
    return {
        'id': rest_id
    }


# using path parameter and enum
@app.get('/role/{role}')
async def role(role: Role):
    if role is Role.admin:
        return {'role': role, 'message': 'Role is admin.'}
    if role.value == 'manager':
        return {'role': role, 'message': 'Role is manager.'}
    if role is Role.hr:
        return {'role': role, 'message': 'Role is hr.'}
    if role is Role.staff:
        return {'role': role, 'message': 'Role is staff.'}


# use required query parameter with slice 
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Foot"}, {"item_name": "Bart"}, {"item_name": "Bazt"}]
@app.get('/item/')
def items(skip: int, limit: int):
    return fake_items_db[skip : skip + limit]


# use optional and default query parameter with slice
@app.get('/items/')
def items(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]

# use optional query parameter
@app.get("/optionalQuery/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# use query parameter type conversion
@app.get('/num/{num_id}')
async def number(num_id: str, q : str | None = None, short: bool = False):
    num = {'num': num_id}
    if q:
        num.update({'q': q})
    if not short:
        num.update({
            'description': 'This is an amazing item that has a long description.'
        })

    return num


# Multiple path and query parameters
@app.get('/user/{user_id}/num/{num_id}')
async def number(num_id: str, user_id: str, q : str | None = None, short: bool = False):
    num = {'user': user_id, 'num': num_id}
    if q:
        num.update({'q': q})
    if not short:
        num.update({
            'description': 'This is an amazing item that has a long description.'
        })

    return num

# Item create api.
class Item(BaseModel):
    name: str 
    description: str | None = None
    price: float

@app.post('/createItem/')
async def createItem(item: Item):
    return item


#  Item update with request body + path parameter
@app.put("/createItem/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# Request body + path + query parameters
@app.put("/createItems/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result