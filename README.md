# sistema-transmissao-imagens

# Sistema de Transmissão de Imagens

## Visão Geral

Este projeto consiste em um sistema de transmissão de imagens composto por três serviços principais: S1, S2 e S3. O serviço S1 é um serviço de inferência que utiliza FastAPI para fornecer um endpoint de detecção de pessoas em imagens usando os modelos YOLOv4 ou YOLOv8 com OpenCV. O processamento é feito obrigatoriamente usando CPU. Os serviços S2 e S3 são clientes que capturam frames de vídeo e os enviam para o serviço S1 para a contagem de pessoas, garantindo que cada pessoa no vídeo seja contada apenas uma vez.

## Estrutura do Projeto

sistema-transmissao-imagens/
├── S1/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── .env
│ └── app/
│ ├── main.py
│ ├── config.py
│ ├── services/
│ │ └── detection_service.py
│ ├── utils/
│ │ └── image_utils.py
│ └── logs/
├── S2/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app/
│ ├── main.py
│ └── init.py
├── S3/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── app/
│ ├── main.py
│ └── init.py
├── .github/
│ └── workflows/
│ └── ci-cd.yml
└── docker-compose.yml

markdown
Copiar código

## Requisitos do Sistema

- **Python 3.9**
- **Docker**
- **Docker Compose**
- **Git**

## Instruções de Configuração e Execução

### 1. Clonando o Repositório

Clone o repositório do projeto para o seu ambiente local:

```bash
git clone https://github.com/airtonmega/sistema-transmissao-imagens.git
cd sistema-transmissao-imagens
2. Configuração do Serviço de Inferência (S1)
2.1. Criação do Arquivo .env
Navegue até o diretório S1 e crie um arquivo .env com o seguinte conteúdo:

bash
Copiar código
cd S1
touch .env
nano .env
Adicione o seguinte conteúdo ao arquivo .env:

plaintext
Copiar código
MODEL_PATH=yolov4.weights
2.2. Construção e Execução do Docker
No diretório S1, construa a imagem Docker e execute o container:

bash
Copiar código
docker build -t s1-service .
docker run -p 8000:8000 --env-file .env s1-service
3. Configuração dos Clientes (S2 e S3)
3.1. Construção e Execução do Cliente S2
Navegue até o diretório S2, construa a imagem Docker e execute o container:

bash
Copiar código
cd ../S2
docker build -t s2-client .
docker run s2-client
3.2. Construção e Execução do Cliente S3
Navegue até o diretório S3, construa a imagem Docker e execute o container:

bash
Copiar código
cd ../S3
docker build -t s3-client .
docker run s3-client
4. Orquestração com Docker Compose
Docker Compose facilita a orquestração de múltiplos containers Docker.

4.1. Construção e Execução dos Serviços
No diretório raiz (sistema-transmissao-imagens), execute:

bash
Copiar código
docker-compose up --build
4.2. Execução em Segundo Plano (Detached Mode)
Para executar os serviços em segundo plano:

bash
Copiar código
docker-compose up -d --build
4.3. Parada dos Serviços
Para parar todos os serviços:

bash
Copiar código
docker-compose down
5. Configuração de CI/CD com GitHub Actions
Para configurar a integração e entrega contínua (CI/CD), adicione o arquivo de workflow no diretório .github/workflows.

5.1. Criação do Arquivo de Workflow
Navegue até o diretório .github/workflows e crie o arquivo ci-cd.yml:

bash
Copiar código
cd ../.github/workflows
touch ci-cd.yml
nano ci-cd.yml
Adicione o seguinte conteúdo:

yaml
Copiar código
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    services:
      docker:
        image: docker:19.03.12
        options: --privileged
        ports:
          - 2375:2375
        env:
          DOCKER_TLS_CERTDIR: ""

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          cd S1
          pip install -r requirements.txt

      - name: Run tests
        run: |
          cd S1
          python -m unittest discover -s app/tests

      - name: Build Docker images
        run: docker-compose build

      - name: Push Docker images
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker-compose push

  deploy:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Deploy to production
        run: |
          ssh user@your_server 'cd /path/to/project && docker-compose pull && docker-compose up -d'
5.2. Configuração de Segredos no GitHub
Adicione os segredos DOCKER_USERNAME e DOCKER_PASSWORD nas configurações do seu repositório no GitHub.