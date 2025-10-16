from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Reuse existing CalculatorService from the Pyro5 implementation
from calculator import CalculatorService

app = FastAPI(title="CalculatorService API")

# In production, restrict origins to trusted domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

calc = CalculatorService()


class OpIn(BaseModel):
    a: float
    b: float


@app.get("/")
def root():
    return {"service": "CalculatorService", "ops": ["add", "subtract", "multiply", "divide"]}


@app.post("/add")
def add(inp: OpIn):
    return {"result": calc.add(inp.a, inp.b)}


@app.post("/subtract")
def subtract(inp: OpIn):
    return {"result": calc.subtract(inp.a, inp.b)}


@app.post("/multiply")
def multiply(inp: OpIn):
    return {"result": calc.multiply(inp.a, inp.b)}


@app.post("/divide")
def divide(inp: OpIn):
    try:
        return {"result": calc.divide(inp.a, inp.b)}
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))

