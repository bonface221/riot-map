## Riot-map
An application where users can:
*   Sign in (authentication)
*   View the Map for areas prone to riots
*   Add areas that have riots

## Getting Started

*   Fork the repository
*   git clone the project to your local machine
*   Set up a virtual environment in the project folder
```
$ pipenv shell
```

### Prerequisites

*get pipenv

```
Debian- sudo apt install pipenv
```
```
Windows- pip install --user pipenv
```
```
Locate python interpreter
$ pipenv --py
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python
```


*get all requirements in the Pipfile.lock

```
$ pipenv install
```

### Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.

Now run the following command

```
python3.9 manage.py runserver
```

And view the site at the port provided which is most likely 127.0.0.1:8000

## Running the tests

To run the automated tests for this system, run the following command

```
python3.9 manage.py test base

```

## Deployment

To deploy on heroku:
*   Have a Procfile in the project root;
*   Update requirements.txt file with all the requirements in the project root;
*   Have Gunicorn to requirements.txt;
*   Have runtime.txt to specify the correct Python version in the project root;
*   Ensure configuration whitenoise to serve static files.
*   Add a heroku remote by logging in
*   Configure all the settings in .env on heroku (set MODE to 'prod' on heroku)
*   git push to heroku
*   git push database and migrate to heroku server

## Built With

* Python Programming Language
* Django Web Framework

## Versioning

Find all the versions used in the pipfile.lock :


## Authors

- [Bonface Maina](https://github.com/bonface221)
- [Chanai Agwata](https://github.com/chanaiagwata)
- [Carolyne Maunda](https://github.com/bonface221)





## License

This project is licensed under the [MIT License](./LICENSE)

## Acknowledgments

* My Technical Mentors here at Moringa
* My fellow collaborators Chanai and carolyne