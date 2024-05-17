Serviço de Inferência de Detecção de Pessoas com YoloV4/V8
Visão Geral
Este projeto implementa um serviço de inferência utilizando FastAPI para detecção de pessoas em vídeos usando modelos YoloV4 ou YoloV8. O modelo é carregado utilizando OpenCV e o processamento é feito exclusivamente em CPU. Dois clientes (S2 e S3) enviam frames de vídeo para o serviço S1 para realizar a contagem de pessoas. Cada cliente tem um tracker dedicado para garantir que cada pessoa no vídeo seja contada apenas uma vez.

Funcionalidades
Detecção de Pessoas: Utiliza YoloV4 ou YoloV8 para detectar pessoas em cada frame.
Processamento via CPU: Todo o processamento é realizado usando a CPU.
Contagem de Pessoas: Cada pessoa é contada apenas uma vez, mesmo que apareça em múltiplos frames.
Serviço API: Utiliza FastAPI para receber frames e retornar a contagem de pessoas.
Requisitos
Python 3.8+
FastAPI
OpenCV
Numpy
Pydantic
Uvicorn