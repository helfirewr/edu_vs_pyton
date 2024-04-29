# Napisz program decydujący czy wyjść czy zostać w domu zależnie od pogody
# 1) Dodaj zmienne:
#    - raining = False
#    - haveUmbrella = False
#    - temperature = 14
# 2) Sprawdź czy temperatura jest powyżej lub równa 40 lub poniżej lub równa 0
#    w takim wypadku wyświetl "Zostań w domu"
# 3) Jeżeli powyższy warunek nie jest spełniony w elif sprawdź kolejny czy
#    temperatura jest powyżej 0 oraz poniżej 10 stopni oraz ma parasolkę
#    i pada, w takim wypadku wyświetl: "Możesz wyjść z parasolką"
# 4) Gdy żadne z powyższych nie jest spełnione sprawdź w kolejnym elif
#    czy nie pada i temperatura jest powyżej lub równe 10 to wyświetl:
#    "Możesz wyjść bez parasolki"
# 5) Na koniec dodaj ostatnią domyślną opcję z informacją "Zostań w domu"

raining = False
haveUmbrella = False
temperature = 9

if temperature >= 40 or temperature <= 0:
    print("Zostań w domu, za niska, za wysoka temperatura")
elif temperature > 0 and temperature < 10 and haveUmbrella and raining:
    print("Możesz wyjść z parasolką")
elif raining == False and temperature >= 10:
    print("Możesz wyjść bez parasola")
else:
    print("Zostań w domu")



