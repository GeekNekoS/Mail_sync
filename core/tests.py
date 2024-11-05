from .models import EmailAccount, EmailMessage
from django.utils import timezone
from django.test import TestCase


class EmailAccountModelTest(TestCase):
    def setUp(self):
        self.account = EmailAccount.objects.create(
            email='test@example.com',
            password='securepassword',
            provider='gmail.com'
        )

    def test_email_account_creation(self):
        self.assertEqual(self.account.email, 'test@example.com')
        self.assertEqual(self.account.provider, 'gmail.com')
        self.assertIsInstance(self.account.created_at, timezone.datetime)
        self.assertIsInstance(self.account.updated_at, timezone.datetime)


class EmailMessageModelTest(TestCase):
    def setUp(self):
        self.account = EmailAccount.objects.create(
            email='test@example.com',
            password='securepassword',
            provider='gmail.com'
        )
        self.message = EmailMessage.objects.create(
            account=self.account,
            message_id='12345',
            subject='Test Subject',
            sent_date=timezone.now(),
            received_date=timezone.now(),
            message_text='This is a test message.',
            attachments=[]
        )

    def test_email_message_creation(self):
        self.assertEqual(self.message.subject, 'Test Subject')
        self.assertEqual(self.message.account, self.account)
        self.assertIsInstance(self.message.sent_date, timezone.datetime)
        self.assertIsInstance(self.message.received_date, timezone.datetime)
        self.assertFalse(self.message.is_read)
