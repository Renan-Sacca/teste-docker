FROM python:3.6.7
MAINTAINER RENAN SACCA
GIT CLONE SERVIDOR
WORKDIR /var/www
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "main.py"]