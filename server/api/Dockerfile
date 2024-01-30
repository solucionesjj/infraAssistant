FROM python
RUN apt-get -y update && apt-get install -y gunicorn git
WORKDIR /app
RUN git clone https://github.com/solucionesjj/infraAssistant.git
WORKDIR /app/infraAssistant/server/api
RUN cat requirements.txt
RUN pip install -r requirements.txt
CMD	["uvicorn","api:app","--host","0.0.0.0","--port","80"]