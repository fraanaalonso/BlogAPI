release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py collectstatic --dry-run --noinput
web: gunicorn config.wsgi
