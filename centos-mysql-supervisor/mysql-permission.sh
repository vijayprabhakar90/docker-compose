while [ -z "`netstat -tln | grep 3306`" ]; do
  echo 'Waiting for Mysql to start ...'
  sleep 1
done

mysql -e "grant all privileges on *.* to 'root'@'%' identified by ''"
mysql -e "grant all privileges on *.* to 'root'@'localhost' identified by ''"
mysql -e "FLUSH PRIVILEGES"
