from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model.model import Model

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.post("/api/get_citations/")
def get_citations(messages: dict):
    if messages:
        model = Model(messages['messages']) 
        citations = model.get_citations()
        return citations
    else:
        return {"error": "no data provided"}