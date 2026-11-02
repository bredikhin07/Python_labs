from notifications import EmailFactory, LegacyPrinter, NotificationCenter, PrinterAdapter, SmsFactory


def main():
    center = NotificationCenter()
    center.subscribe(PrinterAdapter(LegacyPrinter()))

    center.publish(EmailFactory().create("Лабораторная работа готова"))
    center.publish(SmsFactory().create("Проверка пройдена"))


if __name__ == "__main__":
    main()
