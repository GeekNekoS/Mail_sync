from django.db import models


class EmailAccount(models.Model):
    """Модель для хранения данных почтового аккаунта."""
    email = models.EmailField(unique=True, verbose_name="Почтовый адрес")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    provider = models.CharField(
        max_length=50,
        choices=[('yandex.ru', 'Yandex'), ('gmail.com', 'Gmail'), ('mail.ru', 'Mail')],
        verbose_name="Почтовый сервис"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.email} ({self.provider})"


class EmailMessage(models.Model):
    """Модель для хранения информации о сообщениях."""
    account = models.ForeignKey(
        EmailAccount,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Почтовый аккаунт"
    )
    message_id = models.CharField(max_length=255, unique=True, verbose_name="ID сообщения")
    subject = models.CharField(max_length=255, verbose_name="Тема сообщения")
    sent_date = models.DateTimeField(verbose_name="Дата отправки")
    received_date = models.DateTimeField(verbose_name="Дата получения")
    message_text = models.TextField(verbose_name="Текст сообщения")
    attachments = models.JSONField(default=list, blank=True, verbose_name="Список вложений")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")

    def __str__(self):
        account_email = self.account.email if self.account else 'Unknown account'
        return f"Message from {self.sent_date} to {account_email}"
