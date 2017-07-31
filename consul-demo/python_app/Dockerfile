FROM python:3.4.3-onbuild

MAINTAINER Vijay Prabhakar, <vijayprabhakar.90@gmail.com>

EXPOSE 8080
COPY consul /bin/consul
RUN chmod 777 /bin/consul
RUN mkdir /etc/consul.d
RUN apt-get update
RUN apt-get install -y supervisor
COPY supervisord.conf /etc/supervisord.conf
RUN mkdir /opt/consuldata
CMD ["/usr/bin/supervisord"]
