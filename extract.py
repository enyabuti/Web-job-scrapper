import requests

def scrape_jobs(app_id, app_key, location=None, num_pages=1):
    """
    Fetch job postings from Adzuna API.

    Args:
        app_id (str): Your Adzuna API app ID.
        app_key (str): Your Adzuna API key.
        location (str): Job location (e.g., 'Remote').
        num_pages (int): Number of pages to fetch.

    Returns:
        list: A list of job postings as dictionaries.
    """
    base_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"
    jobs = []

    for page in range(1, num_pages + 1):
        params = {
            'app_id': app_id,
            'app_key': app_key,
            'page': page
        }
        if location:
            params['where'] = location

        print(f"Request URL: {base_url}")
        print(f"Request Params: {params}")

        response = requests.get(base_url, params=params)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            results = response.json().get('results', [])
            jobs.extend(results)
            print(f"Fetched {len(results)} jobs from page {page}")
        else:
            print(f"Error fetching page {page}: Status Code {response.status_code}")
            print(f"Response: {response.text}")
            break

    return jobs
