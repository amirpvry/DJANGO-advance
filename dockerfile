FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1


WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./core /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]