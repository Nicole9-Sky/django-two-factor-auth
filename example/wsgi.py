import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

try:
    from .create_superuser import run
    run()
except Exception as e:
    print(f"Error creating superuser: {e}")


application = get_wsgi_application()
