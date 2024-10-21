import requests
from bs4 import BeautifulSoup
import time

# Define the target URL
url = "https://jobinja.ir/"

# Send a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
try:
    response = requests.get(url, headers=headers, verify=False, timeout=10)
    response.raise_for_status()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all the links to tabs or subpages
    links = soup.find_all('a', href=True)
    
    # Collect unique links to avoid repetition
    base_url = "https://jobinja.ir"
    subpage_links = set()

    for link in links:
        href = link['href']
        if href.startswith('/'):  # It's a relative link
            full_url = base_url + href
        elif href.startswith('http'):
            full_url = href
        else:
            continue  # Skip if the href doesn't look like a valid link

        subpage_links.add(full_url)

    # Extract text from each subpage
    for subpage_url in subpage_links:
        try:
            subpage_response = requests.get(subpage_url, headers=headers, verify=False, timeout=10)
            subpage_response.raise_for_status()

            # Parse the HTML content of the subpage
            subpage_soup = BeautifulSoup(subpage_response.text, 'html.parser')
            
            # Extract all text from the subpage
            subpage_text = subpage_soup.get_text(strip=True)

            # Print a snippet of the extracted text from each subpage
            print(f"URL: {subpage_url}\nContent Snippet: {subpage_text[:1000]}\n")

            # To avoid overwhelming the server, add a short delay
            time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while accessing {subpage_url}: {e}")

except requests.exceptions.SSLError as e:
    print(f"SSL error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
