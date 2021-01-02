host="pulsehack.samireland.com"

docker-compose build

docker-compose push

ssh -t $host "mkdir pulse"

scp production.yml $host:~/pulse/docker-compose.yml
scp secrets.env $host:~/pulse/

ssh $host "cd pulse && docker-compose pull"
ssh $host "cd pulse && docker-compose up --remove-orphans -d"
ssh $host "cd pulse && docker network connect bridge pulse_nginx_1 2>/dev/null"

ssh $host "rm -r pulse"