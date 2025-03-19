import sqlite3

def init_db():
    conn = sqlite3.connect("jobs.db")
    conn.execute("CREATE TABLE IF NOT EXISTS seen (job_id TEXT PRIMARY KEY)")
    conn.close()

def is_new(job_id):
    conn = sqlite3.connect("jobs.db")
    result = conn.execute("SELECT 1 FROM seen WHERE job_id = ?", (job_id,))
    exists = result.fetchone() is not None
    if not exists:
        conn.execute("INSERT INTO seen (job_id) VALUES (?)", (job_id,))
        conn.commit()
    conn.close()
    return not exists
