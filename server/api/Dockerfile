FROM python
RUN apt-get -y update && apt-get -y upgrade
WORKDIR /app
RUN git clone https://github.com/solucionesjj/infraAssistant.git
WORKDIR /app/infraAssistant/server/api
RUN pip install -r requirements.txt
CMD	["uvicorn","api:app","--host","0.0.0.0","--port","80"]

modificar para trabajar con versiones específicas