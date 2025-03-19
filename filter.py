def filter_jobs(jobs, keywords):
    return [
        job for job in jobs
        if any(keyword.lower() in job["title"].lower() for keyword in keywords)
    ]
