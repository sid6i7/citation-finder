from fastapi import FastAPI
from model.model import Model

app = FastAPI()

@app.get("/get_citations")
def get_citations():
    model = Model()
    citations = model.get_citations()
    return citations