# HLD

## 使用技術
- FastAPI
- MySQL
- Docker
- Poetry

## ディレクトリ構成
- api
- schemas
- models

## API
- GET /todos
- POST /todos
- PUT /todos/{id}
- DELETE /todos/{id}

## D# HLD

## システム概要
ToDoを管理するFastAPIアプリ

## 使用技術
- FastAPI
- MySQL
- Docker
- Poetry

## ディレクトリ構成
api: APIルーティング
schemas: リクエスト/レスポンス
models: DBモデル
crud: DB操作

## API一覧
- GET /todos
- POST /todos
- PUT /todos/{id}
- DELETE /todos/{id}

## DB設計
Todo
- id
- title
- completed

## 処理概要
Client → Router → CRUD → DB
Todo
- id
- title
- completed