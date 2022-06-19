import csv
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# tutaj zmieniasz zestaw słówek
with open('slowka.csv', mode='r') as infile:
    reader = csv.reader(infile)
    nieodpowiedziane = {rows[0]: rows[1] for rows in reader}
tryb = input("Wybierz tryb nauka/test")
liczba_pytan = 5
nr_pytania = 0
runda = 1
dobre = 0
zle = 0
koniec = False
nieodpowiedziane_temp = nieodpowiedziane.copy()
while len(nieodpowiedziane_temp) != 0:
    print(f'''Runda {runda}''')
    nieodpowiedziane = nieodpowiedziane_temp.copy()
    keys = list(nieodpowiedziane.keys())
    random.shuffle(keys)
    for pol in keys:
        nr_pytania += 1
        rus = nieodpowiedziane[pol]
        odp = input("\t" + pol)
        if odp == rus:
            dobre += 1
            nieodpowiedziane_temp.pop(pol)
        else:
            zle += 1
            bledy = rus
            # bledy = ""
            # if len(odp) < len(rus):
            #     krotsze = odp
            # else:
            #     krotsze = rus
            # for ind in range(len(krotsze)):
            #     if odp[ind] == rus[ind]:
            #         bledy += rus[ind]
            #     else:
            #         bledy += bcolors.WARNING + rus[ind] + bcolors.ENDC
            # brak = len(rus) - len(krotsze)
            # if brak != 0:
            #     bledy += bcolors.WARNING + rus[-brak:] + bcolors.ENDC
            print(f'''Poprawna odpowiedź to: {bledy}''')
        if tryb == "test" and nr_pytania >= liczba_pytan:
            print(f'''Twój wynik to {round(dobre / (dobre + zle), 4) * 100} %''')
            koniec = True
            break
    if koniec:
        break
    if len(nieodpowiedziane_temp) == 0:
        print(f'''Gratulacje! Skończyłeś_aś po {runda} rundach.''')

    runda += 1
    print("\n" * 50)
