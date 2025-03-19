from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def check_novonordisk():
    # Set Chrome options for headless mode
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver and pass options separately
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    url = "https://www.novonordisk.com/careers/find-a-job/career-search-results.html?"
    driver.get(url)

    # Simulate clicking the 'Show More' button or handle dynamic content
    while True:
        try:
            # Find and click the 'Show More' button
            show_more_button = driver.find_element_by_xpath('//button[contains(text(), "Show more")]')
            show_more_button.click()
            time.sleep(2)
        except:
            break  # No more 'Show More' button

    job_elements = driver.find_elements_by_class_name("job-listing-class-name")
    jobs = []

    for job in job_elements:
        title = job.find_element_by_class_name("job-title-class-name").text
        location = job.find_element_by_class_name("job-location-class-name").text
        jobs.append({"title": title, "location": location})

    driver.quit()
    return jobs
