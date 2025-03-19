import requests
from bs4 import BeautifulSoup
from filter import is_relevant
import logging

def check_novonordisk():
    url = "https://www.novonordisk.com/careers/find-a-job/career-search-results.html?"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                       (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.warning(f"Failed to fetch {url} - Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # TODO: This depends on how jobs are listed – may need to adapt
        job_elements = soup.select(".job-listing")  # <- you'll need to inspect & confirm this selector

        jobs = []
        for el in job_elements:
            title = el.get_text(strip=True)
            link = el.get("href")

            job = {
                "title": title,
                "url": link,
                "description": "",  # optional: extract preview text if available
                "company": "Novo Nordisk"
            }

            if is_relevant(job):
                jobs.append(job)

        return jobs

    except Exception as e:
        logging.exception("Error scraping Novo Nordisk")
        return []
