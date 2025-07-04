# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto para dentro do container
COPY ./src ./src

# Define variável de ambiente para o diretório da app
ENV PYTHONPATH=/app/src

# Expõe a porta da API
EXPOSE 8002

# Comando padrão para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--app-dir", "src"]
