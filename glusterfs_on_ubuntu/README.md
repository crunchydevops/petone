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
Get the device name of this new device 
```

`






