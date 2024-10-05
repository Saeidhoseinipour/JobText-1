import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import random

class JobScraper:
    def __init__(self):
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
        }
        # List of proxy IPs (replace with actual proxies)
        self.proxies_list = [
            {"http": "http://proxy1.com:8080", "https": "http://proxy1.com:8080"},
            {"http": "http://proxy2.com:8080", "https": "http://proxy2.com:8080"},
            # Add more proxies here...
        ]

    def get_random_proxy(self):
        """Return a random proxy from the list."""
        return random.choice(self.proxies_list)

    def scrape_jobs(self, url):
        """Scrape job listings from a job board website."""
        try:
            # Choose a random proxy for each request
            proxy = self.get_random_proxy()

            # Make a GET request with retry logic, timeout, and rotating proxy
            response = self.session.get(url, headers=self.headers, proxies=proxy, timeout=20)
            response.raise_for_status()

            # Parsing the response
            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find_all("div", class_="job-listing")
            for job in jobs:
                title = job.find("h2", class_="job-title").text.strip()
                company = job.find("div", class_="company").text.strip()
                location = job.find("div", class_="location").text.strip()
                description = job.find("div", class_="description").text.strip()
                job_url = job.find("a", class_="apply-link")["href"]
                date_posted = job.find("div", class_="date-posted").text.strip()

                print(f"Job Title: {title}, Company: {company}, Location: {location}")

        except requests.exceptions.ConnectionError as ce:
            print("Connection error occurred: ", ce)
        except requests.exceptions.Timeout as te:
            print("Timeout error occurred: ", te)
        except requests.exceptions.RequestException as e:
            print("An error occurred: ", e)

# Example usage:
scraper = JobScraper()
scraper.scrape_jobs("https://example-job-board.com/jobs")