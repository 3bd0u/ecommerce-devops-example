#!/bin/bash
set -e
BUILD_NUMBER="$1"
IMAGE="3bd0u/ecommerce-app:${BUILD_NUMBER}"
WORKDIR="/home/ubuntu/ecommerce"

mkdir -p ${WORKDIR}
cd ${WORKDIR}

# pull and run docker
docker pull ${IMAGE}
docker stop ecommerce || true
docker rm ecommerce || true
docker run -d --name ecommerce -p 5000:5000 ${IMAGE}

echo "Deployed ${IMAGE}"
