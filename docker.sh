docker build . -t dab_spam
docker run --name dab_spammer dab_spam --restart=always -ti -d