import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta


def clean_data(jobs):
    """
    Clean and standardize scraped job data.

    Args:
        jobs (list): List of dictionaries containing raw job data.

    Returns:
        pd.DataFrame: Cleaned and transformed job data.
    """
    # Validate input
    if not jobs or not isinstance(jobs, list):
        raise ValueError("Input 'jobs' must be a non-empty list of dictionaries.")

    # Convert list of jobs to DataFrame
    df = pd.DataFrame(jobs)

    # Ensure all expected columns are present
    expected_columns = ['Title', 'Company', 'Location', 'Summary', 'DatePosted']
    for col in expected_columns:
        if col not in df.columns:
            print(f"Missing column '{col}' detected. Adding it with default values.")
            df[col] = None  # Add missing columns with default values

    # Log the raw DataFrame
    print("Raw DataFrame before cleaning:")
    print(df.head())

    # Drop duplicate job postings based on key columns
    df.drop_duplicates(subset=['Title', 'Company', 'Location'], inplace=True)

    # Handle missing values by filling in defaults
    df['Title'] = df['Title'].fillna('Unknown Title')
    df['Company'] = df['Company'].fillna('Unknown Company')
    df['Location'] = df['Location'].fillna('Unknown Location')
    df['Summary'] = df['Summary'].fillna('No summary provided')

    # Standardize the DatePosted column
    df['DatePosted'] = df['DatePosted'].apply(lambda x: standardize_date(x) if pd.notnull(x) else '1970-01-01')

    # Log the cleaned DataFrame
    print("Cleaned DataFrame:")
    print(df.head())

    return df


def standardize_date(date_str):
    """
    Standardize the date string into a consistent format.

    Args:
        date_str (str): Raw date string from the scraper.

    Returns:
        str: Standardized date in YYYY-MM-DD format or a default placeholder for invalid dates.
    """
    today = datetime.date.today()

    try:
        if isinstance(date_str, str) and "day" in date_str:
            # Parse "X days ago"
            days_ago = int(date_str.split()[0])
            standardized_date = today - datetime.timedelta(days=days_ago)
        elif isinstance(date_str, str) and "30+" in date_str:
            # Parse "30+ days ago" as approximately 1 month ago
            standardized_date = today - relativedelta(months=1)
        elif isinstance(date_str, str):
            # Attempt to parse standard date strings
            standardized_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        else:
            # Default to today's date for unrecognized formats
            standardized_date = today
    except (ValueError, TypeError):
        # Handle invalid date strings by defaulting to today's date
        standardized_date = today

    return standardized_date.strftime('%Y-%m-%d')
