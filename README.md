Aplicação em Python utilizando Flask para apresentar uma página HTML com meu currículo.
A aplicação é containerizada e é possível executá-la em um container Docker.  

Estes foram os passos seguidos para a sua construção:


Para criar o aplicativo:

1. Instalei o Flask usando o comando "pip install Flask" no terminal.

2. Criei um diretório para o projeto e naveguei até ele no terminal.

3. Dentro do diretório, criei um arquivo chamado "app.py" e escrevi o código do aplicativo Flask.

4. Criei um arquivo chamado "Dockerfile" e escrevi o código Dockerfile.

5. Criei um arquivo chamado "requirements.txt" e escrevi "Flask==2.0.1".

10. Compilei a imagem Docker usando o comando "docker build -t flask-resume-app" no terminal.

11. Executei o container Docker usando o comando "docker run -p 8080:80 flask-resume-app" no terminal.

12. Acessei "http://localhost:8080" para ver o resultado.


Para publicar no Dockerhub, inseri no terminal "docker login", 
"docker build -t usernameisrequiredd/flask-resume-app:latest .",
e "docker push usernameisrequiredd/flask-resume-app:latest".
Depois disso acessei "hub.docker.com" para certificar que havia sido publicado.
Link: https://hub.docker.com/repository/docker/usernameisrequiredd/flask-resume-app/general
