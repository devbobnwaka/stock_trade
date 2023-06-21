# stock_trade
A sample project.

# TO TEST THE APPLICATION

## Getting Started

1. Create virtual environment

```bash
#for windows
python -m venv .venv
```

2. Activate virtual environment
```bash
#for windows
.venv\Scripts\activate
```

3. Install all dependencies
```bash
#for windows
pip install -r requirements.txt
```

4. Run the Migrations
Current setup is for MONGO_DB, to use SQLite - uncomment the django.db.backends.sqlite3 Database setting and comment the MONGO_DB settings
```bash
#for windows
python manage.py makemigrations
python manage.py migrate
```

5. Seed initial data into your database using a custom management command
```bash
#for windows
python manage.py load_trader_data.py
python manage.py load_trade_data.py
```

6. Run the development server
```bash
#for windows
python manage.py runserver
```

## NOTE
Login for users range from user1- user10 and just one admin. You confirm this by viewing the database. 
e.g username - user1 
    password - admin12345678
for admin
    username - admin1
    password - admin12345678