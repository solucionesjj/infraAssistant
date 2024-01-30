FROM python
RUN apt-get -y update && apt-get install -y gunicorn git
WORKDIR /app
RUN git clone https://github.com/solucionesjj/infraAssistant.git
WORKDIR /app/infraAssistant/api
RUN pip install -r /app/infraAssistant/server/api/requirements.txt
CMD	["gunicorn","-w","4","api:app","--bind","0.0.0.0:80"]