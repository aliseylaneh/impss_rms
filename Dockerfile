FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip setuptools wheel
WORKDIR /rms
COPY requirements.txt /rms/
RUN pip install -r requirements.txt
COPY . /rms/