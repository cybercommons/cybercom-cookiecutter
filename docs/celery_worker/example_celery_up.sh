
activate () {
  . /path/to/virtualenv/bin/activate 
}

activate;

#start celery wroker in background
# -l log level (info ,debug ,..) ; -Q name of Queue; -n name of celery worker 

nohup celery worker -l info -Q <queue_name> -n <work_node_name> &

