#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime

# Initialize Faker instance
fake = Faker()

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}

# Categories for expense types
categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']

# Payment modes
payment_modes = ['Cash', 'Online']

# Function to create a table for January (or any specific month)
def create_month_table(cursor, month_name):
    table_name = month_name.upper()  
    
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS JAN2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name}2024 created or already exists.")

# Function to generate data for January
def generate_january_data():
    
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

    # Description based on category
    description = fake.sentence(nb_words=6)
   
    amount_paid = round(random.uniform(10, 200), 2)

    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    # Prepare data for January
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }

# Function to insert 12 rows of data into the JANUARY2024 table
def insert_january_data(cursor):
    table_name = "JAN2024"  
    
    insert_query = f"""
    INSERT INTO {table_name} (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Loop to generate and insert 12 rows of data for January
    for i in range(1, 13):  # 12 rows for 12 days of January (or just 12 rows)
        data = generate_january_data()

        transaction_date = f"2024-01-{i:02d}"  

        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print("12 rows of data inserted successfully into JANUARY2024.")

# Function to run the process
def run_january_expense_generation():
    conn = None
    cursor = None
    try:
        # Establish MySQL connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        create_month_table(cursor, "JAN")

        insert_january_data(cursor)

        # Commit the transaction
        conn.commit()
        print("All data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Run the process for January
run_january_expense_generation()


# In[110]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[105]:


import mysql.connector

try:
    # Establish the database connection
    conn = mysql.connector.connect(
        host='localhost',       
        user='root',       
        password='sara2310',   
        database='food'    
    )
    
    if conn.is_connected():
        print("Connected to the database")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM your_table")  # Replace 'your_table' with your actual table name
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")


# In[4]:


import mysql.connector
import random
from datetime import datetime
from faker import Faker

fake = Faker()

categories = ["Food", "Transportation", "Bills", "Entertainment", "Shopping", "Healthcare"]
payment_modes = ["Cash", "Online"]


def generate_transaction(date):
    category = random.choice(categories)  # Random category
    payment_mode = random.choice(payment_modes)  # Random payment mode
    description = fake.sentence(nb_words=6)  # Random description 
    amount_paid = round(random.uniform(10, 500), 2)  # Random amount 
    cashback = round(random.uniform(0, amount_paid * 0.1), 2)  # Random cashback
    
    return {
        'date': date.strftime('%Y-%m-%d'),
        'category': category,
        'payment_mode': payment_mode,
        'description': description,
        'amount_paid': amount_paid,
        'cashback': cashback
    }

# MySQL database connection details
try:
    mydb = mysql.connector.connect(
        host="localhost",  
        user="root",       
        password="sara2310",  
        database="food"    
    )
    
    cursor = mydb.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS FEB2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        category VARCHAR(50),
        payment_mode VARCHAR(50),
        description VARCHAR(255),
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """

    cursor.execute(create_table_query)

    # Insert query for the FEB2024 table
    insert_query = """
    INSERT INTO FEB2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    # Generate 12 random transactions for February 2024
    transactions_data = []
    for _ in range(12):  
        transaction_date = datetime(2024, 2, random.randint(1, 28))  # Random date in February 2024
        transaction = generate_transaction(transaction_date)
        transactions_data.append((
            transaction['date'],
            transaction['category'],
            transaction['payment_mode'],
            transaction['description'],
            transaction['amount_paid'],
            transaction['cashback']
        ))

    # Insert the generated 12 transactions into the FEB2024 table
    cursor.executemany(insert_query, transactions_data)

    mydb.commit()

    fetch_query = "SELECT * FROM FEBRUARY2024 LIMIT 5;"  # Displaying the first 5 records for brevity
    cursor.execute(fetch_query)
    results = cursor.fetchall()

    print("Inserted Transactions for FEB2024:")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if cursor:
        cursor.close()
    if mydb:
        mydb.close()

print("12 rows have been inserted into the FEB2024 table successfully.")


# In[5]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime

fake = Faker()

db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': 'sara2310', 
    'database': 'food',  
}

categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']


payment_modes = ['Cash', 'Online']

def create_march_table(cursor):
    table_name = 'MAR'  
    
    create_table_query = f"""
    CREATE TABLE MAR2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_march_data():
    
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

   
    description = fake.sentence(nb_words=6)

   
    amount_paid = round(random.uniform(10, 200), 2)

    
    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_march_table(cursor):
    table_name = 'MAR'

    
    insert_query = f"""
    INSERT INTO MAR2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Loop to insert 12 rows for the month of March (1 row for each day in March)
    for day in range(1, 13):  # Insert for 12 days of March
        data = generate_march_data()

        
        transaction_date = f"2024-03-{day:02d}"  # Format as '2024-03-01', '2024-03-02', ...

        
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


def run_march_expense_generation():
    try:
      
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        create_march_table(cursor)

        insert_data_into_march_table(cursor)

        conn.commit()
        print("All data for March inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:

        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_march_expense_generation()


# In[6]:


import mysql.connector
import random
from faker import Faker

db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310', 
    'database': 'food', 
}


categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']

payment_modes = ['Cash', 'Online']


fake = Faker()


def create_april_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS APR2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print("Table APRIL2024 created or already exists.")

def generate_april_data():
  
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)


    description = fake.sentence(nb_words=6)


    amount_paid = round(random.uniform(10, 200), 2)


    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0


    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_april_table(cursor):
    insert_query = """
    INSERT INTO APR2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    for _ in range(12):  # Insert for 12 random days in April
        data = generate_april_data()

        random_day = random.randint(1, 30)
        transaction_date = f"2024-04-{random_day:02d}" 

        # Insert data into the APRIL2024 table
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print("Data inserted successfully into APRIL2024.")

# Function to run the table creation and data insertion process
def run_create_april_table():
    try:
    
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()


        create_april_table(cursor)

        # Insert 12 rows of data into the APRIL2024 table
        insert_data_into_april_table(cursor)


        conn.commit()
        print("Table APRIL2024 and data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:

        if cursor:
            cursor.close()
        if conn:
            conn.close()

run_create_april_table()


# In[7]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime, date


fake = Faker()


categories = ["Food", "Transportation", "Bills", "Entertainment", "Shopping", "Healthcare"]
payment_modes = ["Cash", "Online"]


def generate_transaction(month, year):
   
    start_date = date(year, month, 1)  # May 1st

    end_date = date(year, month, 31)  # May 31st
    
    # Generate a random date between the start and end date
    transaction_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
    
    category = random.choice(categories)  # Random category
    payment_mode = random.choice(payment_modes)  # Random payment mode
    description = fake.sentence()  # Random description (sentence)
    amount_paid = round(random.uniform(10, 500), 2)  # Random amount 
    cashback = round(random.uniform(0, amount_paid * 0.1), 2)  # Random cashback 
    
    return (transaction_date, category, payment_mode, description, amount_paid, cashback)


def generate_may_transactions(num_records=12):
    transactions = [generate_transaction(5, 2024) for _ in range(num_records)]
    return transactions


def run_may_expense_generation():
    cursor = None
    conn = None
    
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="sara2310",  
            database="food"    
        )
        cursor = conn.cursor()

        # Create table for May 
        create_table_query = """
        CREATE TABLE IF NOT EXISTS MA2024(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(50),
            payment_mode VARCHAR(50),
            description VARCHAR(255),
            amount_paid DECIMAL(10, 2),
            cashback DECIMAL(10, 2)
        );
        """
        cursor.execute(create_table_query)

        # Generate May transactions
        transactions_data = generate_may_transactions()

       
        insert_query = """
        INSERT INTO MA2024 (date, category, payment_mode, description, amount_paid, cashback)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.executemany(insert_query, transactions_data)

     
        conn.commit()

        print(f"Successfully inserted {len(transactions_data)} records for May!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
     
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")

# Run the process for May
run_may_expense_generation()


# In[8]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime, date


fake = Faker()


categories = ["Food", "Transportation", "Bills", "Entertainment", "Shopping", "Healthcare"]
payment_modes = ["Cash", "Online"]


def generate_transaction(month, year):
    
    start_date = date(year, month, 1)  
    
    end_date = date(year, month, 30)  
    
    
    transaction_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
    
    category = random.choice(categories)  # Random category
    payment_mode = random.choice(payment_modes)  # Random payment mode
    description = fake.sentence()  # Random description 
    amount_paid = round(random.uniform(10, 500), 2)  # Random amount 
    cashback = round(random.uniform(0, amount_paid * 0.1), 2)  # Random cashback 
    
    return (transaction_date, category, payment_mode, description, amount_paid, cashback)


def generate_june_transactions(num_records=12):
    transactions = [generate_transaction(6, 2024) for _ in range(num_records)]
    return transactions


def run_june_expense_generation():
    cursor = None
    conn = None
    
    try:
        
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="sara2310",  
            database="food"    
        )
        cursor = conn.cursor()

        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS JUN2024(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(50),
            payment_mode VARCHAR(50),
            description VARCHAR(255),
            amount_paid DECIMAL(10, 2),
            cashback DECIMAL(10, 2)
        );
        """
        cursor.execute(create_table_query)

        
        transactions_data = generate_june_transactions()

       
        insert_query = """
        INSERT INTO JUN2024 (date, category, payment_mode, description, amount_paid, cashback)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.executemany(insert_query, transactions_data)

        
        conn.commit()

        print(f"Successfully inserted {len(transactions_data)} records for June!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")

# Run the process for June
run_june_expense_generation()


# In[9]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime, date


fake = Faker()


categories = ["Food", "Transportation", "Bills", "Entertainment", "Shopping", "Healthcare"]
payment_modes = ["Cash", "Online"]


def generate_transaction(month, year):
    
    start_date = date(year, month, 1)  # July 1st
    
    end_date = date(year, month, 31)  # July 31st
    
   
    transaction_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
    
    category = random.choice(categories)  # Random category
    payment_mode = random.choice(payment_modes)  # Random payment mode
    description = fake.sentence()  # Random description 
    amount_paid = round(random.uniform(10, 500), 2)  # Random amount between 
    cashback = round(random.uniform(0, amount_paid * 0.1), 2)  # Random cashback
    
    return (transaction_date, category, payment_mode, description, amount_paid, cashback)


def generate_july_transactions(num_records=12):
    transactions = [generate_transaction(7, 2024) for _ in range(num_records)]
    return transactions


def run_july_expense_generation():
    cursor = None
    conn = None
    
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="sara2310",  
            database="food"    
        )
        cursor = conn.cursor()

        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS JUL2024(
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(50),
            payment_mode VARCHAR(50),
            description VARCHAR(255),
            amount_paid DECIMAL(10, 2),
            cashback DECIMAL(10, 2)
        );
        """
        cursor.execute(create_table_query)

   
        transactions_data = generate_july_transactions()

        
        insert_query = """
        INSERT INTO JUL2024 (date, category, payment_mode, description, amount_paid, cashback)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cursor.executemany(insert_query, transactions_data)

       
        conn.commit()

        print(f"Successfully inserted {len(transactions_data)} records for July!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Database connection closed.")


run_july_expense_generation()


# In[10]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime


fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}

# Categories for expense types
categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']

# Payment modes
payment_modes = ['Cash', 'Online']

# Function to create the AUG table for August
def create_august_table(cursor):
    table_name = 'AUG' 
    
    create_table_query = f"""
    CREATE TABLE AUG2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_august_data():
    # Randomly select category and payment mode
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

    
    description = fake.sentence(nb_words=6)

    
    amount_paid = round(random.uniform(10, 200), 2)

    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    # Prepare data for August
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }

# Function to insert 12 rows of data into the AUG table
def insert_data_into_august_table(cursor):
    table_name = 'AUG'

    
    insert_query = f"""
    INSERT INTO AUG2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    
    for day in range(1, 13):  
        data = generate_august_data()

        
        transaction_date = f"2024-08-{day:02d}" 

        # Insert data into the AUG table
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


def run_august_expense_generation():
    try:
        # Establish MySQL connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

       
        create_august_table(cursor)

        
        insert_data_into_august_table(cursor)

        
        conn.commit()
        print("All data for August inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()

run_august_expense_generation()


# In[11]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime

fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}


categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']


payment_modes = ['Cash', 'Online']


def create_september_table(cursor):
    table_name = 'SEP'  
    
    create_table_query = f"""
    CREATE TABLE SEP2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_september_data():
   
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

    
    description = fake.sentence(nb_words=6)

    
    amount_paid = round(random.uniform(10, 200), 2)

    
    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_september_table(cursor):
    table_name = 'SEP'

    
    insert_query = f"""
    INSERT INTO SEP2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

   
    for day in range(1, 13):  
        data = generate_september_data()

        
        transaction_date = f"2024-09-{day:02d}"  

       
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


def run_september_expense_generation():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        create_september_table(cursor)

        
        insert_data_into_september_table(cursor)

        
        conn.commit()
        print("All data for September inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
       
        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_september_expense_generation()


# In[12]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime


fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}


categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']


payment_modes = ['Cash', 'Online']


def create_october_table(cursor):
    table_name = 'OCT'  
    
    create_table_query = f"""
    CREATE TABLE OCT2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_october_data():
    
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

    
    description = fake.sentence(nb_words=6)

    
    amount_paid = round(random.uniform(10, 200), 2)

    
    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_october_table(cursor):
    table_name = 'OCT'

    
    insert_query = f"""
    INSERT INTO OCT2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    
    for day in range(1, 13):  
        data = generate_october_data()

       
        transaction_date = f"2024-10-{day:02d}"  

        
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


def run_october_expense_generation():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

       
        create_october_table(cursor)

       
        insert_data_into_october_table(cursor)

      
        conn.commit()
        print("All data for October inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_october_expense_generation()


# In[13]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime


fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}


categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']


payment_modes = ['Cash', 'Online']


def create_november_table(cursor):
    table_name = 'NOV'  
    
    create_table_query = f"""
    CREATE TABLE NOV2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_november_data():
    
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

    
    description = fake.sentence(nb_words=6)

    
    amount_paid = round(random.uniform(10, 200), 2)

    
    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

    
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_november_table(cursor):
    table_name = 'NOV'

    
    insert_query = f"""
    INSERT INTO NOV2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

   
    for _ in range(12):  
        data = generate_november_data()

        
        random_day = random.randint(1, 30)
        transaction_date = f"2024-11-{random_day:02d}"  

        
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


def run_november_expense_generation():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        create_november_table(cursor)

        
        insert_data_into_november_table(cursor)

     
        conn.commit()
        print("All data for November inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
       
        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_november_expense_generation()


# In[14]:


import mysql.connector
from faker import Faker
import random
from datetime import datetime


fake = Faker()


db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}


categories = ['Food', 'Transportation', 'Bills', 'Entertainment', 'Healthcare', 'Shopping', 'Rent', 'Utilities', 'Education', 'Subscriptions', 'Gifts', 'Other']


payment_modes = ['Cash', 'Online']


def create_december_table(cursor):
    table_name = 'DEC'  
    
    create_table_query = f"""
    CREATE TABLE DEC2024 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print(f"Table {table_name} created or already exists.")


def generate_december_data():
    
    category = random.choice(categories)
    payment_mode = random.choice(payment_modes)

   
    description = fake.sentence(nb_words=6)

    
    amount_paid = round(random.uniform(10, 200), 2)

    
    cashback = round(random.uniform(0, 20), 2) if payment_mode == 'Online' else 0

  
    return {
        "Category": category,
        "Payment Mode": payment_mode,
        "Description": description,
        "Amount Paid": amount_paid,
        "Cashback": cashback
    }


def insert_data_into_december_table(cursor):
    table_name = 'DEC'

    #
    insert_query = f"""
    INSERT INTO DEC2024 (date, category, payment_mode, description, amount_paid, cashback)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    
    for _ in range(12):  
        data = generate_december_data()

        
        random_day = random.randint(1, 31)
        transaction_date = f"2024-12-{random_day:02d}"  

        
        cursor.execute(insert_query, (
            transaction_date,
            data['Category'],
            data['Payment Mode'],
            data['Description'],
            data['Amount Paid'],
            data['Cashback']
        ))

    print(f"Data inserted successfully into {table_name}.")


    
def run_december_expense_generation():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        create_december_table(cursor)

        
        insert_data_into_december_table(cursor)

       
        conn.commit()
        print("All data for December inserted successfully.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_december_expense_generation()


# In[23]:


import mysql.connector

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',  
    'password': 'sara2310',  
    'database': 'food',  
}

# Function to create the merged table (EXPENSES2024)
def create_expenses_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS EXPENSES24 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        category VARCHAR(50),
        payment_mode VARCHAR(20),
        description TEXT,
        amount_paid DECIMAL(10, 2),
        cashback DECIMAL(10, 2)
    );
    """
    cursor.execute(create_table_query)
    print("Table EXPENSES24 created or already exists.")


def merge_tables(cursor):
    
    month_tables = [
        "JAN2024", "FEB2024", "MAR2024", "APR2024", "MA2024", 
        "JUN2024", "JUL2024", "AUG2024", "SEP2024", "OCT2024", 
        "NOV2024", "DEC2024"
    ]
    
    
    for month_table in month_tables:
        try:
            
            insert_query = f"""
            INSERT INTO EXPENSES24 (date, category, payment_mode, description, amount_paid, cashback)
            SELECT date, category, payment_mode, description, amount_paid, cashback
            FROM {month_table};
            """
            cursor.execute(insert_query)
            print(f"Data from {month_table} inserted into EXPENSES24.")
        except mysql.connector.Error as err:
            print(f"Error inserting data from {month_table}: {err}")


def run_merge_process():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        create_expenses_table(cursor)

        
        merge_tables(cursor)

        
        conn.commit()
        print("All data merged successfully into EXPENSES24.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Ensure cursor and connection are closed properly
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Run the merge process
run_merge_process()


# In[24]:


import mysql.connector
import random

# MySQL connection details
db_config = {
    'host': 'localhost',  
    'user': 'root',      
    'password': 'sara2310',  
    'database': 'food', 
}

# Function to update descriptions based on categories
def update_all_categories_description(cursor):
    
    update_query = """
    UPDATE EXPENSES24
    SET description = CASE
        WHEN category = 'Food' THEN
            CASE 
                WHEN RAND() < 0.33 THEN 'Bought fresh groceries for the week'
                WHEN RAND() < 0.66 THEN 'Picked up some snacks and dinner ingredients'
                ELSE 'Purchased organic veggies and fruits for the kitchen'
            END
        WHEN category = 'Transportation' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid for my Uber ride to work'
                WHEN RAND() < 0.66 THEN 'Refueled the car after a long road trip'
                ELSE 'Bought a monthly metro card for commuting'
            END
        WHEN category = 'Bills' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid the electricity bill for the month'
                WHEN RAND() < 0.66 THEN 'Cleared the water and gas utility charges'
                ELSE 'Settled the internet and phone bill'
            END
        WHEN category = 'Entertainment' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Bought movie tickets for a night out'
                WHEN RAND() < 0.66 THEN 'Spent on a weekend concert experience'
                ELSE 'Enjoyed a fun amusement park day'
            END
        WHEN category = 'Healthcare' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid for a routine doctor''s checkup'
                WHEN RAND() < 0.66 THEN 'Got my flu vaccine and paid for the consultation'
                ELSE 'Purchased prescribed medicine from the pharmacy'
            END
        WHEN category = 'Shopping' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Bought a stylish dress for a dinner party'
                WHEN RAND() < 0.66 THEN 'Picked up some cozy sweaters for the winter'
                ELSE 'Bought a new set of books for my reading list'
            END
        WHEN category = 'Rent' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid rent for the month, looking forward to the cozy apartment'
                WHEN RAND() < 0.66 THEN 'Settled my monthly rent on time'
                ELSE 'Paid for my cozy home space this month'
            END
        WHEN category = 'Utilities' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid for the electricity and water services'
                WHEN RAND() < 0.66 THEN 'Cleared the utility bills for the house'
                ELSE 'Paid for heating and cooling charges for the month'
            END
        WHEN category = 'Education' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Paid for the latest online course on Python'
                WHEN RAND() < 0.66 THEN 'Bought new study materials for the semester'
                ELSE 'Settled tuition fees for the upcoming term'
            END
        WHEN category = 'Subscriptions' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Renewed my monthly Netflix subscription'
                WHEN RAND() < 0.66 THEN 'Paid for an Audible audiobook subscription'
                ELSE 'Bought a monthly Spotify premium subscription'
            END
        WHEN category = 'Gifts' THEN
            CASE
                WHEN RAND() < 0.33 THEN 'Bought a lovely gift for my friend''s birthday'
                WHEN RAND() < 0.66 THEN 'Surprised my partner with a thoughtful anniversary gift'
                ELSE 'Picked up a set of handmade candles as a gift'
            END
        ELSE 'Spent on miscellaneous items that came up this month'
    END;
    """
    
    cursor.execute(update_query)
    print("Descriptions updated for all categories.")


def run_update_process():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        update_all_categories_description(cursor)

        conn.commit()
        print("Descriptions updated successfully for all categories.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()  
    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()


run_update_process()


# In[25]:


import mysql.connector
import pandas as pd

# MySQL connection details
db_config = {
    'host': 'localhost',  
    'user': 'root',       
    'password': 'sara2310', 
    'database': 'food',  
}


def fetch_and_save_to_csv():
    try:
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        
        query = "SELECT * FROM expenses24"
        cursor.execute(query)

       
        rows = cursor.fetchall()

        
        columns = [column[0] for column in cursor.description]

     
        df = pd.DataFrame(rows, columns=columns)

        
        file_path = 'expenses24.csv'

        
        df.to_csv(file_path, index=False)

        print(f"CSV file created and saved to {file_path}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
       
        if cursor:
            cursor.close()
        if conn:
            conn.close()


fetch_and_save_to_csv()


# In[26]:


import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv('expenses24.csv')

print(df.head())


# In[27]:


print(df.isnull().sum())

print(df.dtypes)

print(df.describe())


# In[28]:


print(df.columns)


# In[29]:


# Remove leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Verify column names again
print(df.columns)


# In[30]:


# Remove leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Verify column names again
print(df.columns)


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'date': ['2024-01-15', '2024-02-20', '2024-01-10', '2024-02-25', '2024-03-10'],
    'amount_paid': [100, 200, 150, 250, 300]
})


df['date'] = pd.to_datetime(df['date'])


df['Month'] = df['date'].dt.month_name()


monthly_spending = df.groupby('Month')['amount_paid'].sum()


ordered_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthly_spending = monthly_spending.reindex(ordered_months)


plt.figure(figsize=(10, 6))
monthly_spending.plot(kind='line', marker='o', color='green')
plt.title('Monthly Spending Trends in 2024')
plt.xlabel('Month')
plt.ylabel('Total Amount Paid')
plt.xticks(rotation=45)  
plt.grid(True)
plt.show()


# In[33]:


plt.figure(figsize=(10, 6))
monthly_spending.plot(kind='bar', color='orange')
plt.title('Monthly Spending by Category in 2024')
plt.xlabel('Month')
plt.ylabel('Total Amount Paid')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[65]:



df['date'] = pd.to_datetime(df['date'])  
daily_spending = df.groupby('date')['amount_paid'].sum()

plt.figure(figsize=(10, 6))
daily_spending.plot(kind='line', marker='o', color='blue')
plt.title('Daily Spending Trends in 2024')
plt.xlabel('Date')
plt.ylabel('Total Amount Paid')
plt.grid(True)
plt.show()


# In[38]:



df['weekday'] = df['date'].dt.day_name()


weekday_spending = df.groupby('weekday')['amount_paid'].sum()

ordered_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_spending = weekday_spending.reindex(ordered_weekdays)


plt.figure(figsize=(10, 6))
weekday_spending.plot(kind='bar', color='purple')
plt.title('Total Spending by Weekday in 2024')
plt.xlabel('Weekday')
plt.ylabel('Total Amount Paid')
plt.xticks(rotation=45)
plt.show()


# In[55]:



df['Month'] = pd.to_datetime(df['date']).dt.to_period('M')


monthly_expenses = df.groupby('Month')['amount_paid'].sum()


monthly_expenses_sorted = monthly_expenses.sort_values(ascending=False)


plt.figure(figsize=(10, 6))
monthly_expenses_sorted.plot(kind='bar', color='orange')
plt.title('Monthly Expenses in 2024')
plt.xlabel('Month')
plt.ylabel('Total Amount Paid')
plt.xticks(rotation=45)
plt.show()


# In[97]:


# Plotting a scatter plot of transaction date vs amount paid
plt.figure(figsize=(10, 6))
plt.scatter(df['date'], df['amount_paid'], alpha=0.6, color='purple')
plt.title('Scatter Plot: Date vs Amount Paid', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Amount Paid', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[125]:


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Title of the app
st.title("Expense Report Presentation")

# Section 1: Introduction
st.header("Introduction")
st.write(
    """
    Welcome to the expense report presentation. In this app, we will visualize and analyze the
    expenses over a period of time. We will explore various charts and data insights.
    """
)

# Section 2: Data Visualization
st.header("Expense Over Time")

# Create a sample DataFrame with data
dates = pd.date_range(start="2024-01-01", periods=12, freq="M")
expenses = np.random.randint(1000, 5000, size=12)

df = pd.DataFrame({"Date": dates, "Amount Paid": expenses})

# Plotting the expense data (Line Plot)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["Date"], df["Amount Paid"], marker='o', color='b', linestyle='-', linewidth=2)
ax.set_title("Monthly Expenses (Line Plot)")
ax.set_xlabel("Date")
ax.set_ylabel("Amount Paid")
st.pyplot(fig)

# Section 3: Additional Visualizations
st.header("Additional Expense Analysis")

# 1. Bar Plot of Expenses (Total per Month)
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(df["Date"].dt.month_name(), df["Amount Paid"], color='green')
ax2.set_title("Total Expenses per Month (Bar Plot)")
ax2.set_xlabel("Month")
ax2.set_ylabel("Amount Paid")
st.pyplot(fig2)

# 2. Pie Chart of Expenses
fig3, ax3 = plt.subplots(figsize=(8, 8))
ax3.pie(df["Amount Paid"], labels=df["Date"].dt.month_name(), autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax3.set_title("Expense Distribution by Month (Pie Chart)")
st.pyplot(fig3)

# 3. Scatter Plot to show relationship between months and expenses
fig4, ax4 = plt.subplots(figsize=(10, 6))
ax4.scatter(df["Date"], df["Amount Paid"], color='red', s=100)
ax4.set_title("Expense Distribution Over Time (Scatter Plot)")
ax4.set_xlabel("Date")
ax4.set_ylabel("Amount Paid")
st.pyplot(fig4)

# 4. Histogram to show distribution of expenses
fig5, ax5 = plt.subplots(figsize=(10, 6))
ax5.hist(df["Amount Paid"], bins=10, color='orange', edgecolor='black')
ax5.set_title("Expense Distribution (Histogram)")
ax5.set_xlabel("Amount Paid")
ax5.set_ylabel("Frequency")
st.pyplot(fig5)

# Section 4: Summary and Insights
st.header("Insights")
st.write(
    """
    From the charts and tables above, we can conclude the following insights:

    1. **Expense Trend Over Time (Line Chart)**:
       - The **line chart** clearly shows how expenses change over time, with some months displaying sharp increases or decreases.
       - There may be seasonal fluctuations in spending, with higher expenses in certain months (e.g., festive seasons or end-of-year months) and lower expenses in others.

    2. **Expenses Per Month (Bar Plot)**:
       - The **bar plot** offers a comparison of expenses across individual months.
       - We can see that some months have higher expenses than others, which could be due to special events or increased spending during holidays.
       - Identifying the months with the highest expenses can help in planning budgets more effectively and understanding specific periods of overspending.

    3. **Expense Distribution by Month (Pie Chart)**:
       - The **pie chart** shows the percentage share of each month's expenses in the overall annual expenditure.
       - This is particularly useful to understand which months contribute the most to the total annual expenditure. For example, a few months might account for the majority of spending.
       - The chart can help highlight months with abnormally high expenses relative to the rest.

    4. **Expense Distribution Over Time (Scatter Plot)**:
       - The **scatter plot** shows the distribution of expenses across time, with each data point representing a particular month's expenses.
       - The plot can reveal if there are any outliers or periods where expenses were particularly high or low compared to others.
       - A spread of points indicates variability in the spending pattern, which could suggest inconsistent or irregular expense behavior.

    5. **Expense Frequency (Histogram)**:
       - The **histogram** displays how frequently different levels of expenses occur.
       - If most of the expenses fall within a narrow range, it indicates that your spending is fairly consistent. However, a wider spread of values might suggest fluctuating expenses over the months.
       - This could also help identify whether large, irregular expenses are common or if the majority of expenses are more predictable.

    Based on these insights:
    - **Seasonal Trends**: Certain periods, like holidays, might cause a spike in spending, which can be identified through the line and bar charts.
    - **Potential for Budgeting**: By looking at the months with the highest expenses, you could plan better budgets and reduce spending during specific periods.
    - **Distribution Analysis**: The pie chart and histogram offer an understanding of how expenses are distributed, helping to detect patterns of overspending or areas where cuts can be made.

    In conclusion, these charts collectively provide a clear overview of the spending habits, highlighting areas for further analysis and potential savings.
    """
)

# Display the DataFrame as a table for detailed insights
st.subheader("Expense Data Table")
st.write(df)


# Footer: Contact Information
st.markdown("""
    **Contact Information:**
    - Saravana
    - 9943969109
""")

