# 📘 Documentação Técnica - Estrutura CQRS/DDD Python

## 📖 Visão Geral

Este projeto segue uma arquitetura **DDD (Domain-Driven Design)** com separação por **Vertical Slices** e uso do padrão **CQRS (Command Query Responsibility Segregation)**, inspirado em práticas utilizadas no desenvolvimento com C# e .NET.

O framework principal utilizado é o **FastAPI**, por sua leveza, tipagem forte com Pydantic, e excelente performance para APIs RESTful.

---

## 🏗 Estrutura Sugerida

```bash
python.template.api/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   └── exceptions.py
│   ├── shared/
│   │   ├── base_model.py
│   │   ├── base_entity.py
│   │   └── repository.py
│   ├── modules/
│   │   ├── exemple/
│   │   │   ├── application/
│   │   │   │   ├── commands/
│   │   │   │   │   └── create_exemple.py
│   │   │   │   ├── queries/
│   │   │   │   │   └── get_exemple.py
│   │   │   ├── domain/
│   │   │   │   ├── entities/
│   │   │   │   │   └── exemple.py
│   │   │   │   ├── value_objects/
│   │   │   │   └── enums/
│   │   │   ├── infrastructure/
│   │   │   │   └── repository.py
│   │   │   ├── presentation/
│   │   │   │   └── exemple_controller.py
│   │   │   └── tests/
│   │   │       └── test_exemple.py
│   │   └── __init__.py
│   └── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .env
```

---

## 🔄 Equivalência com .NET

| C# (.NET)                      | Python (FastAPI)                         |
|-------------------------------|------------------------------------------|
| `Startup.cs`, `Program.cs`    | `main.py`                                |
| `Controllers`                 | `presentation/*.py`                      |
| `DTOs`                        | `application/commands/*.py`              |
| `Services`                    | `application/services/*.py` (opcional)   |
| `Entities`                    | `domain/entities/*.py`                   |
| `Repositories` (interface)    | `shared/repository.py`                   |
| `Repositories` (implementação)| `infrastructure/repository.py`           |
| `MediatR`                     | Command/Query Handler + Dispatcher       |

---

## 📦 Dependências Iniciais

```bash
pip install fastapi uvicorn pydantic[dotenv] python-multipart
```

---

## 🚀 Execução

```bash
uvicorn app.main:app --reload
```

Documentação Swagger:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👨‍💻 Autor

**Guilherme Figueiras Maurila**  
[LinkedIn](https://www.linkedin.com/in/guilherme-maurila) • [YouTube](https://www.youtube.com/channel/UCjy19AugQHIhyE0Nv558jcQ) • [Email](mailto:gfmaurila@gmail.com)