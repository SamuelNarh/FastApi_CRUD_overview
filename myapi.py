
from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# GET - Get an Information
# POST - CREATE SOMETHING NEW
# PUT - UPDATE A DATA
# DELETE - DELETE SOMETHING
students ={
    1:{
        "name":"john",
        'age':17,
        "class":"year 12"
        
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

# @app.get("/")
# def index():
#     return {"name":"First Data"}


@app.get('/get-student/{student_id}')
def get_student(student_id:int = Path( description="The ID of the student you want to view" ,gt=0 ,lt=3)):
    return students[student_id]

# gt,lt  are for greater than and less than respectively

# QUERE PARAMETER
@app.get("/get-by-name") #no need to add  / at end because it is already added in url path
def get_student(*, name: Optional[str] ,test : int):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data":"Not Found"}

# Combining Query and Path
@app.get("/get-by-name/{student_id}")
def get_students_id(*, student_id:int ,name:Optional[str]):
    for student_id in students:
        if students[student_id]['name'] == name:
            return (students[student_id] , students[student_id])
    return {"Data":"Not Found"}


# REQUEST BODY 
@app.post('/create-student/{student_id}')
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error": "Student Exist"}
    students[student_id] = student
    return students[student_id]
        

@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not  exist"}
    if student.name != None: #if its not empty
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age =student.age
    if students.year != None:
        student[student_id].year = student.year
        
    return students[student_id]

@app.delete("delete-student/{student_id}")
def delete_student(student_id:int):
    if  student_id not in students:
        return {"error":"Student Does Not Exists"}
    del students[student_id]
    return {"message":"student successfully deleted"}
