FROM ubuntu

ENV FLASK_APP=app
EXPOSE 8000

COPY . .

RUN apt-get update && apt-get install -y python3 python3-venv python3-dev pkg-config default-libmysqlclient-dev build-essential
RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

CMD [".venv/bin/python", "app.py"]