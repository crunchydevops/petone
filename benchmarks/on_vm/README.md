# Benchmark on Virtual machines

## Set up the environment using Ansible 
### Install glusterfs
The inventory file is define as follows: 
```shell script
[master-leader]
 leader1 ansible_host=137.74.61.91 ansible_ssh_user=centos ansible_ssh_pass=xxxx  ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
   [slave]
 slave1 ansible_host=51.68.28.141 ansible_ssh_user=centos ansible_ssh_pass=xxxx  ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
   ```
