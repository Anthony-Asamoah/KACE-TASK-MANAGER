# AITI-KACE Task Manager Assessment | December 5, 2023

This is a RESTful APIs backend that leverages on ***Django Rest Framework*** featuring a Postgresql database.

---


## Getting Started


1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
# For Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```
Create a .env file in the root directory.
Copy over the variables from the 'example.env' file.
Provide the required values for each of the given keys.
```

5. Run database migrations:
```bash
cd app
python3 manage.py migrate
```
6. Create a superuser account and follow the prompts:
```bash
cd app
python3 manage.py createsuperuser --username admin --email admin@example.com
```

7. Run the application:

```bash
cd app
python3 manage.py runserver 8000
```

8. Access the API documentation:
```
Open http://127.0.0.1:8000 in your browser to view the available endpoints.
```