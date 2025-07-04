# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte para o container
COPY . .

# Expõe a porta da API
EXPOSE 8000

# Comando padrão para iniciar o servidor
CMD ["uvicorn", "Main:app", "--host", "0.0.0.0", "--port", "8000"]
