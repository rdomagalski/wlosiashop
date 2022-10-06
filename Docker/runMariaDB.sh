docker run -d \
  --name=mariadb \
  -e PUID=1000 \
  -e PGID=1000 \
  -e MYSQL_ROOT_PASSWORD="changemeordie" \
  -e TZ=Europe/Warsaw \
  -p 3306:3306 \
  -v /var/dockerstorage/mariadb-owncloud:/config \
  --restart unless-stopped \
  linuxserver/mariadb