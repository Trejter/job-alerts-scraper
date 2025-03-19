from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def check_novonordisk():
    # Set Chrome options for headless mode
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Set up the WebDriver service and pass it to the constructor
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.novonordisk.com/careers/find-a-job/career-search-results.html?"
    driver.get(url)

    # Simulate clicking the 'Load More' button or handle dynamic content
    while True:
        try:
            # Find and click the 'Load More' button
            load_more_button = driver.find_element(By.XPATH, '//button[contains(text(), "Load more")]')
            load_more_button.click()
            time.sleep(2)  # Wait for new results to load
        except:
            break  # No more 'Load More' button

    # Extract job titles using the correct class 'bold h4' for job titles
    job_elements = driver.find_elements(By.CLASS_NAME, "bold.h4")
    jobs = []

    for job in job_elements:
        title = job.text  # Get the text of the job title
        logging.info(f"Found job: {title}")
        jobs.append({"title": title})

    driver.quit()
    return jobs
