#!/bin/bash
# push the images to docker hub but only on the master branch
if [ "$TRAVIS_BRANCH" == "master" ]; then
  docker build -t dennistimmers/multi_api ./services/api
  docker build -t dennistimmers/multi_client ./services/client
  docker build -t dennistimmers/multi_nginx ./services/nginx
  docker build -t dennistimmers/multi_worker ./services/worker
  # log in to docker hub
  echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
  # push all the necessary images
  docker push dennistimmers/multi_api
  docker push dennistimmers/multi_client
  docker push dennistimmers/multi_nginx
  docker push dennistimmers/multi_worker
else
  echo "images not pushed because we are on branch "${TRAVIS_BRANCH}
fi