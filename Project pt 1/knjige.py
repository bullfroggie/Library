"""
Module with functions dedicated to
manipulating book related data
"""

import src.bibliotekar as bibliotekar
import src.podaci_knjige as knjige


def prikaz_knjiga():
    # Function for printing all of the books from the podaci_knjige.py file

        print("{:^226}".format("KNJIGE\n"))
        for knjiga in knjige.knjige:
            print("| ID: {} |\t\t Autor: {:>25} \t\t|"
                  "\t\t Ime knjige: {:>25} \t\t|"
                  "\t\t Godina izdavanja: {} \t\t|"
                  "\t\t Ukupan br. primeraka: {} \t\t|"
                  "\t\t Br. slobodnih primeraka: {} \t\t|".format(
                    knjiga["id"],
                    knjiga["autor"],
                    knjiga["ime_knjige"],
                    knjiga["god_izd"],
                    knjiga["ukupan_br_prim"],
                    knjiga["br_slob_prim"]))


def dodavanje_knjige():
    # Function for adding books
    # Firstly checking whether the entered ID already exists
    # if that's not the case, then all of the other inputs are presented

    prikaz_knjiga()

    postoji = True
    nova_knjiga = {}
    id_od_svih_knjiga = []

    for ident in knjige.knjige:
        id_od_svih_knjiga.append(ident["id"])

    while postoji:
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            id_knjige = int(input("\nUnesite ID knjige: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.")
        else:
            if id_knjige == 1:
                return False
            if id_knjige not in id_od_svih_knjiga:
                postoji = False
                ime_knjige = input("Ime knjige: ")
                autor = input("Autor: ")
                try:
                    godina_izdavanja = int(input('Godina izdavanja: '))
                    ukupan_br_prim = int(input('Ukupan broj primeraka: '))
                    br_slob_prim = int(input('Broj slobodnih primeraka: '))
                except (ValueError, TypeError):
                    print("\nMorate uneti broj.\n")
                else:
                    nova_knjiga["id"] = id_knjige
                    nova_knjiga["autor"] = autor
                    nova_knjiga["ime_knjige"] = ime_knjige
                    nova_knjiga["god_izd"] = godina_izdavanja
                    nova_knjiga["ukupan_br_prim"] = ukupan_br_prim
                    nova_knjiga["br_slob_prim"] = br_slob_prim
                    knjige.knjige.append(nova_knjiga)

                    prikaz_knjiga()
                    return
            if postoji:
                print("\nUneti ID vec postoji.")


def izmena_knjige():
    # Function for editing books
    # Search for the book by the ID of the book
    # After the book is selected, the user can edit it

    prikaz_knjiga()

    pronadjena = False
    while not pronadjena:
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            pretraga = int(input("\nUnesite ID od knjige koju zelite da menjate: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.")
        else:
            if pretraga == 1:
                return False
            for knjiga in knjige.knjige:
                if pretraga == knjiga["id"]:
                    pronadjena = True
                    while True:
                        print("\nIzaberite opciju za izmenu:\n\n"
                              "1) Autor\n"
                              "2) Ime knjige\n"
                              "3) Godina izdavanja\n"
                              "4) Ukupan br. primeraka\n"
                              "5) Br. slobodnih primeraka\n\n"
                              "6) Povratak na glavni meni")
                        izmena = input("Unesite redni broj: ")
                        if izmena == "1":
                            novi_autor = input("Novi autor: ")
                            knjiga["autor"] = novi_autor
                            prikaz_knjiga()
                            print("\nAutor promenjen u {}.".format(novi_autor))
                            return
                        elif izmena == "2":
                            novo_ime_knjige = input("Novo ime knjige: ")
                            knjiga["ime_knjige"] = novo_ime_knjige
                            prikaz_knjiga()
                            print("\nIme knjige izmenjeno u {}.".format(novo_ime_knjige))
                            return
                        elif izmena == "3":
                            try:
                                nova_godina_izd = int(input("Nova godina izdavanja: "))
                            except (ValueError, TypeError):
                                print("\nMorate uneti broj.")
                            else:
                                knjiga["god_izd"] = nova_godina_izd
                                prikaz_knjiga()
                                print("\nIzmenjena godina izdavanja za knjigu - {},  u {}."
                                      .format(knjiga["ime_knjige"], nova_godina_izd))
                                return
                        elif izmena == "4":
                            try:
                                novi_ukupan_br_prim = int(input("Novi ukupan br. primeraka: "))
                            except (ValueError, TypeError):
                                print("\nMorate uneti broj.")
                            else:
                                knjiga["ukupan_br_prim"] = novi_ukupan_br_prim
                                prikaz_knjiga()
                                print("\nUkupan broj primeraka za knjigu - {},  izmenjen u {}."
                                      .format(knjiga["ime_knjige"], novi_ukupan_br_prim))
                                return
                        elif izmena == "5":
                            try:
                                novi_br_slobodnih_prim = int(input("Novi br. slobodnih primeraka: "))
                            except (ValueError, TypeError):
                                print("\nMorate uneti broj.")
                            else:
                                knjiga["br_slob_prim"] = novi_br_slobodnih_prim
                                prikaz_knjiga()
                                print("\nUkupan broj primeraka knjige - {},  izmenjen u {}."
                                      .format(knjiga["ime_knjige"], novi_br_slobodnih_prim))
                                return
                        elif izmena == "6":
                            print("Povratak na glavni meni.")
                            return
                        else:
                            print("\nMorate uneti postojeci redni broj. Pokusajte ponovo.")
            if not pronadjena:
                print("\nUneli ste nepostojeci ID. Pokusajte ponovo.")


def brisanje_knjige():
    # Function for deleting books
    # Firstly searching for the book by the ID of the book
    # After the book is picked, the user can delete it

    while True:
        prikaz_knjiga()
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            pretraga = int(input("\nUnesite ID od knjige koju zelite da izbrisete: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.")
        else:
            if pretraga == 1:
                return False
            for knjiga in knjige.knjige:
                if pretraga == knjiga["id"]:
                    knjige.knjige.remove(knjiga)
                    prikaz_knjiga()
                    bibliotekar.glavni_meni()
                    return False
            else:
                print("\nUneli ste nepostojeci ID, pokusajte ponovo.")


def rashodovanje():
    # Function for book dismantling
    # If the librarian notices that certain books are in bad shape..
    # he can remove copies of those books from the library system

    postoji = False
    while not postoji:
        print("\nUkoliko mislite da je stanje odredjene knjige"
              " dovedeno do toga da ju je potrebno rashodovati,\n"
              " \t\t\tunesite ID date knjige pa potom i broj primeraka za rashodovanje.\n")
        prikaz_knjiga()
        print("\n(hint) Za povratak na glavni meni u polje za ID unesite br. 1")
        try:
            izbor = int(input("\nUnesite ID knjige za rashodovanje: "))
            broj_primeraka = int(input("Broj primeraka za rashodovanje: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.\n")
        else:
            if izbor == 1:
                return False
            for knjiga in knjige.knjige:
                if izbor == knjiga["id"]:
                    if knjiga["ukupan_br_prim"] >= knjiga["ukupan_br_prim"] - broj_primeraka >= 0\
                       and knjiga["br_slob_prim"] != 0:

                        knjiga["ukupan_br_prim"] -= broj_primeraka
                        knjiga["br_slob_prim"] -= broj_primeraka
                        prikaz_knjiga()
                        print('\n***{} primerak/a knjige "{}", autora - {}, uspesno rashodovan/o.\n***'
                              .format(broj_primeraka, knjiga["ime_knjige"], knjiga["autor"]))
                        bibliotekar.glavni_meni()
                        postoji = True
                        return
                    else:
                        print("\nRashodovanje datog broja primeraka nije moguce, pokusajte ponovo.")
            if not postoji:
                print("\nUneli ste pogresan ID knjige.")
