#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# para iniciar el programa debes entrar al entorno virtual (.\venv\Scripts\activate), luego si no esta creada la base de datos, crearla en conecion_sqlite3.py, con esto hecho y con las migraciones al dia, basta con hacer nun runserver y tulizar la aplicacion.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
