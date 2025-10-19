import pandas as pd
import sqlite3
import os
import sys

# --- Configuration ---
CSV_PATH = 'questions.csv'
DB_PATH = 'database/questions.db'
TABLE_NAME = 'questions'
# ---------------------

def load_csv_to_sqlite(csv_path=CSV_PATH, db_path=DB_PATH, table_name=TABLE_NAME):
    """
    Reads questions from a CSV file, standardizes column names, fixes semicolon separators, and loads data.
    """
    print(f"Starting data load from {csv_path}...")
    
    try:
        import pandas as pd
    except ImportError:
        print("❌ Error: The 'pandas' library is required to run this script.")
        sys.exit(1)

    if not os.path.exists(csv_path):
        print(f"❌ Error: CSV file not found at {csv_path}.")
        sys.exit(1)

    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)
        
    try:
        # NOTE: Your uploaded CSV data uses SEMICOLONS (;) as separators within the options field.
        # We must tell pandas to treat the data as comma-separated but replace semicolons with commas 
        # for the 'options' column later.
        df = pd.read_csv(csv_path)

        # --- CRITICAL COLUMN STANDARDIZATION ---
        
        rename_map = {}
        
        # 1. Standardize 'question_text'
        if 'question' in df.columns: rename_map['question'] = 'question_text'
        elif 'Question' in df.columns: rename_map['Question'] = 'question_text'
            
        # 2. Rename 'answer' to 'correct_answer'
        if 'answer' in df.columns: rename_map['answer'] = 'correct_answer'
            
        df.rename(columns=rename_map, inplace=True)
        if rename_map:
            print(f"INFO: Renamed columns: {rename_map}")
            
        # 3. Ensure 'id' column exists
        if 'id' not in df.columns:
            df.insert(0, 'id', range(1, 1 + len(df)))
            print("INFO: Added 'id' column automatically.")
            
        # 4. Consolidate options and fix SEMICOLON separation
        
        # Check if the required 'options' column is present
        if 'options' in df.columns:
            # Fix: Replace semicolon separators in the 'options' column with commas
            df['options'] = df['options'].astype(str).str.replace(';', ',')
            print("INFO: Replaced semicolons (;) with commas (,) in the 'options' column.")
            
        # If the CSV uses separate columns (option_a, option_b, etc.)
        option_cols = [col for col in df.columns if col.startswith('option_')]
        if option_cols and 'options' not in df.columns:
            df['options'] = df[option_cols].fillna('').astype(str).agg(','.join, axis=1)
            df['options'] = df['options'].apply(lambda x: ','.join([i for i in x.split(',') if i.strip() != '']))
            print(f"INFO: Consolidated columns {option_cols} into new 'options' column.")
            df.drop(columns=option_cols, inplace=True)
        elif 'options' not in df.columns:
            df['options'] = ''
            print("WARNING: 'options' column is missing; created an empty column for text answers.")

        # --- END CRITICAL COLUMN STANDARDIZATION ---

        # Connect to SQLite database and replace table
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        
        print(f"\n✅ Success! Loaded {len(df)} questions into {db_path}.")

    except Exception as e:
        print(f"❌ A critical error occurred during CSV to SQLite conversion: {e}")
        sys.exit(1)

if __name__ == '__main__':
    load_csv_to_sqlite()
