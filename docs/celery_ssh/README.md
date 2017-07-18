### Cybercommons dockertask helper

[Dockertask](https://github.com/ouinformatics/dockertask) is a helper that allows you to ssh to docker host and run sister/brother containers. 



##### Requirements File for operation 

1. add dockertask to requirements.txt file in celery
2. Check/Generate ssh keys

	ssh-keygen # if keys are not present
	
	cat ~/.ssh/id_rsa.pub >> .ssh/authorized_keys

	chmod 600 .ssh/authorized_keys # set permission to read/write for owner only

3. Within cybercom_up check host_ip and docker_username. 

    * Change host_ip to hostname or ip address of base system
    * set docker_username current user

4. Add datamount to celery docker container within cybercom_up

    -v path_to_key/.ssh:/root/.ssh:z


