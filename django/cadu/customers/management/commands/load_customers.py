from django.core.management.base import BaseCommand

from cadu.extensions.publisher.publisher import PublisherCustomers


class Command(BaseCommand):
    help = 'Load customers'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        publisher = PublisherCustomers()
        try:
            publisher.load_data(url)
        except Exception as error:
            self.stdout.write(
                self.style.ERROR(f'Error to load customer. Error {error}')
            )

        self.stdout.write(
            self.style.SUCCESS('Customer loaded with success')
        )
