# Python image
FROM python:3.10

# Virtual environment
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# work directory
WORKDIR /app

# Requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# Listen 8000 port
EXPOSE 8000

# migrate and runserver
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
