# Test Project

## Install

1. Apply environment variables:

```
cp example.env .env
```

2. Change a random string for `SECRET_KEY` in `.env`.

3. Install dependencies:

```
pip3 install requirements.txt
```

4. Up docker-compose, migrate database and create super user:

```
docker-compose up -d
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

5. Run the server:

```
python3 manage.py runserver
```
