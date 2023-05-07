FROM python:3.9

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /booking/docker/*.sh


CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]