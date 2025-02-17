from sqlalchemy import create_engine

def load_to_db(dataframe, db_url):
    """
    Load a DataFrame into the database.

    Args:
        dataframe (pd.DataFrame): Data to be inserted.
        db_url (str): Database connection URL.
    """
    from sqlalchemy import create_engine

    engine = create_engine(db_url)
    try:
        if dataframe.empty:
            print("No data to load into the database.")
            return

        # Log the data being inserted
        print(f"Inserting {len(dataframe)} rows into the database.")
        dataframe.to_sql('jobs', engine, if_exists='append', index=False)
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data into the database: {e}")
