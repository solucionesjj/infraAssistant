FROM python
RUN apt-get -y update && apt-get install -y gunicorn git
WORKDIR /app
RUN git clone https://github.com/solucionesjj/infraAssistant.git
WORKDIR /app/infraAssistant/server/api
RUN pip install -r requirements.txt
CMD	["gunicorn","-w","4","-b","0.0.0.0:80","api.py"]