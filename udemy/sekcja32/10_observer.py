# Wzorzec projektowy Observer jest używany do tworzenia systemu, w którym obiekty
# mogą obserwować zmiany w innym obiekcie i być o nich informowane.

# Zalety:
# 1. Wspiera zasadę otwarto-zamknięte, ułatwiając rozszerzanie funkcjonalności.
# 2. Umożliwia luźne powiązanie między obserwatorem a podmiotem.

# Wady:
# 1. Może być trudny do debugowania ze względu na indyrekcyjną komunikację.
# 2. Może prowadzić do niespodziewanych aktualizacji, jeśli nie jest odpowiednio zarządzany.

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class JobPostings:
    def __init__(self):
        self._observers = []
        self._job_postings = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def add_job(self, job_posting):
        self._job_postings.append(job_posting)
        self._notify(job_posting)

    def _notify(self, job_posting):
        for observer in self._observers:
            observer.update(job_posting)

class JobSeeker(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, job_posting):
        print(f"{self._name} został powiadomiony o nowej ofercie pracy: {job_posting}")

# Użycie wzorca Observer
job_postings = JobPostings()
john_doe = JobSeeker("John Doe")
jane_doe = JobSeeker("Jane Doe")

job_postings.subscribe(john_doe)
job_postings.subscribe(jane_doe)

job_postings.add_job("Inżynier oprogramowania")
job_postings.add_job("Projektant UX")

job_postings.unsubscribe(jane_doe)

job_postings.add_job("Menadżer produktu")

# W tym przykładzie:
# 'JobPostings' pełni rolę podmiotu, a 'JobSeeker' to obserwatorzy.
# Obserwatorzy subskrybują podmiot, aby otrzymywać powiadomienia o nowych ofertach pracy.
# 'JobPostings' informuje zarejestrowanych obserwatorów o każdej nowej ofercie pracy.

