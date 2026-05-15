# LLD

## ToDo一覧取得API

### Endpoint
GET /todos

### Response

[
  {
    "id": 1,
    "title": "買い物",
    "completed": false
  }
]

### 処理概要
1. DBからToDo一覧取得
2. response返却

---

## ToDo追加API

### Endpoint
POST /todos

### Request

{
  "title": "買い物"
}

### Response

{
  "id": 1,
  "title": "買い物",
  "completed": false
}

### validation
- title必須
- 100文字以内

### 処理概要
1. request受け取り
2. validation
3. DB保存
4. response返却

---

## ToDo更新API

### Endpoint
PUT /todos/{id}

### Request

{
  "title": "勉強",
  "completed": true
}

### 処理概要
1. id検索
2. データ更新
3. response返却

---

## ToDo削除API

### Endpoint
DELETE /todos/{id}

### 処理概要
1. id検索
2. DB削除
3. response返却