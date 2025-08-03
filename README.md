# Link-monitoring
Временный репозиторий

Скрипт проверяет указанный сайт на работоспособность и определяет dofollow/nofollow

Примеры работы:
```
input: https://www.google.com/
output: {'url': 'https://www.google.com/', 'is_alive': True, 'status': 200, 'rel': 'dofollow'}
```
```
input: https://chatgpt.com/
output: {'url': 'https://chatgpt.com/', 'is_alive': False, 'status': 403, 'rel': 'dofollow'}
```
```
input: https://kwork.ru/
output: {'url': 'https://kwork.ru/', 'is_alive': True, 'status': 200, 'rel': 'dofollow'}
```
