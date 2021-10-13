FROM python:3.9.7

COPY requirements.txt .

RUN pip install -r requirements.txt \
    && rm -r ~/.cache/pip

COPY bin/* .
