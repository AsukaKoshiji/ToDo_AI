# ToDo_AI

AI-Native開発を意識して構築している ToDo API アプリケーション。

FastAPI をベースに、
Docker・Poetry・Pydantic・pytest を利用しながら、
設計駆動（HLD / LLD）で開発を進めています。

---

# Features

* ToDo一覧取得
* ToDo追加
* ToDo更新
* ToDo削除
* 完了状態管理
* バリデーション
* APIテスト
* Docker対応
* Poetryによる依存管理

---

# Tech Stack

* Python 3.14
* FastAPI
* Pydantic v2
* pytest
* Docker
* Poetry

---

# Architecture

```text
Client
  ↓
FastAPI Router
  ↓
CRUD Layer
  ↓
MySQL
```

---

# Directory Structure

```text
app/
├── api/
│   └── routes/
├── core/
├── crud/
├── models/
├── schemas/
└── main.py

tests/
docs/
```

---

# API Endpoints

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| GET    | /todos      | ToDo一覧取得    |
| POST   | /todos      | ToDo作成      |
| PUT    | /todos/{id} | ToDo更新      |
| DELETE | /todos/{id} | ToDo削除      |

---

# Local Development

## Install

```bash
poetry install
```

## Run

```bash
poetry run uvicorn app.main:app --reload
```

---

# Run Tests

```bash
poetry run pytest
```

---

# AI-Native Development

このプロジェクトでは AI を活用しながら開発を進めています。

活用内容:

* HLD / LLD 作成支援
* CRUDコード生成
* テストコード生成
* エラー解析
* リファクタリング支援

ただし、生成コードをそのまま使用するのではなく、
責務分離やデータフローを理解しながら改善を行っています。

---

# Documents

* docs/hld.md
* docs/lld.md
* docs/architecture.md

---

# Future Plans

* SQLAlchemy導入
* Repository Pattern改善
* Service Layer追加
* Alembic migration
* 認証機能
* AI機能追加

---

# Author

AsukaKoshiji
