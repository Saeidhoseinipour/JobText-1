import os
import time
import requests
from bs4 import BeautifulSoup
import json
import scipy.io as sio
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class JobScraper:
    def __init__(self, save_dir, headers):
        self.save_dir = save_dir
        self.headers = headers
        self.all_jobs_data = []

    def clean_persian_text(self, text):
        return text.strip()

    def extract_job_features(self, subpage_soup):
        job_features = {}
        additional_features = {
            'job_category': ('div', 'job-category'),
            'job_location': ('div', 'job-location'),
            'employment_type': ('div', 'employment-type'),
            'min_experience': ('div', 'min-experience'),
            'salary': ('div', 'salary'),
            'gender': ('div', 'gender'),
            'military_status': ('div', 'military-status'),
            'education_level': ('div', 'education-level'),
            'company_intro': ('div', 'company-intro'),
            'skills_required': ('div', 'skills-required'),
        }

        for feature, (tag, class_name) in additional_features.items():
            feature_tag = subpage_soup.find(tag, class_=class_name)
            if feature_tag:
                job_features[feature] = self.clean_persian_text(feature_tag.get_text())

        job_features['content_snippet'] = self.clean_persian_text(subpage_soup.get_text())

        return job_features

    def get_links(self):
        return []

    def scrape_jobs(self):
        subpage_links = self.get_links()

        while subpage_links:
            subpage_url = subpage_links.pop()
            try:
                subpage_response = requests.get(subpage_url, headers=self.headers, verify=False, timeout=10)
                subpage_response.raise_for_status()

                subpage_soup = BeautifulSoup(subpage_response.text, 'html.parser')
                
                job_data = self.extract_job_features(subpage_soup)

                if job_data:
                    self.all_jobs_data.append(job_data)

                    job_title = job_data.get('job_title', 'JobInja')
                    file_path = os.path.join(self.save_dir, f"{job_title}.txt")
                    with open(file_path, 'w', encoding='utf-8') as file:
                        for key, value in job_data.items():
                            file.write(f"{key.capitalize()}: {value}\n")

                    print(f"URL: {subpage_url}")
                    for key, value in job_data.items():
                        print(f"{key.capitalize()}: {value}")
                    print("\n")

                time.sleep(1)

            except requests.exceptions.RequestException as e:
                logger.error(f"An error occurred while accessing {subpage_url}: {e}")

    def save_dataset(self):
        mat_file_path = os.path.join(self.save_dir, "jobinja_data.mat")
        json_file_path = os.path.join(self.save_dir, "jobinja_data.json")

        job_data_dict = {f"job_{i}": job for i, job in enumerate(self.all_jobs_data)}
        
        sio.savemat(mat_file_path, job_data_dict)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(self.all_jobs_data, json_file, ensure_ascii=False, indent=4)

        print(f"Dataset saved as .mat file at: {mat_file_path}")
        print(f"Dataset saved as .json file at: {json_file_path}")

    def display_dataset(self):
        df = pd.DataFrame(self.all_jobs_data)
        print(df)
        return df

# Example usage
if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    save_dir = "./jobinja_data"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    scraper = JobScraper(save_dir, headers)
    scraper.scrape_jobs()
    scraper.save_dataset()
    scraper.display_dataset()
