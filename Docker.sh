sudo systemctl start elasticsearch
sudo systemctl start kibana
sudo docker build -t seim .
docker run --network=host seim
sudo docker ps
