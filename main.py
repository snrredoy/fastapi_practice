from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def root():
    return{
        'message': 'Hello World'
    }

@app.get('/info/')
async def info():
    return{
        'name': 'Naeem',
        'roll': 12546,
        'department': 'CSE',
        'Intake': 36
    }

@app.get('/rest/{rest_id}')
async def rest(rest_id):
    return {
        'id': rest_id
    }