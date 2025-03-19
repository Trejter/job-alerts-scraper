import os
import time
import schedule

import logging

logging.basicConfig(level=logging.INFO)

def scrape():
    logging.info("Starting to scrape...")
    # Your scraping logic
    logging.info("Finished scraping.")

if __name__ == "__main__":
    scrape()

from companies import novonordisk
from database import init_db, is_new
from filter import filter_jobs
from notifier import send_telegram

KEYWORDS = os.getenv("KEYWORDS", "").split(",")

def job_check():
    print("🔍 Checking for new jobs...")
    jobs = novonordisk.fetch_jobs()
    for job in jobs:
        if is_new(job["id"]):
            if filter_jobs([job], KEYWORDS):
                msg = f"🆕 {job['title']}\n📍 {job['location']}\n🔗 {job['url']}"
                send_telegram(msg)
                print(f"✅ Sent: {job['title']}")

if __name__ == "__main__":
    init_db()
    schedule.every(15).minutes.do(job_check)
    print("📡 Job watcher started on Railway...")

    while True:
        schedule.run_pending()
        time.sleep(60)


