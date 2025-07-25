FROM python:3.11-slim

# Instala dependências do sistema e o driver ODBC 17 da Microsoft
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev \
    gcc \
    g++ \
    libssl-dev \
    freetds-dev \
    build-essential \
    libffi-dev \
    libsasl2-dev \
    libldap2-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY ./src ./src
COPY ./src/core/env/.env.docker .env

# Define variáveis de ambiente
ENV PYTHONPATH=/app/src
ENV ENVIRONMENT=docker

# Expõe a porta da API
EXPOSE 8002

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--app-dir", "src"]
