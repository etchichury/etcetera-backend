from datetime import date
from pydantic import BaseModel


class ExpenseBase(BaseModel):
    description: str
    value: int
    date: date
