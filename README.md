# Afiliados - Backend

This is a challenge by [Coodesh](https://lab.coodesh.com/devmateusalves/fullstack-afiliados).

### Technologies
- Python 3.10
- Docker 24.0.2
- Django REST Framework
- PostgreSQL

###  Presentation

Take a look at this video, there I explain about the challenge and I show my solution: [Click here](https://www.loom.com/embed/b6a79883a94e4674818e30c82b8d565d)

### Run with Docker
 
First of all, make sure to have Docker already installed. After you done that, go to the following steps:

- Clone this project and then go to the repository directory
- Make a copy of `.env.example` file and rename to `.env`
- Change the `POSTGRES_DB_NAME` and `POSTGRES_PASSWORD` variables with the values that you prefer of database configuration
  - Make sure to copy and paste the same values on `docker-compose.yml` into the `db` container environment variables.
- Then run that to start the project:
```sh
sudo docker compose up
```

### Create a super user
 
Create a new super user to authenticate on frontend and upload the sales file:
Open another Terminal tab, then enter on Docker container bash by running the following commands:
```sh
sudo docker exec -it django_afiliados bash
python manage.py createsuperuser
```
With the user created, do you can authenticate.

### Endpoints

The API endpoints were document with Swagger, and it can be accessed after run the project at http://localhost:8000/swagger/

### Running commands manually

If you want to run some specific command with `manage.py` script or install another lib with pip, then you need to enter the container bash terminal like abova. Run these commands for that:

- To list all containers run `sudo docker ps`
- Then identify the API of this project and run:  `sudo docker exec -it django_afiliados bash`
- Awesome, you are able to run some commands now.

Another option for you is start a new virtual environment manually to help in development. So run:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
In this case, change the virtual environment `POSTGRES_HOST` value at `.env` file from `db` to `localhost`

Then start the project with this:
```sh
cd src
python manage.py runserver 0.0.0.0:8000
```
