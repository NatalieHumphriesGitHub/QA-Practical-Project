export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml games-stack
docker service update --replicas 2 games-stack_front-end