#!/bin/sh
sudo docker run --rm   --name antony_db -e POSTGRES_USER=antony_db -e POSTGRES_PASSWORD=antony_db -d -p 5432:5432  -v $HOME/volume-antony_db/volumes/postgres:/var/lib/postgresql/data  postgres;
