from pydantic import BaseModel
from .expense import ExpenseBase


class BudgetBase(BaseModel):
    title: str
    description: str | None = None
    limit: int
    current_progress: int | None
    expenses: list[ExpenseBase]
