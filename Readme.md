# Instalition
```bash
git clone https://github.com/abubakirovxolmirza/Queue
```
```bash
docker build -t queue:1.0 .
docker run -p 1212:8000 queue:1.0
```


1. .../api/add - bu yerga o'z navbatingizni olasiz

Barcha xonalar ro’yxatini olish uchun uchun `GET` :`…/api/rooms`

```json

{
  "direction": "cards"
}
```

2. ...api/adds - barcha navbatlarni ro'yhatini olish uchun.
3. .../api/recipient/cards - Carta hizmatlari uchun barcha navbatlarni ko'rish.

4. .../api/recipient/cards/{queue_number} - Carta xizmatlari uchun ma'lum bir navbatni o'chirish uchun .
```json

{
  "message": "end"
}
```