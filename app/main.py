from fastapi import FastAPI
from .routers import budgets, expenses


app = FastAPI()

app.include_router(budgets.router)
app.include_router(expenses.router)


@app.get("/ping/")
def read_root():
    return {"result": "alive"}
