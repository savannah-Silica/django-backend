# Django implementation of the community's backend.

## It implements a simple authentication using dj-rest-auth.
 Github authentication to be added later.<br>
 check the [api/urls.py](https://github.com/savannah-Silica/django-backend/blob/main/api/urls.py) files for authentication api path

## It has a custom user model.
  The custom user model is in the [api folder](https://github.com/savannah-Silica/django-backend/tree/main/api) , the user manager has not yet been implemented.

## Collaboration
Please contribute to the repo.<br>
> Create an issue before cloning and later on creating a pull request.<br>


## Set Up , Install & Run

### Clone Repository
```bash
git clone https://github.com/savannah-Silica/django-backend
```

### Create a Virtual Environment
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is [pipenv](https://pypi.org/project/pipenv/) or venv, which is included in [Python](https://www.python.org/).

With venv, you can create a virtual environment by typing this in the command prompt, remember to navigate to where you want to create your project.

Windows:
```bash
py -m venv myproject
```
Unix/MacOS:
```bash
python -m venv myproject
```

This will setup a virtual environment. Then you have to activate the environment, by typing this command:

Windows:
```bash
myproject\Scripts\activate.bat
```
Unix/MacOS:
```bash
source myproject/bin/activate
```
Once the environment is activated, you will see this result in the command prompt:

Windows:
```bash
(myproject) C:\Users\Your Name>
```
Unix/MacOS:
```bash
(myproject) ... $
```

> ***Note***: You must activate the virtual environment every time you open the command prompt to work on your project.

### Install dependencies
Ensure you have python running on your machine.

```bash
pip install -r requirements.txt
```

### Run
Open the terminal in the main directory and run
```bash
python manage.py runserver
```
