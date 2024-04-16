docker rm $(docker ps -aq)
docker image rm dab_spam
docker build . -t dab_spam --network=host
docker run dab_spam --name dab_spammer --restart=always -ti -d 