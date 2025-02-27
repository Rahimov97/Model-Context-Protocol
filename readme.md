# MCP File Finder Server

## Требования
- Python 3.7+
- Flask (`pip install flask`)
- Cline в VSCode

## Установка и запуск

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/mcp-file-finder.git
   cd mcp-file-finder
   ```
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Запустите сервер:
   ```sh
   python mcp_service.py
   ```

Сервер запустится на `http://127.0.0.1:5000`.

## Конфигурация Cline
Создайте или обновите файл `.cline.json` в корне проекта:
```json
{
  "mcpServers": {
    "file-finder-mcp": {
      "args": [
        "python",
        "mcp_service.py"
      ],
      "command": "python",
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

## Пример тестового запроса
Отправьте GET-запрос:
```sh
curl "http://127.0.0.1:5000/search?fragment=test"
```

Пример ответа:
```json
[
  {
    "name": "test_file.txt",
    "path": "C:\\Users\\User\\Documents\\test_file.txt",
    "size": 1234,
    "created_at": "2025-02-27T14:30:00"
  }
]
```
