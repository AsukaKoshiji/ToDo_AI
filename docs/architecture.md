# アーキテクチャ設計

## システム構成

Client
↓
FastAPI
↓
MySQL

## ディレクトリ構成

app/
├── api/
├── schemas/
├── models/
├── crud/
├── db/
└── main.py

## 責務

api :
ルーティングを担当

schema :
request/response定義

models：
DBモデル定義

crud :
DB操作枠

## 使用技術

ーFastAPI
ーMySQL
ーDocker
ーPoetry
ーSQLAlchemy
ーAlembic