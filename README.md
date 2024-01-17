# my-ecommerce-app
An ecommerce app with DevOps

1. Clone the repo
2. Get the .env from the lead

http://localhost:8080/


<!--  -->
git clone https://github.com/anilkumaran/my-ecommerce-app.git
cd my-ecommerce-app/
ls
cat README.md

Test commit3



K8s - minikube https://medium.com/featurepreneur/deploying-a-flask-app-to-kubernetes-f05c93866aff
----- minikube
sudo apt update
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo apt install -y docker.io
sudo usermod -aG docker $USER && newgrp docker
minikube config set driver docker
minikube start --driver=docker


-- kubectl https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client


docker login
docker tag minikube-flask-app anil121786/minikube-flask-app
docker push anil121786/minikube-flask-app