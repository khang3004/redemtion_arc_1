""" 1. SQL Lite
    2. Context Manager
    3. List of Tuples """

import sqlite3
# Dữ liệu giả lập (ID, Ngày, Doanh thu, Chi phí)
raw_data = [
    (1, "2023-01-01", 100.0, 80.0),
    (2, "2023-01-02", 150.0, 100.0),
    (3, "2023-01-03", 200.0, 120.0),
    (4, "2023-01-01", 50.0, 30.0) # Trùng ngày
]

#1. Connect to Database (Create tamporary file to fast test)
#Use with statement to connect to database (Auto close connection )

with sqlite3.connect(':memory:') as conn:
    cursor = conn.cursor()

    #2. Create Table (Standard SQL Commands)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        date TEXT,
        revenue REAL,
        cost REAL
    )
    """)

    #3. Bulk Insert Data (Standard SQL Commands)
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", raw_data)

    #4. Query Data (Compute PROFIT by day)
    print("-" * 3 + "Daily Profit Report" + "-" * 3)
    query = """
        SELECT 
            date,
            SUM(revenue - cost) as profit
        FROM sales
        GROUP BY date
    """

    cursor.execute(query)
    
    #5. Fetch Results
    results = cursor.fetchall()

    for row in results:
        print(f"Date: {row[0]} | Profit: {row[1]:.2f}")