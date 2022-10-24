FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY proj/ /code/
RUN pip install uwsgi
RUN pip install -r requirements.txt
