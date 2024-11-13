# AITI-KACE Task Manager Assessment | November 13, 2024

This is a RESTful APIs backend that leverages on ***Django Rest Framework*** featuring a Postgresql database.

Features
- create and manage users
- create and manage tasks
- assign tasks to users (assignee gets an email notification)

---
## Table of content
- Getting Started
- Api Usage

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


## Api Usage
The Api can be explored in a browser via 'http://127.0.0.1:8000/'.
This is well documented and secured.
alternatively you can make manual requests to the server.
all api information can be found in the browser via the specified url

to make requests;
1. login
```
- make a GET request to http://127.0.0.1:8000/auth/login/
- extract the csrf token from the response headers and use that in subsequent post requests
- make a POST request to 'http://127.0.0.1:8000/auth/login' with params: 
    username: admin 
    password: <your password>
```
2. explore tasks
```
- get a list of tasks via GET 'http://127.0.0.1:8000/tasks'
- create a task via POST 'http://127.0.0.1:8000/tasks'
```
3. explore other endpoints in the browser since that is where the docs can be found