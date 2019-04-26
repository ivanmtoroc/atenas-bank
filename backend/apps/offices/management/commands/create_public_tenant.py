# Django
from django.core.management.base import BaseCommand, CommandError

# Offices models
from apps.offices.models import OfficeModel, DomainModel

class Command(BaseCommand):
    help = 'Create the public tenant record for the project.'

    def handle(self, **kwargs):
        public_tenant, created = OfficeModel.objects.get_or_create(
            schema_name = 'public',
            name = 'Public tenant'
        )

        if created:
            public_domain, created = DomainModel.objects.get_or_create(
                domain = 'localhost',
                tenant_id = public_tenant.id
            )
            success_message = self.style.SUCCESS('Successfully created public tenant!')
            self.stdout.write(success_message)
        else:
            raise CommandError('Public tenant is already created.')
