"""TDD: отдельные проверки поведения через unittest."""

import unittest
from unittest.mock import Mock

from notifications import (
    EmailNotification,
    EmailFactory,
    NotificationCenter,
    NotificationFactory,
    PrinterAdapter,
    SmsNotification,
    SmsFactory,
)


class NotificationTests(unittest.TestCase):
    def test_factory_creates_email_and_sms(self):
        email = EmailFactory().create("Готово")
        sms = SmsFactory().create("Готово")
        self.assertIsInstance(email, EmailNotification)
        self.assertIsInstance(sms, SmsNotification)
        self.assertEqual(email.format(), "Email: Готово")
        self.assertEqual(sms.format(), "SMS: Готово")

    def test_base_factory_cannot_be_created(self):
        with self.assertRaises(TypeError):
            NotificationFactory()

    def test_center_notifies_each_subscriber_once(self):
        center = NotificationCenter()
        first, second = Mock(), Mock()
        message = EmailFactory().create("Готово")
        center.subscribe(first)
        center.subscribe(first)
        center.subscribe(second)
        center.publish(message)
        first.update.assert_called_once_with(message)
        second.update.assert_called_once_with(message)

    def test_unsubscribed_observer_receives_nothing(self):
        center = NotificationCenter()
        subscriber = Mock()
        center.subscribe(subscriber)
        center.unsubscribe(subscriber)
        center.publish(SmsFactory().create("Готово"))
        subscriber.update.assert_not_called()

    def test_adapter_calls_legacy_printer_with_formatted_message(self):
        printer = Mock()
        adapter = PrinterAdapter(printer)
        adapter.update(SmsFactory().create("Готово"))
        printer.send_text.assert_called_once_with("SMS: Готово")


if __name__ == "__main__":
    unittest.main()
