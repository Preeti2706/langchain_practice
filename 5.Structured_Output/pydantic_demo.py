from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'preeti'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com', 'cgpa':5}

student = Student(**new_student)

student_dict = dict(student)  #convert pydantic object to dictionary

print(student_dict['cgpa'])

student_json = student.model_dump_json() #convert pydantic object to json