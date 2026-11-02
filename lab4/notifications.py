"""Три шаблона проектирования на примере службы уведомлений."""

from abc import ABC, abstractmethod


class EmailNotification:
    def __init__(self, text):
        self.text = text

    def format(self):
        return f"Email: {self.text}"


class SmsNotification:
    def __init__(self, text):
        self.text = text

    def format(self):
        return f"SMS: {self.text}"


class NotificationFactory(ABC):
    """Порождающий шаблон «Фабричный метод»."""

    @abstractmethod
    def create(self, text):
        pass


class EmailFactory(NotificationFactory):
    def create(self, text):
        return EmailNotification(text)


class SmsFactory(NotificationFactory):
    def create(self, text):
        return SmsNotification(text)


class NotificationCenter:
    """Поведенческий шаблон «Наблюдатель»: рассылка подписчикам."""

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def publish(self, notification):
        for subscriber in self.subscribers:
            subscriber.update(notification)


class LegacyPrinter:
    """Старый интерфейс: принимает готовую строку."""

    def send_text(self, text):
        print(text)


class PrinterAdapter:
    """Структурный шаблон «Адаптер»: приводит старый интерфейс к update."""

    def __init__(self, printer):
        self.printer = printer

    def update(self, notification):
        self.printer.send_text(notification.format())
