import os
import django
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from myapp.models import TestModel

start = time.time()
TestModel.objects.create(name="Sync Signal Test")
end = time.time()

print(f"Elapsed time: {end - start:.2f} seconds")
