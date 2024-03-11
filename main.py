import re
import string
from urllib.parse import quote
from scrapper import get_questions_answers
from shared import generate_random_responses,format_url_params
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

# listName = ["Juan", "Pedro", "Maria", "Jose", "Luis", "Ana", "Rosa", "Carlos", "Jorge", "Miguel", "Raul", "Javier", "Sofia", "Laura", "Daniela", "Fernanda", "Diego", "Manuel", "Ricardo", "Roberto", "Fernando", "Jesús", "Alejandro", "Mariana", "Andrea", "Gabriela", "Paula", "Valentina", "Camila", "Sara", "Santiago", "Sebastian", "Mateo", "Nicolas", "Samuel", "David", "Daniel", "Emilio", "Emiliano", "Emilia", "Emiliana"]
# lastNameList = ["Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Flores", "Torres", "Rivera", "Gomez", "Diaz", "Reyes", "Morales", "Cruz", "Ortiz", "Santiago", "Gutierrez", "Chavez", "Ramos", "Vasquez", "Vargas", "Castillo", "Jimenez", "Moreno", "Romero", "Alvarez", "Ruiz", "Pineda", "Herrera", "Medina", "Aguilar", "Guerrero", "Mendoza"]

# numeroDeControl = [
#     '20213032', '22210320', '22210280', '22210332', '22210281', '21211909', '21212047', 
#     '22210335', '22210318', '22210881', '20212404', '21211912', '21211959', '22210306', 
#     '19212434', '22210880', '22210301', '22210364', '22210297', '22210277', 'L22211207', 
#     '22211550', '21210354', '22210313', '20211767', '21211943', '21211913', '19211725', '21212061', '21211940'
# ]

if __name__ == "__main__":
    #Setup variables
    url:str = "https://docs.google.com/forms/d/e/1FAIpQLSdJBgTUrrbzDfj1nI1NDVcue_mOA6dYua1yf0gTyxVbEoslbQ/viewform"
    qty_forms_submited = 30
    
    #The result are the questions, the id of the question and also their answers
    result = get_questions_answers(url)
    
    for i in range(qty_forms_submited):
        random_form = generate_random_responses(result)
        url_to_fetch = format_url_params(url,random_form)
        
        success = open_browser_fill_form_submit(url, random_form)
        if success:
            print(f"Form {i+1} submitted successfully")
        else:
            print(f"Failed to submit form {i+1}")
        
        
        
        
        
        
        