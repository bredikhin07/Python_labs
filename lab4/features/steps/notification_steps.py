from unittest.mock import Mock

from behave import given, then, when

from notifications import EmailFactory, NotificationCenter, PrinterAdapter, SmsFactory


@given("создана фабрика уведомлений")
def step_factory(context):
    context.factory = EmailFactory()


@when('я создаю уведомление "{kind}" с текстом "{text}"')
def step_create(context, kind, text):
    assert kind == "email"
    context.notification = context.factory.create(text)


@then('формат сообщения равен "{expected}"')
def step_format(context, expected):
    assert context.notification.format() == expected


@given("центр с двумя подписчиками")
def step_two_subscribers(context):
    context.center = NotificationCenter()
    context.subscribers = [Mock(), Mock()]
    for subscriber in context.subscribers:
        context.center.subscribe(subscriber)


@given("центр со старым принтером через адаптер")
def step_legacy_printer(context):
    context.center = NotificationCenter()
    context.printer = Mock()
    context.center.subscribe(PrinterAdapter(context.printer))


@when('я публикую SMS с текстом "{text}"')
def step_publish_sms(context, text):
    context.notification = SmsFactory().create(text)
    context.center.publish(context.notification)


@then("каждый подписчик получает это сообщение один раз")
def step_each_subscriber(context):
    for subscriber in context.subscribers:
        subscriber.update.assert_called_once_with(context.notification)


@then('старый принтер получает строку "{expected}"')
def step_printer(context, expected):
    context.printer.send_text.assert_called_once_with(expected)
