#  Glusterfs
#  Get the latest tag:   git describe --tags `git rev-list --tags --max-count=1` | sort -V
#  Remove remote file in:  .gitignore git rm --cached `git ls-files -i -X .gitignore`
FROM fedora:rawhide

RUN dnf-y update && \
    dnf install -y wget git automake autoconf libtool flex bison openssl-devel  \
    libxml2-devel python-devel libaio-devel libibverbs-devel      \
    librdmacm-devel readline-devel lvm2-devel glib2-devel         \
    userspace-rcu-devel libcmocka-devel libacl-devel sqlite-devel \
    fuse-devel redhat-rpm-config rpcgen libtirpc-devel make libuuid-devel

# set systemd
RUN dnf -y install systemd && dnf clean all
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done);
rm -f /lib/systemd/system/multi-user.target.wants/*;
rm -f /etc/systemd/system/*.wants/*;
rm -f /lib/systemd/system/local-fs.target.wants/*;
rm -f /lib/systemd/system/sockets.target.wants/*udev*;
rm -f /lib/systemd/system/sockets.target.wants/*initctl*;
rm -f /lib/systemd/system/basic.target.wants/*;
rm -f /lib/systemd/system/anaconda.target.wants/*;

VOLUME ["/sys/fs/cgroup"]

RUN dnf -y install systemd && dnf clean all && \
    wget https://download.gluster.org/pub/gluster/glusterfs/LATEST/glusterfs-7.4.tar.gz && \
    tar -zxvf glusterfs-7.4.tar.gz && \
    cd glusterfs-7.4 && \
    ./autogen.sh && \
    ./configure --with-ipv6-default &&\
    make && \
    make install
#ENTRYPOINT ["/usr/local/sbin/glusterd"]
CMD ["/bin/bash"]

