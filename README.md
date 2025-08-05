```sh
source venv/bin/activate
```

```sh
curl -X POST "http://127.0.0.1:8000/generate" \
 -H "Content-Type: application/json" \
 -d '{"service": "gpt", "keyword": "오메가3"}'
 ```