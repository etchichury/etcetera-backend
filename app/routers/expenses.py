from datetime import date
from fastapi import APIRouter

router = APIRouter()


@router.get("/expenses/")
def get_all_expenses():
    return [
        {"description": "Dominos", "value": 3290, "date": date.today()},
        {"description": "Lunch", "value": 1950, "date": date.today()},
    ]
