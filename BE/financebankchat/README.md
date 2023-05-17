# README #
```bash
# Virtual environment
$ # Install virtualenv
$ pip install virtualenv
$ # Step 1: initialize virtual environment in folder named 'venv'
$ python -m virtualenv venv
$ # Windows: access virtual env
$ # cmd
$ venv\\Scripts\\activate.bat
$ # powershell
$ venv\\Scripts\\activate.ps1
$ # Linux: access virtual env
$ source venv/bin/activate
```

```bash
# Install package in venv
$ pip install -r requirements.txt
```

```bash
# migration
$ python manage makemigrations
$ python manage migrate
$ python manage collectstatic
# load sample data
& python3 -m manage loaddata financebankchat/fixture/stock.json
& python3 -m manage loaddata financebankchat/fixture/provider.json

```

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
# runserver
$ python manage.py runserver
```
### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact