from fastapi import FastAPI
from pydantic import BaseModel
from notebooks.generation_test import generate_answer


app= FastAPI()

class QueryRequest(BaseModel):

    question : str


@app.get('/health')
def home():
    return {
        'message' : 'Document Assistant Project running successfully!'
    }    


@app.post('/query')
async def generate_response(query: QueryRequest):

    answer = generate_answer(query.question)
    return {'answer':answer}
