from fastapi import APIRouter
from ..schemas.budget import BudgetCreate


router = APIRouter()


@router.get("/budgets/")
async def read_budgets():
    return [{"name": "Groceries"}]


@router.post("/budgets/", response_model=BudgetCreate)
async def create_budget(bugdet: BudgetCreate):
    return bugdet
