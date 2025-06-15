# Personal Business Card Flask Application | Веб-приложение для персональной визитки

[English](#english) | [Русский](#russian)

<a name="english"></a>
## English

A modern web application built with Flask that serves as a personal business card/portfolio website.

### Features

- Modern and responsive design
- Contact form functionality
- Database integration with SQLAlchemy
- User authentication system
- RESTful API endpoints
- Automated testing with pytest
- Code quality checks with flake8

### Tech Stack

- **Backend**: Flask 3.0.2
- **Database**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: pytest
- **Code Quality**: flake8
- **CI/CD**: GitHub Actions

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2.git
cd FlaskProjectPersonalBusinessCard2
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the root directory with the following content:
```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

### Running the Application

1. Start the development server:
```bash
flask run
```

2. Open your browser and navigate to `http://localhost:5000`

### Running Tests

```bash
pytest
```

### Project Structure

```
FlaskProjectPersonalBusinessCard2/
├── .github/
│   └── workflows/          # GitHub Actions configuration
├── app/
│   ├── main/              # Main application blueprint
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   └── __init__.py        # Application factory
├── tests/                 # Test files
├── .env                   # Environment variables
├── .gitignore            # Git ignore file
├── config.py             # Configuration
├── LICENSE               # MIT License
├── README.md             # This file
├── requirements.txt      # Project dependencies
└── run.py               # Application entry point
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

IsDarkByte - [@IsDarkByte](https://github.com/IsDarkByte)

Project Link: [https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2](https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2)

---

<a name="russian"></a>
## Русский

Современное веб-приложение, построенное на Flask, которое служит персональной визиткой/портфолио.

### Возможности

- Современный и адаптивный дизайн
- Функциональность контактной формы
- Интеграция с базой данных через SQLAlchemy
- Система аутентификации пользователей
- RESTful API endpoints
- Автоматизированное тестирование с pytest
- Проверка качества кода с flake8

### Технологический стек

- **Бэкенд**: Flask 3.0.2
- **База данных**: SQLAlchemy
- **Фронтенд**: HTML, CSS, JavaScript
- **Тестирование**: pytest
- **Качество кода**: flake8
- **CI/CD**: GitHub Actions

### Требования

- Python 3.11 или выше
- pip (менеджер пакетов Python)
- Git

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2.git
cd FlaskProjectPersonalBusinessCard2
```

2. Создайте и активируйте виртуальное окружение:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `.env` в корневой директории со следующим содержимым:
```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

5. Инициализируйте базу данных:
```bash
flask db init
flask db migrate
flask db upgrade
```

### Запуск приложения

1. Запустите сервер разработки:
```bash
flask run
```

2. Откройте браузер и перейдите по адресу `http://localhost:5000`

### Запуск тестов

```bash
pytest
```

### Структура проекта

```
FlaskProjectPersonalBusinessCard2/
├── .github/
│   └── workflows/          # Конфигурация GitHub Actions
├── app/
│   ├── main/              # Основной blueprint приложения
│   ├── static/            # Статические файлы (CSS, JS, изображения)
│   ├── templates/         # HTML шаблоны
│   └── __init__.py        # Фабрика приложения
├── tests/                 # Файлы тестов
├── .env                   # Переменные окружения
├── .gitignore            # Файл игнорирования Git
├── config.py             # Конфигурация
├── LICENSE               # Лицензия MIT
├── README.md             # Этот файл
├── requirements.txt      # Зависимости проекта
└── run.py               # Точка входа в приложение
```

### Участие в разработке

1. Форкните репозиторий
2. Создайте ветку для вашей функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте ваши изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте изменения в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

### Лицензия

Этот проект лицензирован под MIT License - подробности в файле [LICENSE](LICENSE).

### Контакты

IsDarkByte - [@IsDarkByte](https://github.com/IsDarkByte)

Ссылка на проект: [https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2](https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2) 