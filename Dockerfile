FROM centos/python-38-centos7:20210726-fad62e9

USER root
RUN yum install -y python-devel mysql-devel MariaDB-devel
RUN yum install -y python3-devel mysql-devel
RUN yum install -y gcc
RUN yum install -y ncurses-devel
WORKDIR /usr/app/src
EXPOSE 3510
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
#Server will reload itself on file changes if in dev mode
ENV FLASK_DEBUG=1  

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

#CMD ["flask", "load-data"]
CMD ["flask", "run"]