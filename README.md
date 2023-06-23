# Fullstack Afiliados

This repository is the Backend side of Fullstack Afiliados test: https://lab.coodesh.com/devmateusalves/fullstack-afiliados
This project was made with Django REST Framework

### Run with Docker
 
- First of all, make sure to have Docker already installed
- Clone this project and then go to the repository directory
- Make a copy of `.env.example` file and rename to `.env`
- Change the `POSTGRES_NAME`, `POSTGRES_USER` and `POSTGRES_PASSWORD` variables with the values that you prefer of database configuration
- But make sure to copy and paste the same values on `docker-compose.yml` into the `db` container environment variables.
- Then run that to start the project:
```sh
sudo docker compose up``
```