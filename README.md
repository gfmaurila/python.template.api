# 📘 Documentação Técnica - Estrutura CQRS/DDD em Python

## 📖 Visão Geral

Este projeto segue os princípios de **DDD (Domain-Driven Design)** com o padrão **CQRS (Command Query Responsibility Segregation)** e estrutura em **Vertical Slices**, utilizando `FastAPI` e nomeando os arquivos, métodos e entidades no **padrão C#**.

A arquitetura favorece **separação de responsabilidades**, escalabilidade e **organização por funcionalidade** em vez de camadas tradicionais.

---

## 🏗 Estrutura Atual do Projeto

```bash
python.template.api/
└── src/
    ├── main.py
    ├── api/
    │   ├── UserController.py
    │   └── MessagingTestController.py
    ├── application/
    │   └── User/
    │       ├── commands/
    │       │   ├── CreateUserCommand.py
    │       │   ├── UpdateUserCommand.py
    │       │   ├── DeleteUserCommand.py
    │       │   ├── Create/
    │       │   │   └── Events/
    │       │   │       └── Domain/Messaging/{Kafka,RabbitMQ,Redis}/...
    │       │   ├── Delete/
    │       │   │   └── Events/
    │       │   │       └── Domain/Messaging/{Kafka,RabbitMQ,Redis}/...
    │       │   ├── Update/
    │       │   │   └── Events/
    │       │   │       └── Domain/Messaging/{Kafka,RabbitMQ,Redis}/...
    │       ├── dtos/
    │       │   └── UserDto.py
    │       ├── events/
    │       │   ├── UserCreatedDomainEventHandler.py
    │       │   ├── UserDeletedDomainEventHandler.py
    │       │   └── UserUpdatedDomainEventHandler.py
    │       └── queries/
    │           ├── GetUserByIdQuery.py
    │           └── GetAllUsersQuery.py
    ├── core/
    │   ├── domain/
    │   │   ├── entities/
    │   │   │   └── BaseEntity.py
    │   │   ├── interfaces/
    │   │   │   └── IAggregateRoot.py
    │   │   └── events/
    │   │       └── Event.py
    │   ├── Config.py
    │   ├── Openapi.py
    │   └── Security.py
    ├── domain/
    │   ├── entities/
    │   │   └── User/
    │   │       ├── UserEntity.py
    │   │       └── events/
    │   │           ├── UserCreatedDomainEvent.py
    │   │           ├── UserDeletedDomainEvent.py
    │   │           ├── UserUpdatedDomainEvent.py
    │   │           └── Messaging/{Kafka,RabbitMQ,Redis}/...
    │   ├── enums/
    │   │   ├── EGender.py
    │   │   └── ENotificationType.py
    │   ├── interfaces/
    │   │   └── IUserRepository.py
    │   └── valueobjects/
    │       ├── Email.py
    │       ├── PhoneNumber.py
    │       └── ValueObject.py
    ├── infrastructure/
    │   ├── messaging/
    │   │   ├── RedisSubscriber.py
    │   │   ├── RabbitSubscriber.py
    │   │   ├── KafkaSubscriber.py
    │   │   └── User/
    │   │       └── Pub/
    │   │           ├── RedisPublisher.py
    │   │           ├── RabbitMQPublisher.py
    │   │           └── KafkaPublisher.py
    │   └── repositories/
    │       └── UserRepositoryMemory.py
```

---

## 🔄 Equivalência com .NET

| C# (.NET)                      | Python (FastAPI)                                           |
|-------------------------------|------------------------------------------------------------|
| `Startup.cs`, `Program.cs`    | `main.py`                                                  |
| `Controllers`                 | `api/UserController.py`                                    |
| `DTOs`                        | `application/User/dtos/UserDto.py`                         |
| `Commands`                    | `application/User/commands/*.py`                           |
| `Queries`                     | `application/User/queries/*.py`                            |
| `Entities`                    | `domain/entities/User/UserEntity.py`                       |
| `Events`                      | `domain/entities/User/events/User*DomainEvent.py`          |
| `Event Handlers`              | `application/User/events/User*DomainEventHandler.py`       |
| `Interfaces` (IRepository)    | `domain/interfaces/IUserRepository.py`                     |
| `Repositories` (impl.)        | `infrastructure/repositories/UserRepositoryMemory.py`      |

---

## 📦 Dependências Iniciais

```bash
pip install fastapi uvicorn pydantic
```

---

## 🚀 Como Executar

**1.** Acesse a pasta `src`:

```bash
cd src
```

**2.** Execute o servidor FastAPI:

```bash
uvicorn main:app --reload --port 8081
```

**3.** Acesse no navegador:

- Swagger: [http://localhost:8081/docs](http://localhost:8081/docs)
- Redoc: [http://localhost:8081/redoc](http://localhost:8081/redoc)

---

## 🛠 Comandos Disponíveis

| Operação        | Método | Rota             | Payload (exemplo)                          |
|-----------------|--------|------------------|--------------------------------------------|
| Create User     | POST   | `/users`         | `{ "Name": "Guilherme", "Email": "..." }`  |
| Get All Users   | GET    | `/users`         | —                                          |
| Get User By Id  | GET    | `/users/{id}`    | —                                          |
| Update User     | PUT    | `/users/{id}`    | `{ "Name": "Novo Nome", "Email": "..." }` |
| Delete User     | DELETE | `/users/{id}`    | —                                          |

---

✅ Validação de Dados e Retornos Padronizados

A API implementa um **tratamento global de erros** com tradução das mensagens do `Pydantic` para **português** e retorno padronizado com a classe `ApiResult`.

🛡 Validação de senha

A senha deve atender aos seguintes critérios:

- Pelo menos **1 caractere especial**
- Pelo menos **1 letra maiúscula**
- Pelo menos **1 letra minúscula**
- Pelo menos **1 número**
- ❌ Não pode conter **números em sequência crescente** (ex: 123)
- ❌ Não pode conter **letras em sequência crescente** (ex: abc)

📄 Exemplo de erro traduzido

```json
{
  "success": false,
  "status_code": 422,
  "errors": [
    {
      "message": "O valor deve conter pelo menos 8 caracteres."
    }
  ],
  "data": null
}
```

📘 Retorno padronizado

Todas as respostas seguem o padrão:

```json
{
  "success": true,
  "success_message": "Usuário criado com sucesso!",
  "status_code": 200,
  "errors": [],
  "data": {
    "id": 123
  }
}
```

- Implementado por meio das classes `ApiResult` e `ErrorDetail` (`core/response/ApiResult.py`)
- Erros de validação são interceptados por `ExceptionHandler.py`
- Baseado no estilo de resposta das APIs REST em C#


---

## 🧩 Eventos de Domínio

- `UserCreatedDomainEvent`
- `UserDeletedDomainEvent`
- `UserUpdatedDomainEvent`

Todos processados por seus respectivos handlers em `application/User/commands/*/Events/Domain`.

---

## 🔔 Mensageria: Redis, RabbitMQ & Kafka Pub/Sub

Este projeto utiliza Redis, RabbitMQ e Kafka como mecanismos de mensageria assíncrona para processamento de eventos.

### Redis

- Comunicação assíncrona via canais `user-created`, `user-updated`, `user-deleted`.
- Subscribers iniciados automaticamente no `lifespan` (`RedisSubscriber`).
- Publisher em: `infrastructure/messaging/User/Pub/RedisPublisher.py`
- Subscriber em: `infrastructure/messaging/RedisSubscriber.py`
- Dependência:
  ```bash
  pip install redis==5.0.3
  ```

### RabbitMQ

- Utiliza `fanout exchange` com nome configurável via `.env`.
- Publisher em: `infrastructure/messaging/User/Pub/RabbitMQPublisher.py`
- Subscriber em: `infrastructure/messaging/RabbitSubscriber.py`
- http://localhost:15672/#/
- Dependência:
  ```bash
  pip install pika==1.3.2
  ```

### Kafka

- Tópico configurável via `.env`.
- Publisher em: `infrastructure/messaging/User/Pub/KafkaPublisher.py`
- Subscriber em: `infrastructure/messaging/KafkaSubscriber.py`
- UI para teste: http://localhost:9100/
- Dependência:
  ```bash
  pip install kafka-python
  ```

#### Exemplo de configuração no `.env.development`:
```env
# RabbitMQ
RABBITMQ_EXCHANGE=user-exchange
RABBITMQ_QUEUE=user-created-queue

# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:29092
KAFKA_TOPIC=user-topic
KAFKA_GROUP_ID=user-group
```

---

## 🧪 Controller de Testes de Mensageria

O arquivo `MessagingTestController.py` expõe endpoints de teste para envio de mensagens via cada mecanismo:

| Tipo       | Método | Rota                       |
|------------|--------|----------------------------|
| Redis      | POST   | `/test-messaging/redis`    |
| RabbitMQ   | POST   | `/test-messaging/rabbitmq` |
| Kafka      | POST   | `/test-messaging/kafka`    |

Cada rota envia um payload de exemplo para o canal correspondente.


---

## ⚙️ Serviço Worker (Mensageria)

Este projeto possui um serviço de **Worker assíncrono** separado da API, responsável por escutar mensagens de eventos nas filas do Redis, RabbitMQ e Kafka.

O arquivo principal do worker é:

```bash
src/worker/main.py
```

Este worker roda os `Subscribers` que escutam os canais/filas configuradas para:

- Redis: `user-created`, `user-deleted`, `user-updated`
- RabbitMQ: fila configurável via `.env`
- Kafka: tópico configurável via `.env`

### 🐳 Executando com Docker

Você pode subir a API e o Worker juntos com:

```bash
docker-compose up --build
```

Ou apenas o worker:

```bash
docker-compose run --rm worker
```

O comando que o container `worker` executa é:

```dockerfile
command: python src/worker/main.py
```

---

## 🧠 Observação

A API e o Worker compartilham o mesmo `Dockerfile` e `requirements.txt`, garantindo ambiente unificado e reduzindo duplicidade de configuração.

---


## Autor

- Guilherme Figueiras Maurila
 
## 📫 Como me encontrar
- [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ)
- [![Linkedin Badge](https://img.shields.io/badge/-Guilherme_Figueiras_Maurila-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/guilherme-maurila)](https://www.linkedin.com/in/guilherme-maurila)
- [![Gmail Badge](https://img.shields.io/badge/-gfmaurila@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:gfmaurila@gmail.com)](mailto:gfmaurila@gmail.com)
- 📧 Email: gfmaurila@gmail.com

