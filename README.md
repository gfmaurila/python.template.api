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
    │   ├── dtos/
    │   │   └── UserDto.py
    │   ├── commands/
    │   │   ├── CreateUserCommand.py
    │   │   ├── UpdateUserCommand.py
    │   │   └── DeleteUserCommand.py
    │   └── queries/
    │       ├── GetUserByIdQuery.py
    │       └── GetAllUsersQuery.py
    ├── domain/
    │   ├── entities/
    │   │   └── User.py
    │   └── interfaces/
    │       └── IUserRepository.py
    └── infrastructure/
        └── repositories/
            └── UserRepositoryMemory.py
```

---

## 🔄 Equivalência com .NET

| C# (.NET)                      | Python (FastAPI)                         |
|-------------------------------|------------------------------------------|
| `Startup.cs`, `Program.cs`    | `main.py`                                |
| `Controllers`                 | `api/UserController.py`                  |
| `DTOs`                        | `application/dtos/UserDto.py`            |
| `Commands`                    | `application/commands/*.py`              |
| `Queries`                     | `application/queries/*.py`               |
| `Entities`                    | `domain/entities/*.py`                   |
| `Interfaces` (IRepository)    | `domain/interfaces/IUserRepository.py`   |
| `Repositories` (impl.)        | `infrastructure/repositories/*.py`       |

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

| Operação       | Método | Rota             | Payload (exemplo)                    |
|----------------|--------|------------------|--------------------------------------|
| Create User    | POST   | `/users`         | `{ "Name": "Guilherme", "Email": "..." }` |
| Get All Users  | GET    | `/users`         | —                                    |
| Get User By Id | GET    | `/users/{id}`    | —                                    |
| Update User    | PUT    | `/users/{id}`    | `{ "Name": "Novo Nome", "Email": "..." }` |
| Delete User    | DELETE | `/users/{id}`    | —                                    |

---

## 👨‍💻 Autor

**Guilherme Figueiras Maurila**  
[LinkedIn](https://www.linkedin.com/in/guilherme-maurila) • [YouTube](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ) • [Email](mailto:gfmaurila@gmail.com)
