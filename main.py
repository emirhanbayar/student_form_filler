from filler import eokul
from studentclass import Student
import pandas as pd

if __name__ == "__main__":
    gir = eokul()
    gir.LogIn()

    dataset = pd.read_excel("data.xlsx")
    dataset = dataset.iloc[1:, [1, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]].values


    for data in dataset:    
        student = Student(data)
        gir.Assign(student)