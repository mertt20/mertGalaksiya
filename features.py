from pydantic import BaseModel

# Class describes features 
class feature(BaseModel):
    #To express the Number of pregnancies
    Pregnancies : int

    #To express the Glucose level in blood
    Glucose : int


    #To express the Body mass index
    BMI: float

    #	To express the Diabetes percentage
    DiabetesPedigreeFunction: float
