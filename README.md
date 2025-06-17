# Personal Business Card Flask Application | Веб-приложение для персональной визитки

[![Tests](https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2/actions/workflows/python-app.yml/badge.svg)](https://github.com/IsDarkByte/FlaskProjectPersonalBusinessCard2/actions/workflows/python-app.yml)

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
- Code quality checks with ruff

### Tech Stack

- **Backend**: Flask 3.0.2
- **Database**: SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: pytest
- **Code Quality**: ruff
- **CI/CD**: GitHub Actions

### Prerequisites

- Python 3.11 or higher
- uv (universal Python package/dependency manager)
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

3. Install uv (if not installed):
```bash
pip install uv  # or: pipx install uv
```

4. Install dependencies:
```bash
uv pip install  # uses pyproject.toml
# or, if you prefer:
uv pip install -r requirements.txt
```

5. Create `.env` file in the root directory with the following content:
```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

6. Initialize the database:
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

### Running Linting (ruff)

To check code quality and style using ruff, run:
```bash
ruff check .
```
You can also auto-fix some issues with:
```bash
ruff check . --fix
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
- Проверка качества кода с ruff

### Технологический стек

- **Бэкенд**: Flask 3.0.2
- **База данных**: SQLAlchemy
- **Фронтенд**: HTML, CSS, JavaScript
- **Тестирование**: pytest
- **Качество кода**: ruff
- **CI/CD**: GitHub Actions

### Требования

- Python 3.11 или выше
- uv (универсальный менеджер зависимостей Python)
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

3. Установите uv (если не установлен):
```bash
pip install uv  # или: pipx install uv
```

4. Установите зависимости:
```bash
uv pip install  # используется pyproject.toml
# или, если нужно:
uv pip install -r requirements.txt
```

5. Создайте файл `.env` в корневой директории со следующим содержимым:
```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

6. Инициализируйте базу данных:
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

### Запуск линтинга (ruff)

Для проверки качества и стиля кода с помощью ruff выполните:
```bash
ruff check .
```
Также можно автоматически исправить некоторые ошибки:
```bash
ruff check . --fix
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