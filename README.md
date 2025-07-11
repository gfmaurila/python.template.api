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
    │   └── UserController.py
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

## 🧩 Eventos de Domínio

- `UserCreatedDomainEvent`
- `UserDeletedDomainEvent`
- `UserUpdatedDomainEvent`

Todos processados por seus respectivos handlers em `application/User/events`.


## 🔔 Mensageria: Redis & RabbitMQ Pub/Sub

Este projeto utiliza Redis e RabbitMQ como mecanismos de mensageria assíncrona para processamento de eventos de domínio.

### Redis

- Comunicação assíncrona via canais `user-created`, `user-updated`, `user-deleted`.
- Subscribers iniciados automaticamente no startup (`lifespan`).
- Dependência:
  ```bash
  pip install redis==5.0.3
  ```

### RabbitMQ

- Utiliza `fanout exchange` com o nome configurável via `.env` (`RABBITMQ_EXCHANGE`).
- Fila configurável via `.env` (`RABBITMQ_QUEUE`).
- Publisher e Subscriber implementados em `infrastructure/messaging`.
- http://localhost:15672/#/


### Kafka

- http://localhost:9100/

#### Exemplo `.env`:
```env
RABBITMQ_EXCHANGE=user-exchange
RABBITMQ_QUEUE=user-created-queue
```

#### Dependência:
```bash
pip install pika==1.3.2
```

