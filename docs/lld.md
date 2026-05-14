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

---

## ToDo追加API

### Endpoint
POST /todos

### Request
{
  "title": "買い物"
}