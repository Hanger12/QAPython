# Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Hanger12/QAPython.git
    ```

2. Установите зависимости:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Linux/Mac
    # или
    venv\Scripts\activate  # Для Windows
   
   pip install -r requirements.txt
   ```

# Проект автоматизации e2e тестирования для сайта saucedemo.com
1. Установите драйвер браузера:
    - Для Chrome [скачайте драйвер](https://chromedriver.chromium.org/downloads).
    - Для YandexBrowser [скачайте драйвер](https://github.com/yandex/YandexDriver/releases/tag/v24.7.0-stable)

## Запуск теста

Запустите тест:
```bash
cd e2e_tests
python test_saucedemo.py
```
# Проект автоматического теста для работы с GitHub API
1. Настройте файл `.env`:
    - Создайте файл `.env` в корне проекта:
    ```bash
    touch .env
    ```
    - Добавьте в `.env` файл ваши данные:
    ```txt
    GITHUB_TOKEN=your_github_token
    GITHUB_USER=your_github_username
    REPO_NAME=test-repo
    ```

    - Получить токен можно в настройках GitHub по ссылке: https://github.com/settings/tokens

## Запуск теста

Для запуска теста выполните:
```bash
cd GitHub_API
python test_api.py