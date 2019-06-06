# Use binami nginix container for non-root container
# See more here : https://hub.docker.com/r/bitnami/nginx/
#       or here : https://github.com/bitnami/bitnami-docker-nginx.git

FROM docker.repo1.uhc.com/bitnami/nginx:1.14.1-ol-7-r6

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
COPY /dist /app
COPY nginx.conf /opt/bitnami/nginx/conf/nginx.conf

# Port 8080 is exposed already from base image
# Entrypoint/CMD is performed in base image as well

