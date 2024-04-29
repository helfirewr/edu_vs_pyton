# Wzorzec projektowy Dependency Injection jest używany do oddzielenia tworzenia obiektów
# od ich używania, co pozwala na zmniejszenie zależności między klasami.

# Zalety:
# 1. Ułatwia testowanie, poprzez umożliwienie podstawiania 
#    fałszywych implementacji (mocków).
# 2. Zwiększa elastyczność i możliwość ponownego wykorzystania kodu.
# 3. Ułatwia zarządzanie zależnościami między klasami.

# Wady:
# 1. Może skomplikować konfigurację systemu.
# 2. Zwiększenie liczby klas i interfejsów w projekcie.

class Report:
    def __init__(self, content):
        self.content = content

class ReportGenerator:
    def generate_report(self):
        return Report("Zawartość raportu")

class ReportSaver:
    def save_report(self, report):
        print(f"Zapisano raport: {report.content}")

class ReportService:
    def __init__(self, generator, saver):
        self.generator = generator
        self.saver = saver

    def create_and_save_report(self):
        report = self.generator.generate_report()
        self.saver.save_report(report)

# Użycie wzorca Dependency Injection
generator = ReportGenerator()
saver = ReportSaver()
report_service = ReportService(generator, saver)

report_service.create_and_save_report()
