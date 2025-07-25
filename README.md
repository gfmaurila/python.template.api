
# 📘 Documentação Técnica - API Python com CQRS, DDD e FastAPI

## 📖 Visão Geral

Este projeto é um **template de arquitetura Python** com os padrões:

- ✅ DDD (Domain-Driven Design)
- ✅ CQRS (Command Query Responsibility Segregation)
- ✅ Vertical Slices Architecture
- ✅ FastAPI como framework web principal
- ✅ MongoDB, Redis, Kafka e RabbitMQ como integrações
- ✅ JWT para autenticação
- ✅ Log centralizado com MongoDB
- ✅ Validações, Responses padronizadas e mensagens traduzidas

---

## 🏗 Estrutura do Projeto

```bash
python.template.api/
└── src/
    ├── api/
    │   ├── AuthController.py
    │   ├── GithubController.py
    │   ├── LogController.py
    │   ├── MessageController.py
    │   ├── MessagingTestController.py
    │   ├── RedisPostController.py
    │   └── UserController.py
    ├── application/
    │   ├── Auth/         # Login, Esqueci e Redefinir senha
    │   ├── Github/       # GitHub Integration
    │   ├── Log/          # Gerenciamento de logs
    │   ├── Message/      # CRUD MongoDB
    │   └── User/         # Usuários com eventos e mensageria
    ├── core/
    │   ├── domain/
    │   ├── env/
    │   ├── response/
    │   ├── security/
    │   └── util/
    ├── domain/
    │   ├── entities/
    │   ├── enums/
    │   ├── interfaces/
    │   └── valueobjects/
    ├── infrastructure/
    │   ├── database/
    │   ├── integration/github/
    │   ├── logging/
    │   ├── messaging/User/Pub/
    │   ├── repositories/
    │   └── service/
    ├── worker/
    │   ├── User/
    │   └── main.py
    └── main.py
```

---

## 🚀 Como Executar o Projeto

### 🔧 Local com Python

```bash
pip install -r requirements.txt
cd src
uvicorn main:app --reload --port 8081
```

Acesse:
- Swagger: http://localhost:8081/docs
- Redoc: http://localhost:8081/redoc

### 🐳 Com Docker

```bash
docker-compose up --build
```

Ou apenas o worker:

```bash
docker-compose run --rm worker
```

---

## 📦 Endpoints Disponíveis

### 🔐 AuthController

| Método | Rota                      | Descrição                  |
|--------|---------------------------|----------------------------|
| POST   | /auth/login               | Login com e-mail e senha   |
| POST   | /auth/forgot-password     | Envia código por e-mail    |
| POST   | /auth/reset-password      | Redefine senha com código  |

### 👤 UserController

| Método | Rota           | Descrição         |
|--------|----------------|-------------------|
| GET    | /users         | Lista usuários    |
| GET    | /users/{id}    | Busca por ID      |
| POST   | /users         | Cria usuário      |
| PUT    | /users/{id}    | Atualiza usuário  |
| DELETE | /users/{id}    | Remove usuário    |

### 🧪 MessagingTestController

Testes manuais com mensageria:

| Método | Rota                    |
|--------|-------------------------|
| POST   | /test-messaging/redis   |
| POST   | /test-messaging/rabbitmq|
| POST   | /test-messaging/kafka   |

### 📫 RedisPostController

CRUD usando Redis:

| Método | Rota                     |
|--------|--------------------------|
| GET    | /redis-posts             |
| GET    | /redis-posts/{id}        |
| POST   | /redis-posts             |
| PUT    | /redis-posts/{id}        |
| DELETE | /redis-posts/{id}        |

### 📨 MessageController (MongoDB)

CRUD usando MongoDB:

| Método | Rota                 |
|--------|----------------------|
| GET    | /messages            |
| GET    | /messages/{id}       |
| POST   | /messages            |
| PUT    | /messages/{id}       |
| DELETE | /messages/{id}       |

### 🐱 GithubController

| Método | Rota                        | Descrição                      |
|--------|-----------------------------|--------------------------------|
| GET    | /github/user                | Perfil GitHub (live)           |
| GET    | /github/repos               | Repositórios GitHub (live)     |
| POST   | /github/store/profile       | Armazena perfil no Mongo       |
| POST   | /github/store/repos         | Armazena repositórios no Mongo |
| GET    | /github/stored/profile      | Recupera perfil do Mongo       |
| GET    | /github/stored/repos        | Recupera repositórios do Mongo |

### 📜 LogController

| Método | Rota              | Descrição                         |
|--------|-------------------|-----------------------------------|
| GET    | /logs/?limit=100  | Lista logs                        |
| DELETE | /logs/?older_than=YYYY-MM-DDTHH:mm:ss | Remove logs antigos |

---

## 🧩 Validações e Responses Padronizados

Todas as respostas seguem o formato:

```json
{
  "success": true,
  "status_code": 200,
  "success_message": "Mensagem",
  "errors": [],
  "data": {}
}
```

Erros de validação retornam:

```json
{
  "success": false,
  "status_code": 422,
  "errors": [
    { "message": "Campo é obrigatório." }
  ],
  "data": null
}
```

> 📍 Classes: `ApiResult`, `ExceptionHandler` em `core/response`

---

## 📫 Mensageria Assíncrona

Suporte a 3 mecanismos via Pub/Sub:

### Redis

- Canais: `user-created`, `user-updated`, `user-deleted`
- Publisher: `RedisPublisher.py`
- Subscriber: `RedisSubscriber.py`

### RabbitMQ

- Fanout exchange
- Publisher: `RabbitMQPublisher.py`
- Subscriber: `RabbitSubscriber.py`
- Painel: http://localhost:15672

### Kafka

- Tópico: `user-topic` (via .env)
- Publisher: `KafkaPublisher.py`
- Subscriber: `KafkaSubscriber.py`
- Painel UI opcional: http://localhost:9100

---

## 🧪 Testes via Postman

Importe o arquivo:

```
📁 API - Python.postman_collection.json
```

E utilize todos os endpoints documentados por coleção: Auth, Messaging, MongoDB, Redis, GitHub, Logs e User.

---

## 📫 Como me encontrar
- [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ)
- [![Linkedin Badge](https://img.shields.io/badge/-Guilherme_Figueiras_Maurila-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/guilherme-maurila)](https://www.linkedin.com/in/guilherme-maurila)
- [![Gmail Badge](https://img.shields.io/badge/-gfmaurila@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:gfmaurila@gmail.com)](mailto:gfmaurila@gmail.com)
- 📧 Email: gfmaurila@gmail.com
