docker build . -t dab_spam --network=host
docker run --name dab_spammer dab_spam --restart=always -ti -d 