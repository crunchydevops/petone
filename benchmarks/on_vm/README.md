# Benchmark on Centos virtual machines

## Set up the environment using Ansible

### Pre-requisite 
Download this repository
```shell script
 git clone https://github.com/crunchydevops/petone.git 
```
### Install glusterfs
The inventory file is defined as follows:   
```shell script
[leader]
leader1 ansible_host=51.254.227.43 ansible_ssh_user=centos ansible_ssh_pass=xxxx  ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
[slave]
slave1 ansible_host=51.68.28.141 ansible_ssh_user=centos ansible_ssh_pass=xxxx  ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
slave2 ansible_host=158.69.102.162 ansible_ssh_user=centos ansible_ssh_pass=xxxx  ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
```
### Ansible playbook
The Ansible playbook ```install_gluster_centos.yml``` is a straitforward deployment of glusterfs on 3 servers. 
A volume    
type as an example
```shell script
 ansible-playbook -i /home/hme/cent benchmarks/on_vm/install_gluster_centos.yml
```
## Install postgresql 12.2
Mount a directory as a glusterfs type 
```shell script
   sudo mount -t glusterfs leader01:/gv0 /mnt
```
Download postgresql repository and build the image 
```shell script
  git clone https://github.com/system-dev-formations/docker-postgres12.git
  cd docker-postgres12
  docker build -t pg122 .
```
Add a group and postgres user on the leader
```shell script
  sudo groupadd -g 70 postgres
  sudo adduser -g 70 -u 70 postgres
```
Start postgresql container connected to glusterfs volume  
```shell script
  docker run -d -it --name db  -p 25432:5432 --rm -v /tmp:/tmp -v /mnt:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password pg122
```
Create database ``` CREATE DATABASE tpc-test ```
Create all tables 
```shell script
  git clone   https://github.com/system-dev-formations/tpc-ds-postgresql.git 
  cd tpc-ds-postgresql
  cd tpcds-kit/tools
  apk add --no-cache make g++ gcc bison flex  
  make
  ./dsdgen -DIR /tmp -SCALE 10 -FORCE -VERBOSE
```


