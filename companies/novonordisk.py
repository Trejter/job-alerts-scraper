import requests
import logging

def check_novonordisk():
    url = "https://www.novonordisk.com/your-career/job-opportunities.html"
    response = requests.get(url)
    
    if response.status_code != 200:
        logging.warning(f"Failed to fetch {url} - Status code: {response.status_code}")
        return

    html = response.text

    # Example logic — you’d replace this with real parsing
    if "Poland" in html or "Remote" in html:
        logging.info("✅ Found job(s) matching criteria!")
    else:
        logging.info("❌ No jobs found matching criteria.")
