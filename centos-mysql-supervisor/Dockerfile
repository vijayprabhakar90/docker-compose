FROM aarongo/centos-ssh-supervisor

COPY consul /bin/consul
RUN chmod 777 /bin/consul
RUN mkdir /etc/consul.d
RUN echo '{"service": {"name": "mysqldb", "tags": ["db"], "port": 3306}}' |  tee /etc/consul.d/db_service.json
RUN yum clean all
RUN rpm --rebuilddb; yum install -y yum-plugin-ovl
RUN  yum install -y mysql-server mysql
COPY supervisord.conf /etc/supervisord.conf
RUN mkdir /opt/consuldata
EXPOSE 22 3306
COPY mysql-permission.sh /etc/mysql-permission.sh
CMD ["/usr/bin/supervisord"]
