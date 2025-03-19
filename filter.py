# filter.py

# Keywords to match in job titles or descriptions
KEYWORDS = [
    "Confluence",
    "Jira",
    "ScriptRunner",
    "API",
    "Administrator",
    "Developer"
]

def is_relevant(job):
    """
    Returns True if the job is relevant based on title or description.
    """
    job_text = (job.get("title", "") + " " + job.get("description", "")).lower()
    return any(keyword.lower() in job_text for keyword in KEYWORDS)
