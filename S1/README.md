# Serviço de Inferência (S1)

## Visão Geral
Este serviço utiliza FastAPI para fornecer um endpoint de detecção de pessoas em imagens usando modelos YOLOv4 ou YOLOv8 com OpenCV. O processamento é feito usando CPU.

## Instalação

### Pré-requisitos
- Python 3.9
- Docker

### Instruções
1. Clone o repositório.
2. Navegue até o diretório `S1`.
3. Crie um arquivo `.env` baseado no exemplo fornecido.
4. Construa a imagem Docker:
   ```bash
   docker build -t s1-service .
