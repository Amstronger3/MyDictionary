FROM python:3
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /usr/src/MyDictionary
WORKDIR /usr/src/MyDictionary


COPY requirements.txt /usr/src/MyDictionary/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/MyDictionary/



