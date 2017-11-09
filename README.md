# dropsosvos

look at the .env file for api keys needed to run

1. `pipenv install`
2. `python manage.py migrate`
3. `python mange.py runserver 0.0.0.0:5000`

##Upload a file
`curl -F "file=@Pipfile" -F "name=name" -F "metadata=keep" localhost:5000/upload/`

##Download file
`curl localhost:5000/upload/:id:/`
