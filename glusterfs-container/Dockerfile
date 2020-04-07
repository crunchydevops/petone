FROM ubuntu:16.04

MAINTAINER hmeftah <admin@crunchydevops.com>
ENV ARCH "x86_64"
LABEL architecture="$ARCH" \
      name="glusterfs-ubuntu" \
      version="latest" \
      vendor="MIT" \
      summary="This image has a running glusterfs service" \
      io.k8s.display-name="Gluster server on ubuntu" \
      io.k8s.description="Gluster Image is based on Ubuntu Image which is a scalable network filesystem." \
      description="Gluster Image is based on ubuntu Image which is a scalable network filesystem. " \

RUN apt-get update -y && \
    apt-get install software-properties-common -y && \
    add-apt-repository ppa:gluster/glusterfs-3.10 -y && \
    apt-get update -y && \
    apt-get install glusterfs-server -y

