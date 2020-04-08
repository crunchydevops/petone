#  Glusterfs
#  Get the latest tag --  git describe --tags `git rev-list --tags` | sort -V
#

FROM centos:7

RUN yum -y update
RUN yum -y install epel-release
RUN yum -y  install wget autoconf automake bison cmockery2-devel dos2unix flex   \
            fuse-devel glib2-devel libacl-devel libaio-devel libattr-devel    \
            libcurl-devel libibverbs-devel librdmacm-devel libtirpc-devel     \
            libtool libxml2-devel lvm2-devel make openssl-devel pkgconfig     \
            pyliblzma python-devel python-eventlet python-netifaces           \
            python-paste-deploy python-simplejson python-sphinx python-webob  \
            pyxattr readline-devel rpm-build sqlite-devel systemtap-sdt-devel tar userspace-rcu-devel

RUN  wget https://download.gluster.org/pub/gluster/glusterfs/LATEST/glusterfs-7.4.tar.gz && \
     tar -zxvf glusterfs-7.4.tar.gz && \
     cd glusterfs-7.4 && \
     ./autogen.sh && \
     ./configure --with-ipv6-default &&\
     make && \
     make install
ENTRYPOINT ["/usr/local/sbin/glusterd"]

