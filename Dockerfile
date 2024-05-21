FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=newsletter
ENV MYSQL_USER=flaskuser
ENV MYSQL_PASSWORD=flaskpassword

COPY init.sql /docker-entrypoint-initdb.d/
