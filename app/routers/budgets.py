from fastapi import APIRouter

router = APIRouter()


@router.get("/budgets/")
async def read_budgets():
    return [{"name": "Groceries"}]
