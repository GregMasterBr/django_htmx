# Django com o HTMX

O projeto usa o [FastProjectTemplateDjango](https://github.com/GregMasterBr/FastProjectTemplateDjango) como base e HTMX para validar interação de dados do BD com a interface sem a necessidade do JS.

## Usage

Lets create your project, **you will clone this repo**, just follow the instructions bellow.

**NOTE**: You may need need to replace **_myproject_** placeholder to your project's name, it can break the installation.


### Linux and Mac
```
cd myproject
python3 -m venv .venv 
source .venv/bin/activate
pip install --upgrade pip
pip install django
```

### Windows
```
cd myproject
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install django
```

And then, proceed with the installation of the requirements. 

### [PROD]
```
pip install -r requirements.txt
```


### [DEV]
```
pip install -r requirements-dev.txt
```

## Tips
- python manage.py check  
- python manage.py migrate  
- python manage.py createsuperuser
- python manage.py runserver  
- python manage.py collectstatic  


