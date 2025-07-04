# 📘 Documentação Geral - Projeto python.template.api em Python

## 📖 Visão Geral
O **Projeto python.template.api** consiste em um conjunto de APIs desenvolvidas com **FastAPI (Python 3.11+)**, estruturadas de forma modular para atender diferentes domínios de negócio. A comunicação entre os serviços ocorre por **mensageria assíncrona** (RabbitMQ/Kafka) e integração via `.env`, com infraestrutura completa em **Docker Compose**.

---

## 🏗 Arquitetura e Tecnologias Utilizadas

- **FastAPI + Pydantic** → Framework moderno e performático para APIs REST
- **Uvicorn** → ASGI server rápido e leve
- **MongoDB** → Banco NoSQL
- **SQL Server** → Banco relacional via Docker
- **Redis** → Cache distribuído
- **RabbitMQ / Kafka** → Mensageria para eventos e integração assíncrona
- **Docker & Docker Compose** → Conteinerização da infraestrutura
- **Swagger/OpenAPI** → Documentação automática
- **JWT** → Autenticação baseada em token

---

## 📁 Estrutura do Projeto

```bash
📂 python.template.api
├── 📂 Common/
│   ├── domain/
│   │   ├── BaseEntity.py
│   │   ├── IEntity.py
│   │   ├── events/Event.py
│   │   └── ValueObjects/
│   │       ├── ValueObject.py
│   │       ├── Email.py
│   │       └── PhoneNumber.py
│   └── enums/
│       ├── EGender.py
│       └── ENotificationType.py
├── 📂 Extensions/
│   └── Settings.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
```

---

## 📌 Descrição dos Componentes

### 🔐 Autenticação JWT
- Tokens gerados e verificados via `Settings.py`
- Proteção de rotas com dependências (`Depends(verify_jwt)`)

### 🧱 Domínio
- **ValueObjects** como `Email`, `PhoneNumber`
- **BaseEntity** com rastreamento (`DtInsert`, `DtUpdate`, etc.)
- **Eventos de domínio** com classe base `Event`

### 📊 Infraestrutura via Docker Compose

Serviços incluídos:
- SQL Server (`localhost:1433`)
- Redis (`localhost:6379`)
- MongoDB (`localhost:27017`)
- RabbitMQ (`localhost:15672`)
- Kafka + UI (`localhost:9100`)
- API Python (`localhost:8000`)

---

## 🚀 Executando o Projeto

```bash
docker compose down
docker compose up -d --build
```

Documentação da API:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Mensageria e Streaming

### RabbitMQ
- Interface: [http://localhost:15672](http://localhost:15672)
- Usuário: guest / Senha: guest

### Kafka
- Interface: [http://localhost:9100](http://localhost:9100)

---

## 📚 Banco de Dados

### SQL Server
- Host: `localhost`
- Usuário: `sa`
- Senha: `@Poc2Minimal@Api`

### MongoDB
- Host: `localhost`
- Database: `API_Exemple`

---

## 🧪 Testes
Você pode utilizar **pytest** para testes unitários e de integração no projeto Python.

---

## 👨‍💻 Autor

- **Guilherme Figueiras Maurila**

[![LinkedIn](https://img.shields.io/badge/-Guilherme_Maurila-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/guilherme-maurila)  
[![Gmail](https://img.shields.io/badge/-gfmaurila@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)](mailto:gfmaurila@gmail.com)  
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ)