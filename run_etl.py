import sys
import os
from datetime import datetime
from pathlib import Path
import json

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from main import scrape_jobs

def generate_interactive_html(jobs):
    """Generate an interactive HTML page for job listings"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Remote Job Listings</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
                margin: 40px auto;
                max-width: 1200px;
                padding: 0 20px;
                background-color: #f5f7fa;
            }
            .search-container {
                margin: 20px 0;
                padding: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }
            .search-box {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            .filters {
                display: flex;
                gap: 10px;
                margin-top: 10px;
            }
            .filter-btn {
                padding: 8px 15px;
                background: #1F4E78;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .filter-btn:hover {
                background: #2c3e50;
            }
            .job-card {
                background: white;
                margin: 15px 0;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }
            .job-title {
                color: #1F4E78;
                font-size: 1.2em;
                margin: 0 0 10px 0;
            }
            .job-meta {
                display: flex;
                gap: 20px;
                color: #666;
                margin-bottom: 15px;
            }
            .description {
                line-height: 1.6;
                color: #444;
                margin-top: 15px;
            }
            .tag {
                display: inline-block;
                padding: 4px 8px;
                background: #e1ecf4;
                color: #39739d;
                border-radius: 4px;
                font-size: 0.9em;
                margin-right: 8px;
            }
            .hidden {
                display: none;
            }
        </style>
    </head>
    <body>
        <h1>Remote Job Listings</h1>
        
        <div class="search-container">
            <input type="text" id="searchBox" class="search-box" 
                   placeholder="Search by title, company, or location..." onkeyup="searchJobs()">
            <div class="filters">
                <button class="filter-btn" onclick="filterBySource('all')">All Jobs</button>
                <button class="filter-btn" onclick="filterBySource('RemoteOK')">RemoteOK</button>
                <button class="filter-btn" onclick="filterBySource('WeWorkRemotely')">WeWorkRemotely</button>
            </div>
        </div>
        
        <div class="jobs-container">
    """
    
    # Add job cards
    for job in jobs:
        html_content += f"""
            <div class="job-card" data-source="{job['source']}">
                <h2 class="job-title">{job['Job Title']}</h2>
                <div class="job-meta">
                    <span>🏢 {job['Company']}</span>
                    <span>📍 {job['Location']}</span>
                    <span>📅 Posted: {job['Posted Date']}</span>
                </div>
                <div class="description">{job.get('Description', 'No description available')}</div>
                <div style="margin-top: 15px;">
                    <span class="tag">{job['Work Type']}</span>
                    <span class="tag">{job['source']}</span>
                    <a href="{job.get('url', '#')}" target="_blank" 
                       style="float: right; color: #1F4E78; text-decoration: none;">
                        Apply Now →
                    </a>
                </div>
            </div>
        """
    
    html_content += """
        </div>
        
        <script>
            function searchJobs() {
                const searchText = document.getElementById('searchBox').value.toLowerCase();
                const jobs = document.getElementsByClassName('job-card');
                
                Array.from(jobs).forEach(job => {
                    const text = job.textContent.toLowerCase();
                    job.classList.toggle('hidden', !text.includes(searchText));
                });
            }
            
            function filterBySource(source) {
                const jobs = document.getElementsByClassName('job-card');
                Array.from(jobs).forEach(job => {
                    if (source === 'all' || job.dataset.source === source) {
                        job.classList.remove('hidden');
                    } else {
                        job.classList.add('hidden');
                    }
                });
            }
        </script>
    </body>
    </html>
    """
    
    # Save the file
    output_file = os.path.join(output_dir, f'jobs_interactive_{timestamp}.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

def run_pipeline():
    """Run the ETL pipeline"""
    try:
        print("Starting job scraping pipeline...")
        
        # Extract and transform
        jobs = scrape_jobs()
        
        # Create output directory
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        # Save jobs as JSON in the output directory
        json_path = os.path.join(output_dir, 'jobs_data.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(jobs, f, indent=2)
        
        # Create display page
        from display import create_display_page
        create_display_page()
        
        print(f"Pipeline completed. Open output/display.html in a web server to view jobs")
        
    except Exception as e:
        print(f"Error in pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_pipeline()


