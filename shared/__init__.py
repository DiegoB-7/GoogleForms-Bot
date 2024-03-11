import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import urllib.parse
import string

def generarCorreo(numControl):
    return "L"+numControl + "@tectijuana.edu.mx"

def generate_random_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_responses(options):
    response = {
        option.id: random.choice(option.answers) for option in options
    }
    
    return response

def format_url_params(base_url, response):
    """
    Formats the URL parameters by encoding the response values and appending them to the base URL.

    Args:
        base_url (str): The base URL to which the query parameters will be appended.
        response (dict): A dictionary containing the response values.

    Returns:
        str: The formatted URL with the encoded response values as query parameters.
    """
    # Encode the response values to handle spaces
    encoded_response = {key: urllib.parse.quote(value) for key, value in response.items()}
    
    # Join the response items to form query parameters
    query_params = "&".join([f"{key}={value}" for key, value in encoded_response.items()])
    
    # Append the query parameters to the base URL
    formatted_url = f"{base_url}?code={generate_random_code()}&{query_params}"
    
    return formatted_url

def open_browser_fill_form_submit(url):
    """
    Opens a browser, fills a form, and submits it.

    Args:
        url (str): The URL of the form to be filled.

    Returns:
        bool: True if the form submission is successful, False otherwise.
    """
    # Initialize a Chrome WebDriver (you need to download chromedriver from https://chromedriver.chromium.org/)
    driver = webdriver.Chrome()

    # Open the URL
    driver.get(url)
    
    # Wait for the form to load
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    except TimeoutException:
        print("Form not found")
        driver.quit()
        return False
    
    # Find and click the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']"))
    )
    submit_button.click()
    
    # Wait for submission to complete
    time.sleep(1)
    
    # Close the browser
    driver.quit()
    return True