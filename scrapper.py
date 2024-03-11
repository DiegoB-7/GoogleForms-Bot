import requests
from bs4 import BeautifulSoup
import re
from models import Option

def get_questions_answers(url:str):
    # URL to fetch HTML from
    result = []
    
    url = "https://docs.google.com/forms/d/e/1FAIpQLSdJBgTUrrbzDfj1nI1NDVcue_mOA6dYua1yf0gTyxVbEoslbQ/viewform" 
    # Define custom headers with user-agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL with custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all elements with role="listitem"
        list_items = soup.find_all(attrs={"role": "listitem"})
        
        # Iterate over list items
        for list_item in list_items:
            # Extract question
            question = list_item.find('span').text.strip()
            sentinel_inputs = list_item.find_all("input", {"name": re.compile(r'^entry\..*_sentinel$')})
            sentinel_names = [input_element["name"] for input_element in sentinel_inputs]
            
            # Extract answers
            answers = []
            answer_divs = list_item.find_all('div', class_='ulDsOb')
            
            for answer_div in answer_divs:
                answer = answer_div.find('span').text.strip()
                answers.append(answer)
            
            data = Option(question, answers, sentinel_names[0])
            result.append(data)
            
        return result
    else:
        # Print an error message if the request was not successful
        print("Failed to retrieve HTML from", url)

