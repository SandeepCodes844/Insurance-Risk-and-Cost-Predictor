from pydantic import BaseModel , Field , computed_field , field_validator
from typing import Literal , Annotated
from config.city_tier import TIER_1_CITIES , TIER_2_CITIES


#pydantic model for input data validation
class UserInput(BaseModel):

    age: Annotated[int, Field(..., ge=0, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kg")]
    height: Annotated[float, Field(..., gt=0, description="Height of the user in cm")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Annual income of the user in LPA")]
    smoker: Annotated[Literal["yes", "no"], Field(..., description="Whether the user is a smoker")]
    city: Annotated[str, Field(..., description="City of residence")]
    occupation: Annotated[Literal['retired', 'self employed', 'unemployed' , 'government job' , 'business owner' , 'private job' , 'student' , 'others'], Field(..., description="Occupation of the user")]

    @field_validator("city")
    @classmethod
    def normalize_city(cls, v:str) -> str:
      v = v.strip().title()
      return v

    @computed_field
    @property
    def bmi(self) -> float:
       return self.weight / (self.height / 100) ** 2

    @computed_field
    @property
    def lifestyle_score(self) -> "str":
      if self.smoker == "yes" and self.bmi > 30:
        return "high risk"
      elif self.smoker == "yes" or self.bmi > 30:
        return "medium risk"    
      else:        
        return "low risk"  
    
    @computed_field
    @property
    def age_group(self) -> "str":
      if self.age < 30:
        return "young"
      elif self.age < 60:
        return "middle-aged"
      else:
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> "str":
      if self.city in TIER_1_CITIES:
        return "tier 1"
      elif self.city in TIER_2_CITIES:
        return "tier 2"
      else:
        return "tier 3"