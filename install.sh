# !/bin/bash
echo "Create docker images"
cd db_sql
docker build -t postgr .
cd ..
mkdir dbpost
sudo chown -R $USER dbpost
docker build -t flask_api .
docker run \
  --name pst \
  -e POSTGRES_PASSWORD=test1234 \
  -e POSTGRES_USER=zvic \
  -d \
  -v ${PWD}/dbpost:/var/lib/postgresql/data:z \
  -p 5433:5432 postgr

docker run -p5000:5000 --net=host -d flask_api

docker ps
sleep 3
echo " when finished use < docker stop id> ;docker ps -a ; <docker rm -f > ;docker images; docker rmi "
