from pydantic import BaseModel
from typing import Literal

class PredictionResponse(BaseModel):
    predicted_insurance_cost: float
    category: Literal["Low risk","Medium risk","High risk"]
