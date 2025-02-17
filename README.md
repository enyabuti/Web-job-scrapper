# Web-job-scrapper
A Python application that scrapes job listings from LinkedIn and Glassdoor using Selenium.

# Web Job Scraper

A Python application that scrapes job listings from LinkedIn and Glassdoor using Selenium.

![image](https://github.com/user-attachments/assets/3eba6f74-464b-4520-b734-b71c5c261dd2)


## 📚 Overview

This tool automatically gathers job postings from the past week across multiple job platforms (currently LinkedIn and Glassdoor) for specified keywords. Perfect for job seekers who want to stay on top of new opportunities without manually visiting multiple sites.

## ✨ Features

- 🔍 Scrapes jobs posted within the last 7 days
- 🔄 Supports multiple job platforms (LinkedIn, Glassdoor)
- 🤖 Uses headless browser to minimize resource usage
- ✅ Validates job listings to ensure data quality
- 📊 Provides summary statistics of jobs found by source

## 🛠️ Technical Implementation

### Browser Automation

The application uses Selenium WebDriver with Chrome in headless mode for efficient scraping:

```python
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)
```

### Data Quality

Jobs are validated before being added to ensure complete information:

```python
def validate_job(job_data):
    required_fields = {
        'Job Title': str,
        'Location': str,
        'Company': str
    }
    
    for field, field_type in required_fields.items():
        if field not in job_data or not isinstance(job_data[field], field_type) or not job_data[field].strip():
            return False
    return True
```

### Error Handling

The application uses multi-level exception handling to ensure robustness:
- Try-except blocks for individual job extractions
- Source-level error handling
- Global exception handling in the main scraping function

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Chrome browser
- Selenium WebDriver

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/web-job-scraper.git
cd web-job-scraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

By default, the script searches for "Python Developer" positions. To modify the search keyword, update the `scrape_jobs()` call in the main block.

## 📝 Sample Output

The script provides a summary of jobs found:

```
Starting job scraping...
Scraping jobs posted since 2024-02-10...

Scraping LinkedIn...
LinkedIn US Job Found: Senior Python Developer at TechCorp
LinkedIn US Job Found: Python Backend Developer at StartupInc
...

Scraping Glassdoor...
Glassdoor US Job Found: Python Developer at EnterpriseSystem
...

Total jobs found from past week: 47

Jobs by source:
LinkedIn: 32 jobs
Glassdoor: 15 jobs
```

## 📋 Future Enhancements

- [ ] Add support for Indeed and Monster
- [ ] Implement advanced filtering (salary range, job type)
- [ ] Create a database to track jobs over time
- [ ] Add email notifications for new matching positions
- [ ] Implement scheduler for daily/weekly runs

## 👨‍💻 Development

This project was initially self-started and developed over a couple of weeks, with significant enhancements made using Cursor AI. It demonstrates how AI-assisted coding can streamline development while preserving the programmer's vision and architecture decisions.

## ⚠️ Disclaimer

Web scraping may be against the Terms of Service of some websites. This tool is for educational purposes only. Please review the Terms of Service of any website before scraping it.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [Chrome WebDriver](https://chromedriver.chromium.org/)
- [Cursor AI](https://cursor.sh/)

---

If you find this project useful, please consider giving it a ⭐!
