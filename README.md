<h1>Тестовое задание</h1>

**Порядок запуска программы**

1. Клонировать репозиторий

2. Открыть командную консоль и в корневой дириктории введите команду
 
```
docker build -t test_app .

```

3. После того как образ будет собран нужно ввести команду 
	
```
docker run -p 8001:8001 --name app_container test_app

```
