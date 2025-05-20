from pydantic import BaseModel,field_validators, Field
from typing import Optional, Dict, Any, List
from pydantic import BaseModel,compute_field, model_validator
#schema for user

class UserModel(BaseModel):
    id: int
    name: str 
    email : str
    password: str

input_data = {
    "id": 1,
    "name": "John Doe",
    "email": "muanjas",
    "password": "secret" 
} 
user = UserModel(**input_data)
print(user)

class EmployeMode(BaseModel):
    id: int
    name: str = Field(...,
    min_length=3,
    max_length=50,
    description="Name of the employee",
    )
    department: Optional[str] = 'Computer Science'
    salary:int = Field(...,
    ge=1,
    le=1000000000,
    description="Salary of the employee",
    )
    email: str = Field(...,
    regex= r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",)

class SignUp(BaseModel):
    username: str = Field(...,
    min_length=3,
    max_length=50,
    description="Name of the employee",
    )
    email: str = Field(...,
    regex= r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",)
    password: str = Field(...,
    min_length=8,
    max_length=20,
    description="Password of the employee",
    )
    confirm_password: str = Field(...,
    min_length=8,
    max_length=20,  
    description="Password of the employee",
    )
    @model_validator('confirm_password')
    def validate_confirm_password(cls, confirm_password, values):
        password = values.get('password')
        if password is not None and confirm_password != password:
            raise ValueError('Passwords do not match')
        return confirm_password

class ProductModel(BaseModel):
    id: int
    name: str = Field(...,
    min_length=3,
    max_length=50,
    description="Name of the product",
    )
    price: float = Field(...,
    ge=1,
    le=1000000000,
    description="Price of the product",
    )
    quantity: int = Field(...,
    ge=1,
    le=1000000000,
    description="Quantity of the product",
    )
    @compute_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity      


class BookingModel(BaseModel):
    user_id: int
    room_id: int
    night: int = Field(...,
    ge=1)
    rate_per_night: float
    @compute_field
    @property
    def total_amount(self)->float:
        return self.night*self.rate_per_night

