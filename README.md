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

## .env
Store sensitive data in the .env file<br>

The .env file will be hidden automatically from the repo because it should contain sensitive information of the project such as the SECRET_KEY.
After cloning the repo go on and follow these steps:
<ul>
 <li>In the root directory of this Project, (<em>Inside the folder named <strong>community</strong></em>), create a file called <strong>.env</strong></li>
 <li>After creating the file, write the following lines:</li>
 
 ```bash
1. SECRET_KEY=your_secret_key
2. DEBUG=True
```
<li>This should do the trick, try running the server to check for any errors after creating your .env file</li>

 ```bash
python manage.py runserver
```
</ul>

> ***Note*** <strong>Generating Your Own SECRET_KEY</strong>
<p>To generate a new key, use the get_random_secret_key() function present in the django.core.management.utils that returns a 50 character string of random characters.
You can open the python shell by typing this command first to execute the get_random_secret_key</p>

 ```bash
python manage.py shell
```
After opening shell, execute the following codes to generate your random key

 ```bash
 >>>from django.core.management.utils import get_random_secret_key
 >>>print(get_random_secret_key())
```
<p>Copy the key generated and place it in your SECRET_KEY variable in the .env file. <em><strong>There should be no whitespace around the variable</strong></em></p>
