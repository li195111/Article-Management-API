FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD uwsgi --http=0.0.0.0:8000 --module=article_api.wsgi
