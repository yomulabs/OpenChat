import os
from django.core.wsgi import get_wsgi_application

from dj_backend_server.celery import app
from api.data_sources.pdf_handler import pdf_handler
from web.workers.crawler import start_recursive_crawler
from django.core.management.base import BaseCommand


# Initialize the Django application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
get_wsgi_application()

# Replace 'your_project_name' and 'your_app_name' with the actual names.

# Define the arguments for your pdf_handler view function
shared_folder = "dbe7a19fb6a2d643b5b3ab1c737a18af5b0048ca"
namespace = "e74022dd-a48c-490b-92b7-7524f23b9b6d"

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Call the Celery task asynchronously
        #task = pdf_handler.apply_async(args=[shared_folder, namespace])
        start_recursive_crawler("abc","067d13c4-7110-4374-b797-f5f2356964b1")
