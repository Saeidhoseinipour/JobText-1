[![](https://badgen.net/badge/license/Apache/blue?icon=instgrame)](LICENSE)
[![](https://badgen.net/badge/Job/Inja/blue?icon=instgrame)]()
[![](https://badgen.net/badge/API/Text/blue?icon=instgrame)]()



# Tasks
🔍 
- [ ] Read and analyze source codes
- [ ] Dataset exploration and storytelling
- [ ] Review available filtering features on main website
- [ ] Primary focus on job descriptions for each Job ID
- [ ] Clean text data
- [ ] Create text corpus
- [ ] Tokenization process
- [ ] Remove stop words
- [ ] Generate Job-Word Matrix
- [ ] Calculate TF-IDF Job-Word Matrix
- [ ] Create heatmap visualization of Job-Word Matrix
- [ ] Identify and analyze top 20 jobs
- [ ] Extract and analyze top 20 words



# 🏢💼 Jobinja Job Listings Scraper 🔍💻

This repository contains a 🐍 Python script that scrapes job listings from [Jobinja](https://jobinja.ir/). The script is designed to extract detailed information from job ads, such as job title 📋, job type ⏱️, location 📍, and other relevant attributes, and output the data for further 📊 analysis.

## ✨ Features
- **Scrape Job Listings**: Extracts information ℹ️ from job listings available on the Jobinja 🌐 website.
- **Detailed Data Extraction**: Collects various attributes including job title 📜, company name 🏢, location 📍, work experience requirements 💼, contract type 📃, gender 🚻, minimum salary 💰, and education level 🎓.
- **Data Sorting and Display**: Organizes the extracted data based on specified attributes and displays it in a tabular format 🧮 for easy analysis.
- **Save Extracted Data**: Saves the sorted job listings as individual text files 📄 in a specified directory for later review.

## 🛠️ Requirements
- 🐍 Python 3.x
- The following Python libraries are required:
  - `requests`
  - `BeautifulSoup` from `bs4`
  - `pandas`
  - `os`

To install the dependencies, run:

```sh
pip install requests beautifulsoup4 pandas
```

## 🚀 Usage

### 1. 🔄 Clone the Repository

   ```sh
   git clone https://github.com/yourusername/jobinja-job-scraper.git
   cd jobinja-job-scraper
   ```

### 2. 📝 Edit the Main Script

   Update the base URL 🔗 or headers 📋 if necessary:

   ```python
   url = "https://jobinja.ir/"
   headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
   }
   scraper = JobinjaScraper(url, headers)
   scraper.scrape()
   scraper.descriptive_statistics()
   scraper.sort_data()
   ```

### 3. ▶️ Run the Script

   Execute the script by running:

   ```sh
   python jobinja_scraper.py
   ```

   The script will scrape data from Jobinja 🌐, generate descriptive statistics 📊, and display sorted job data 📋. It will also save individual job data into `.txt` files 📁 in `C:/Users/negin/jobinja_sorted_data`.

## 📚 Class Description

### `JobinjaScraper`

- **`__init__(self, base_url, headers)`**: Initializes the scraper with the base URL 🔗 and headers 📋.
- **`get_links(self)`**: Retrieves all relevant links 🔗 from the Jobinja base page for further processing.
- **`extract_subpage_text(self)`**: Extracts job attributes such as job title 📋, type ⏱️, location 📍, company 🏢, and other relevant details from each subpage.
- **`scrape(self)`**: Executes the process by calling `get_links` 🔗 and `extract_subpage_text` 📜 to gather job data 🗂️.
- **`descriptive_statistics(self)`**: Uses `pandas` to generate descriptive statistics 📊 for the dataset.
- **`sort_data(self)`**: Sorts the job data based on attributes like job title 📜, job type ⏱️, location 📍, etc., and displays the data in a structured matrix 🧮. It also saves the sorted data into text files 📁 for easy access.

## 🖨️ Output
- **Console Output**: Displays scraped job data 📋, descriptive statistics 📊, and a sorted data matrix 🧮.
- **Text Files**: Each job listing is saved as an individual text file 📄 in `C:/Users/negin/jobinja_sorted_data` with detailed job information.

## 📝 Example Output
```
URL: https://jobinja.ir/job/listing-url
Content Snippet: [Snippet of the job description]
Job Title: Software Developer
Job Type: Full-Time
Job Location: 📍 Tehran
Company Name: Example Co.
Contract Type: Permanent 📃
Work Experience: 3-5 Years 💼
Min Salary: 💰 40,000,000 IRR
Gender: 🚻 Female
Education Level: 🎓 Bachelor's Degree
```

## 🗒️ Notes
- The script includes error handling for SSL errors 🔒 and generic request errors ❗ to manage connectivity issues smoothly.
- Requests to the server are spaced out with a time delay ⏳ to avoid overwhelming the server (`time.sleep(1)`).

## ⚖️ License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to submit a pull request 📥 if you have any improvements ✨ or bug fixes 🐛. All contributions are welcome 🤗.


