FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /rms
COPY requirements.txt /rms/
RUN pip install -r requirements.txt
COPY . /rms/