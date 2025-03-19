import logging
from companies.novonordisk import check_novonordisk

# Configure logging to print to stdout with timestamps
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Starting job scraper...")

    try:
        check_novonordisk()
        logging.info("Novo Nordisk check complete.")
    except Exception as e:
        logging.error(f"Error during job check: {e}")

if __name__ == "__main__":
    main()
