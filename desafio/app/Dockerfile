FROM python:3.11.3-slim-bullseye


EXPOSE 5000/tcp


RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .


CMD ["flask", "run", "--host=0.0.0.0"]