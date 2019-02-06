"""
Module with functions dedicated to
manipulating data as a user
"""

import json
from bibliotekar import ucitavanje_zaduzenja, ucitavanje_knjiga, ucitavanje_korisnika

trenutno_prijavljen = []


def prijava_korisnik():
    # User's login system
    # If login is successful, the user ..
    # is presented with the user-dedicated main menu

    trenutno_prijavljen.clear()

    korisnici = ucitavanje_korisnika()
    prijavljen = False
    while not prijavljen:
        korisnicko_ime = input("\nKorisnicko ime: ")
        lozinka = input("\nLozinka: ")

        for korisnik in korisnici:
            if korisnicko_ime == korisnik["korisnicko_ime"] and \
                    lozinka == korisnik["lozinka"] and \
                    not korisnik["izbrisan"]:
                print(f"\nUspesno ste se prijavili kao korisnik - {korisnik['ime']} {korisnik['prezime']}")
                trenutno_prijavljen.append(korisnik)
                glavni_meni()
                prijavljen = True
        if not prijavljen:
            print("\nPogresno korisnicko ime ili lozinka.\n")
            return


def glavni_meni():
    # Function for the user's main menu
    # It gives the user a set of options that only users ..
    # can access when logged in
    # User then picks the sequential number of the option he wants to use
    # After which the according function is triggered

    while True:
        print("\nGLAVNI MENI\n\n"
              "1) Pregled zaduzenih knjiga\n"
              "2) Pretrazivanje knjiga\n"
              "3) Izmena podataka trenutno prijavljenog korisnika\n"
              "\nDa biste se odjavili i izasli iz programa, unesite \"q\"")
        izbor = input("\nIzaberite akciju: ")

        if izbor == "1":
            print("\nPREGLED ZADUZENIH KNJIGA\n")
            pregled_zaduzenih_knjiga()
        elif izbor == "2":
            print("\nPRETRAZIVANJE KNJIGA")
            pretrazivanje_knjiga()
        elif izbor == "3":
            print("\nIZMENA PODATAKA TRENUTNO PRIJAVLJENOG KORISNIKA\n")
            izmena_korisnika()
        elif izbor == "q":
            print("\nUspesno ste se odjavili.")
            return False
        else:
            print("\nNiste uneli dobar redni broj.")


def pregled_zaduzenih_knjiga():
    # Function for showcasing obligated books for the currently logged in user

    zaduzenja = ucitavanje_zaduzenja()
    r_b = 0

    for zaduzenje in zaduzenja:
        for prijavljen in trenutno_prijavljen:
            if prijavljen["clanska_karta"] == zaduzenje["clanska_karta"]:
                r_b += 1
                print("{}  |\t\t {} \t\t|\t\t {} \t\t|\t\t {} \t\t|".format(r_b,
                                                                            zaduzenje["id_knjige"],
                                                                            zaduzenje["clanska_karta"],
                                                                            zaduzenje["datum_zaduzivanja"]
                                                                            ))


def pretrazivanje_knjiga():
    # Function for searching books
    # The search can be done by 2 parameters (author or the name of the book)
    # After the book is printed out, it tells the user whether there are any copies available,
    # and if so, how much. It also tell the user whether there aren't any copies available

    knjige = ucitavanje_knjiga()

    pronadjena = False

    while not pronadjena:
        try:
            pretraga = input("Pretraga: ")
            if not pretraga:
                raise ValueError
        except ValueError:
            print("\nMorate nesto uneti!\n")
        else:
            for knjiga in knjige:
                if pretraga.lower() in knjiga["ime_knjige"].lower() or \
                        pretraga.lower() in knjiga["autor"].lower():
                    print("| ID: {} |"
                          "\t\t Autor: {:>25} \t\t|"
                          "\t\t Ime knjige: {:>25} \t\t|"
                          "\t\t Godina izdavanja: {} \t\t|".format(knjiga["id"],
                                                                   knjiga["autor"],
                                                                   knjiga["ime_knjige"],
                                                                   knjiga["god_izd"]))
                    if knjiga["br_slob_prim"] != 0:
                        print("\nIma {} slobodna/slobodnih primerka/primeraka za {}.\n".format(knjiga["br_slob_prim"],
                                                                                               knjiga["ime_knjige"]))
                    elif knjiga["br_slob_prim"] == 0:
                        print("\nNema slobodnih primeraka knjige {}.\n".format(knjiga["ime_knjige"]))
                    pronadjena = True
            if not pronadjena:
                print("\nKnjiga nije pronadjena. Pokusajte ponovo.\n")


def prikaz_korisnika(korisnik):
    # Function for printing users that are used inside of for loops in this module

    print("| Clanska karta: {} |"
          "\t\t Ime: {:>7} \t\t|"
          "\t\t Prezime: {:>10} \t\t|"
          "\t\t Korisnicko ime: {:>10} \t\t|"
          "\t\t Lozinka: {:>15} \t\t|".format(korisnik["clanska_karta"],
                                              korisnik["ime"],
                                              korisnik["prezime"],
                                              korisnik["korisnicko_ime"],
                                              korisnik["lozinka"]))


def izmena_korisnika():
    # Function for editing the currently signed in user's data

    korisnici = ucitavanje_korisnika()

    for korisnik in korisnici:
        for prijavljen in trenutno_prijavljen:
            if prijavljen["korisnicko_ime"] == korisnik["korisnicko_ime"]:
                prikaz_korisnika(korisnik)
                print("\nIzaberite opciju za izmenu:\n\n"
                      "1) Ime\n"
                      "2) Prezime\n"
                      "3) Korisnicko ime\n"
                      "4) Lozinka\n\n\n"
                      "5) Izadji ")
                promena = input("Unesite redni broj: ")
                if promena == "1":
                    novo_ime = input("Novo Ime: ")
                    print("\n")
                    korisnik["ime"] = novo_ime
                    with open("../data/korisnici.json", "w") as upis:
                        json.dump(korisnici, upis, indent=4)
                    prikaz_korisnika(korisnik)
                    print("\nIme korisnika promenjeno u {}.".format(novo_ime))
                    return
                elif promena == "2":
                    novo_prezime = input("Novo Prezime: ")
                    print("\n")
                    korisnik["prezime"] = novo_prezime
                    with open("../data/korisnici.json", "w") as upis:
                        json.dump(korisnici, upis, indent=4)
                    prikaz_korisnika(korisnik)
                    print("\nIzmenjeno prezime za korisnika - {},  u {}.".format(korisnik["ime"], novo_prezime))
                    return
                elif promena == "3":
                    novo_korisnicko_ime = input("Novo Korisnicko Ime: ")
                    print("\n")
                    korisnik["korisnicko_ime"] = novo_korisnicko_ime
                    with open("../data/korisnici.json", "w") as upis:
                        json.dump(korisnici, upis, indent=4)
                    prikaz_korisnika(korisnik)
                    print("\n\nKorisnicko ime za korisnika - {} {},  izmenjeno u {}.".format(korisnik["ime"],
                                                                                             korisnik["prezime"],
                                                                                             novo_korisnicko_ime))
                    return
                elif promena == "4":
                    nova_lozinka = input("Nova lozinka: ")
                    print("\n")
                    korisnik["lozinka"] = nova_lozinka
                    with open("../data/korisnici.json", "w") as upis:
                        json.dump(korisnici, upis, indent=4)
                    prikaz_korisnika(korisnik)
                    print("\nLozinka izmenjena!")
                    return
                elif promena == "5":
                    print("\nPovratak na glavni meni.")
                    return
                else:
                    print("\nUneli ste nepostojeci broj. Program ce biti prekinut.")
