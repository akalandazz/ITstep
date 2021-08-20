import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from projectlogger.logger import Logger
log = Logger('test.log')

class Command(BaseCommand):
	help = "Sends an e-mail reminder to users registered more\
			than N days that are not enrollled into any courses yet"

	def add_arguments(self, parser):
		parser.add_argument('--days', dest='days', type=int)

	def handle(self, *args, **options):
		emails = []
		subject = "Enroll in a Course"
		date_joined = timezone.now() - datetime.timedelta(days = options['days'])
		users = User.objects.annotate(course_count = Count('courses_joined')).filter(course_count = 0, date_joined__date__lte = date_joined)
		log.info(f'{users}')
		for user in users:
			message = f""" Dear {user.first_name}!
			we noticed that you didn't enroll in any course yet.
			what are you waiting for ? """
			emails.append((user,message, settings.DEFAULT_FROM_EMAIL, [user.email]))

		send_mass_mail(emails)
		self.stdout.write(f"Sent {len(emails)} reminders! ")
