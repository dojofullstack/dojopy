#!/bin/sh
sudo docker run --rm  --name JaimeDB -e POSTGRES_USER=jaime_db -e POSTGRES_PASSWORD=jaime_db -d -p 5431:5432  -v $HOME/volume-dojopy/volumes-jaime/postgres:/var/lib/postgresql/data postgres;
