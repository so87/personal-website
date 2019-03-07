#!/bin/sh

if [ "$#" -ne 1 ]
then
  echo "Usage: ./$0 app-name"
  exit 1
fi
export MSYS_NO_PATHCONV=1; "docker.exe" "$@"
docker run --rm -v "$PWD"/build/code/:/code simonowens157/django:v1.0 python manage.py startapp $1