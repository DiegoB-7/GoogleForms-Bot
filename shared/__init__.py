import random


def generarCorreo(numControl):
    return "L"+numControl + "@tectijuana.edu.mx"


def generate_random_responses(options):
    response = {
        option.id: random.choice(option.answers) for option in options
    }
    
    return response

def format_url_params(base_url,response):
    tmp_url = "&".join([f"{key}={value}" for key, value in response.items()])
    
    url = f"{base_url}{tmp_url}"
    
    return url

def open_browser_fill_form_submit(url, form_data):
    # Initialize a Chrome WebDriver (you need to download chromedriver from https://chromedriver.chromium.org/)
    driver = webdriver.Chrome('/path/to/chromedriver')
    
    # Open the URL
    driver.get(url)
    
    # Wait for the form to load
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    except TimeoutException:
        print("Form not found")
        driver.quit()
        return False
    
    # Fill out the form with the provided data
    for question_id, answer in form_data.items():
        input_field = driver.find_element_by_css_selector(f"input[name='{question_id}']")
        input_field.send_keys(answer)
    
    # Find and click the submit button
    submit_button = driver.find_element_by_xpath("//div[@role='button' and contains(text(), 'Submit')]")
    submit_button.click()
    
    # Wait for submission to complete
    time.sleep(2)
    
    # Close the browser
    driver.quit()
    return True