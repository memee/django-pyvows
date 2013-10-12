import os, subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        os.environ["PYTHONPATH"] = os.environ.get("PYTHONPATH", "") + ":."
        subprocess.call(["pyvows"] + list(args))
