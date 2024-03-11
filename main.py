import re
import string
from urllib.parse import quote
from scrapper import get_questions_answers
from shared import generate_random_responses,format_url_params,open_browser_fill_form_submit
import random

def submit_forms(url: str, qty_forms_submited: int):
    """
    Submits multiple forms to a Google Form.

    Args:
        url (str): The URL of the Google Form.
        qty_forms_submited (int): The number of forms to submit.

    Returns:
        None
    """
    # The result are the questions, the id of the question and also their answers
    result = get_questions_answers(url)

    for i in range(qty_forms_submited):
        random_form = generate_random_responses(result)

        url_to_fetch = format_url_params(url, random_form)

        success = open_browser_fill_form_submit(url_to_fetch)
        if success:
            print(f"Form {i+1} submitted successfully")
        else:
            print(f"Failed to submit form {i+1}")

if __name__ == "__main__":
    # Setup variables
    url:str = "Your URL here"
    qty_forms_submited:int = 50

    submit_forms(url, qty_forms_submited)
        
        
        
        
        
        
        