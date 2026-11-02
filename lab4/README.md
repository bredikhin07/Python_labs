# Лабораторная работа №4

Предметная область — уведомления. Реализованы три шаблона:

- **Фабричный метод**: базовый `NotificationFactory` задаёт метод создания,
  а `EmailFactory` и `SmsFactory` создают свои виды сообщений.
- **Наблюдатель**: `NotificationCenter` уведомляет подписчиков.
- **Адаптер**: `PrinterAdapter` подключает `LegacyPrinter` со старым методом `send_text`.

`test_notifications.py` содержит модульные тесты на `unittest` (TDD-часть),
в том числе проверки с `unittest.mock.Mock`. В `features/` находятся
BDD-сценарии для фреймворка `behave`.

Запуск из папки `lab4`:

```sh
python3 main.py
python3 -m unittest -v
python3 -m pip install -r requirements.txt
python3 -m behave
```

Фактический ход разработки по TDD (тест → ошибка → реализация → повторный запуск)
следует показывать при защите отдельно; наличие тестов само по себе не доказывает,
что программа создавалась именно в этом порядке.
