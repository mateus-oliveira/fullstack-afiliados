# Afiliados - Backend

This is a challenge by [Coodesh](https://lab.coodesh.com/devmateusalves/fullstack-afiliados).

### Technologies
- Python 3.10
- Docker
- Django REST Framework
- PostgreSQL


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
Enter on Docker container bash and run the following commands:
```sh
sudo docker exec -it django_afiliados bash
python manage.py createsuperuser
```
With the user created, do you can authenticate.

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
