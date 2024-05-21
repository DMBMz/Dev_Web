
WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


ENV FLASK_APP=app.py


EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0"]