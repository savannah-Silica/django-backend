# Django implementation of the community's backend.

## It implements a simple authentication using dj-rest-auth.
 Github authentication to be added later.<br>
 check the api/urls.py files for authentication api path

## It has a custom user model.
  The custom user model is in the api folder , the user manager has not yet been implemented.

## Collaboration
Please contribute to the repo.<br>
Create an issue before cloning and later on creating a pull request.<br>


## Set Up , Install & Run

### Clone Repository
```bash
git clone https://github.com/savannah-Silica/django-backend
```

### Install dependencies
Ensure you have python running on your machine.<br>
It is recommended you activate a virtual environment using either pipenv or virtualenv<br>
Then
```bash
pip install -r requirements.txt
```

### Run
Open the terminal in the main directory and run
```bash
python manage.py runserver
```