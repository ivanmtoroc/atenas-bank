# Django
from django.core.management.base import BaseCommand, CommandError

# Models
from apps.offices.models import Office, Domain

class Command(BaseCommand):
    help = 'Creates the public tenant record for the project.'

    def handle(self, **kwargs):
        public_tenant, created = Office.objects.get_or_create(
            schema_name = 'public',
            code = '000',
            name = 'Public tenant'
        )

        if created:
            success_message = self.style.SUCCESS('Successfully created public tenant!')
            self.stdout.write(success_message)
        else:
            raise CommandError('Public tenant is already created.')

        public_domain, created = Domain.objects.get_or_create(
            domain = 'localhost',
            tenant_id = '000'
        )
