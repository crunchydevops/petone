# install glusterfs on 2 ubuntu instances 
## Requirements
2 ubuntu 16.04 Vms with an additional disk of 10Gb  

Change /etc/hosts on TEST1  
*VM  hostname= TEST1 (glusterfs1)*
```shell script
 127.0.0.1 glusterfs1
 158.69.102.162 glusterfs2
 51.68.5.207 gusterfs-client
````
Change /etc/hosts on TEST2  
*VM  hostname= TEST2 (glusterfs2)*
```shell script
 172.81.178.76 glusterfs1
 127.0.0.1 glusterfs2
 51.68.5.207 gusterfs-client
```
## Installation 
Note: Use locahost IP on each hostname to avoid NAT redirecting   
On both glusterfs1 and glusterfs2 , type that: 
```shell script
apt-get install software-properties-common -y
add-apt-repository ppa:gluster/glusterfs-3.10
apt-get update -y
apt-get install glusterfs-server -y
systemctl start glusterfs-server 
systemctl enable glusterfs-server
```
Add an extra SSD disk on both VM glusterfs1 and glusterfs2
Check 
```shell script
   fdisk -l 
```
Get the device name (here /dev/vdc) of this new device and make a partition 
```
   fdisk /dev/vdc 
   type n for new
   press enter to accept default values 
   and then type w 
```
Now you got a partition /dev/vdc1 of 10 Gb for example
```shell script
  mkfs.ext4 /dev/vdc1 
```
next, create a storage directory for glusterfs and mount the partition 
```shell script
   mkdir /glusterfs
   mount /dev/vdc1 /glusterfs
```
Create a persistent mount point by edting /etc/fstab 
```
   /dev/vdc1 /glusterfs ext4 defaults 0  0 
 ```

## Configuration GLusterfs Storage Pool

create a trusted storage pool on glusterfs1 
```shell script
 gluster peer probe glusterfs1
 gluster peer status
 gluster pool list
```
## Configure GlusterFS Volume
create a brick directory  with the name gvol0 in the mounted file system on both glusterfs instance. 
```shell script
    mkdir /glusterfs/gvol0
```
On glusterfs1 create a volume named gvol0 with 2 replicas by running the following commands 
```shell script
    gluster volume create gvol0 replica 2 glusterfs1:/glusterfs/gvol0 glusterfs2:/glusterfs/gvol0
    gluster volume start gvol0
    gluster volume info gvol0
```
## Configure GlusterFS Client



