# python-web-app
This is a basic web app which can be run using docker

To run this app using docker, please folow below steps.

# Below steps for mac
# 1. Install docker on mac by below command
brew install docker docker-compose docker-machine

# 2. Install colima: a container runtime manager that runs a Linux virtual machine on macOS and starts a Docker-compatible daemon (usually dockerd or containerd) inside that VM.
brew install colima

# 3. Start Colima
colima start

# 4. Build docker image
docker build -t my-flask-app .

# 5. Create and start running instance of docker image
docker run -d -p 8080:5000 --name flask-server my-flask-app

# 6. Open below webpage and you can see the content
http://10.0.0.133:8080/

# 7. Stop the instance
docker stop flask-server

# 8. Remove the instance
docker rm flask-server

# 9. Stop Colima to free memory
colima stop
