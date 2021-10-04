FROM python:latest

RUN pip install -U pip

COPY ./requirements.txt .
RUN  pip install -r requirements.txt

COPY . /src/

WORKDIR /src


COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]