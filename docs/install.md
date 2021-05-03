# インストール

## 開発環境構築

### Requirements

- Docker

### 手順

```$ clone [this repository]```
```$ cd [this repository]```
```$ docker-compose build```
```$ docker-compose run --rm app make setup```
```$ cp .env.sample .env```

## 起動

```$ docker-compose up make run```

### アクセス

GET http://localhost:5000/api/v1/health
