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
The Ansible playbook ```install_gluster_centos.yml``` is a straitforward deployment of glusterfs on 3 servers: two sets on the   
same subnet in Roubaix, the third one is available on a fast internet at Montreal. It is defined a disaster recovery host.    
type as an example
```shell script
 ansible-playbook -i /home/hme/cent benchmarks/on_vm/install_gluster_centos.yml
```


