import os
import django
import threading

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from myapp.models import TestModel

print(f"[Caller] Thread ID: {threading.get_ident()}")
TestModel.objects.create(name="Thread Test")
