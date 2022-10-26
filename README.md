# Flask CRUD template

This project is a template for simple CRUD applications.

### Technologies:
* <img align="center" alt="ph-HTML" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"> HTML5
* <img align="center" alt="ph-Bootstrap" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg"> Bootstrap 5
* <img align="center" alt="ph-Python" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> Python 3.8+
* <img align="center" alt="ph-Flask" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg"> Flask & Jinja
* <img align="center" alt="ph-Flask" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg"> Flask SQLAlchemy
* <img align="center" alt="ph-Flask" height="25" width="25" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg"> SQLite3

## LICENSE

Free use. Go ahead and use it as often as you need or want.

## How to run it:

1 - Create the virtual environment for libraries:  
```
python3 -m venv venv
```

2 - Activate the virtual environment:  
Linux:   
```shell
. venv/bin/activate
```  
Windows:  
```shell
.\venv\Scripts\activate
```

3 - Install the complementary libraries:  
```shell
pip install -r requirements.txt
```

4 - Edit your `app.py`:
- Edit `app.secret_key` to your secret key
- Edit the `Your Table` class to create your own table
- Change route names and variables
- If you want you can change the style of the pages, just go to the bootstrap 5 documentation and choose what works best for you
- Go to the last line of `app.py` and change `debug=True` to `debug=False`

5 - Run it:  
```shell
python3 app.py
```