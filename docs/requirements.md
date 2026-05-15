# 要件定義書

## システム概要
ToDoを管理するWeb APIアプリケーションを作成する。

## 目的
タスクを登録・更新・削除できるようにする。

## 使用技術
- FastAPI
- MySQL
- Docker
- Poetry

## 機能要件

### ToDo一覧表示
登録済みToDoを一覧表示できる。

### ToDo追加
新しいToDoを登録できる。

### ToDo更新
登録済みToDoを編集できる。

### ToDo削除
登録済みToDoを削除できる。

### 完了状態切り替え
ToDoの完了状態を変更できる。

## 非機能要件

### API
REST API形式で実装する。

### DB
MySQLを使用する。

### 開発環境
Dockerで起動できるようにする。