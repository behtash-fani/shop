FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY . /src

ADD requirements.txt /src
RUN pip install -U pip
RUN pip install -r requirements.txt


RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--chdir", "shop", "--bind", ":8000",  "config.wsgi:application"]