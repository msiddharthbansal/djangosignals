import os
import django
from django.db import transaction

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from myapp.models import TestModel, SignalLog

try:
    with transaction.atomic():
        TestModel.objects.create(name="Should rollback")
        raise Exception("Force rollback")
except Exception as e:
    print(f"Transaction rolled back: {e}")

if SignalLog.objects.exists():
    print("SignalLog didn't rolled back")
else:
    print("SignalLog rolled back")
