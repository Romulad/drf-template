# DRF Template

This repository serves as a starting template I use to build RESTful APIs with Django Rest Framework (DRF).

## Features

- Pre-configured Django Rest Framework setup.
- Token-based authentication with JWT.
- Modular app structure for scalability.
- Example models, serializers, and views.

**Note**: The `apps_dir` directory is where all Django apps for this project are organized. Make sure to create a new Django app in the `apps_dir/<app_name>/` directory (e.g., `apps_dir/my_app/`) and update the `apps.py` file of the newly created app after its creation.

## Requirements

- Python 3.12+
- Django 5.0+
- Django Rest Framework 3.16+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Romulad/drf-template.git
cd drf-template
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Customize the `settings.py` file to suit your project needs.
- Add the `.env` file use `env.template` as example to suit your project needs.
- Add new apps and extend the provided models, serializers, and views.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.