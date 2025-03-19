import requests

def fetch_jobs():
    url = "https://careers.novonordisk.com/jobapi/jobs"
    response = requests.get(url)
    data = response.json()
    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "id": job["jobId"],
            "title": job["title"],
            "url": f"https://careers.novonordisk.com/job/{job['slug']}",
            "location": job["location"],
            "date": job["postedDate"],
        })
    return jobs
