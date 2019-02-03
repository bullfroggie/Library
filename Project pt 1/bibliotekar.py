"""
Module with functions dedicated to
manipulating data as a librarian
"""

import datetime
import src.knjige as knj
import src.podaci_bibliotekara as bibliotekari
import src.podaci_korisnici as korisnici
import src.podaci_zaduzenja as zaduzenja
import src.podaci_knjige as knjige

trenutno_prijavljen = []


def prikaz_korisnika():
    # Function for printing all of the librarians from the podaci_korisnici.py file

    print("{:^180}".format("Korisnici\n"))
    for korisnik in korisnici.korisnici:
        print("| Clanska karta: {} |"
              "\t\t Ime: {:>7} \t\t|"
              "\t\t Prezime: {:>10} \t\t|"
              "\t\t Izbrisan: {:>10} \t\t|"
              "\t\t Korisnicko ime: {:>20} \t\t|"
              "\t\t Lozinka: {:>10}".format(korisnik["clanska_karta"],
                                            korisnik["ime"],
                                            korisnik["prezime"],
                                            str(korisnik["izbrisan"]),
                                            korisnik["korisnicko_ime"],
                                            korisnik["lozinka"]))


def prikaz_bibliotekara():
    # Function for printing all of the librarians from the podaci_bibliotekara.py file

    print("{:^178}".format("Bibliotekari\n"))
    for bibliotekar in bibliotekari.bibliotekari:
        print("| ID: {} |"
              "\t\t Ime: {:>7} \t\t|"
              "\t\t Prezime: {:>10} \t\t|"
              "\t\t Korisnicko ime: {:>25} \t\t|"
              "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                  bibliotekar["ime"],
                                                  bibliotekar["prezime"],
                                                  bibliotekar["korisnicko_ime"],
                                                  bibliotekar["lozinka"]))


def prijava_bibliotekar():
    # Login system for librarians
    # If login is successful, the librarian ..
    # is presented with the librarian-dedicated main menu

    trenutno_prijavljen.clear()

    prijavljen = False
    while not prijavljen:
        korisnicko_ime = input("\nKorisnicko ime: ")
        lozinka = input("\nLozinka: ")

        for bibliotekar in bibliotekari.bibliotekari:
            if korisnicko_ime == bibliotekar["korisnicko_ime"] and \
                    lozinka == bibliotekar["lozinka"]:
                print(f"\nUspesno ste se prijavili kao bibliotekar - {bibliotekar['ime']} {bibliotekar['prezime']}")
                trenutno_prijavljen.append(korisnicko_ime)
                glavni_meni()
                prijavljen = True
        if not prijavljen:
            print("\nPogresno korisnicko ime ili lozinka.\n")
            return


def glavni_meni():
    # Function for the librarian's main menu
    # It gives the user a set of options that only librarians ..
    # can access when logged in
    # User then picks the sequential number of the option he wants to use
    # After which the according function is triggered

    while True:
        print("\nGLAVNI MENI\n\n"
              "1) Unos i izmena podataka o Knjigama\n"
              "2) Unos podataka za Bibliotekara i Korisnika\n"
              "3) Izmena podataka trenutno prijavljenog Bibliotekara\n"
              "4) Zaduživanje i razduživanje Korisnika\n"
              "5) Rashodovanje knjiga\n"
              "6) Brisanje Korisnika\n"
              "\nDa biste se odjavili i izasli iz programa, unesite \"q\"")

        izbor = input("\nIzaberite akciju: ")

        if izbor == "1":
            print("\nUNOS I IZMENA PODATAKA O KNJIGAMA")
            print("---------------------------------\n")
            print("1) Dodavanje nove knjige\n"
                  "2) Izmena knjige\n"
                  "3) Brisanje knjige\n")

            izbor1 = input("Izaberite akciju: ")
            if izbor1 == "1":
                knj.dodavanje_knjige()
            elif izbor1 == "2":
                knj.izmena_knjige()
            elif izbor1 == "3":
                knj.brisanje_knjige()
            else:
                print("\nNiste uneli dobar redni broj.")

        elif izbor == "2":
            print("\nUNOS PODATAKA ZA BIBLIOTEKARA I KORISNIKA")
            print("-----------------------------------------\n")
            print("1) Bibliotekar\n"
                  "2) Korisnik\n")

            izbor2 = input("Izaberite akciju: ")
            if izbor2 == "1":
                print("\nUNOS, BRISANJE ILI IZMENA BIBLIOTEKARA")
                print("--------------------------------------\n")
                print("1) Unos\n"
                      "2) Brisanje\n")
                izbor21 = input("Izaberite akciju: ")
                if izbor21 == "1":
                    dodavanje_bibliotekara()
                elif izbor21 == "2":
                    brisanje_bibliotekara()
                else:
                    print("\nNiste uneli dobar redni broj.")
            elif izbor2 == "2":
                print("\nUNOS, BRISANJE ILI IZMENA KORISNIKA")
                print("-----------------------------------\n")
                print("1) Unos\n"
                      "2) Izmena")
                izbor22 = input("\nIzaberite akciju: ")
                if izbor22 == "1":
                    dodavanje_korisnika()
                elif izbor22 == "2":
                    izmena_korisnika()
                else:
                    print("\nNiste uneli dobar redni broj.")
        elif izbor == "3":
            print("\nIZMENA PODATAKA TRENUTNO PRIJAVLJENOG BIBLIOTEKARA\n")
            izmena_bibliotekara()
        elif izbor == "4":
            print("\nZADUZIVANJE I RAZDUZIVANJE KORISNIKA")
            print("------------------------------------\n")
            print("1) Zaduzivanje\n"
                  "2) Razduzivanje\n")
            izbor41 = input("Izaberite akciju: ")
            if izbor41 == "1":
                print("\nZaduzivanje\n")
                zaduzivanje()
            elif izbor41 == "2":
                print("\nRazduzivanje\n")
                razduzivanje()
        elif izbor == "5":
            print("\nRASHODOVANJE KNJIGA\n")
            knj.rashodovanje()
        elif izbor == "6":
            print("\nBRISANJE KORISNIKA\n")
            brisanje_korisnika()
        elif izbor == "q":
            print("\nUspesno ste se odjavili.")
            return False
        else:
            print("\nNiste uneli dobar redni broj.")


def dodavanje_bibliotekara():
    # Function for adding new librarians to the system

    prikaz_bibliotekara()

    postoji = True
    novi_bibliotekar = {}
    id_od_svih_bibliotekara = []
    korisnicko_od_svih_bib = []

    for bibliotekar in bibliotekari.bibliotekari:
        id_od_svih_bibliotekara.append(bibliotekar["id"])
        korisnicko_od_svih_bib.append(bibliotekar["korisnicko_ime"])

    while postoji:
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            id_bibliotekara = int(input("\nUnesite ID bibliotekara: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.")
        else:
            if id_bibliotekara == 1:
                return False
            try:
                korisnicko_ime = input('\nKorisnicko ime: ')
                if not korisnicko_ime:
                    raise ValueError
            except ValueError:
                print("\nMorate nesto uneti!\n")
            else:

                if id_bibliotekara not in id_od_svih_bibliotekara and \
                        korisnicko_ime not in korisnicko_od_svih_bib:
                    postoji = False

                    lozinka = input('Lozinka: ')
                    ime = input('Ime: ')
                    prezime = input('Prezime: ')

                    novi_bibliotekar['id'] = id_bibliotekara
                    novi_bibliotekar['ime'] = ime
                    novi_bibliotekar['prezime'] = prezime
                    novi_bibliotekar['korisnicko_ime'] = korisnicko_ime
                    novi_bibliotekar['lozinka'] = lozinka
                    bibliotekari.bibliotekari.append(novi_bibliotekar)

                    prikaz_bibliotekara()
                    return
            if postoji:
                print("\nUneti ID ili korisnicko ime vec postoje. Pokusajte ponovo.\n")


def brisanje_bibliotekara():
    # Function for deleting librarians from the system
    # Firstly searching for the librarian by ID
    # After the librarian is picked/found, the user can delete him/her

    while True:
        prikaz_bibliotekara()
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            pretraga = int(input("\nUnesite ID od bibliotekara kog zelite da izbrisete: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.")
        else:
            if pretraga == 1:
                return False
            for bibliotekar in bibliotekari.bibliotekari:
                if pretraga == bibliotekar["id"]:
                    bibliotekari.bibliotekari.remove(bibliotekar)
                    prikaz_bibliotekara()
                    return False
            print("\nUneli ste nepostojeci ID, pokusajte ponovo.")


def dodavanje_korisnika():
    # Function for adding new users to the system

    prikaz_korisnika()

    postoji = True
    novi_korisnik = {}
    ck_od_svih_korisnika = []
    korisnicko_od_svih_k = []

    for ck in korisnici.korisnici:
        ck_od_svih_korisnika.append(ck["clanska_karta"])
        korisnicko_od_svih_k.append(ck["korisnicko_ime"])

    while postoji:
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            ck_korisnika = int(input("\nUnesite broj clanske karte: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.\n")
        else:
            if ck_korisnika == 1:
                return False
            korisnicko_ime = input("Korisnicko ime: ")
            if ck_korisnika not in ck_od_svih_korisnika and \
                    korisnicko_ime not in korisnicko_od_svih_k:
                postoji = False

                ime = input("Ime: ")
                prezime = input("Prezime: ")
                lozinka = input("Lozinka: ")

                novi_korisnik["clanska_karta"] = ck_korisnika
                novi_korisnik["ime"] = ime
                novi_korisnik["prezime"] = prezime
                novi_korisnik["izbrisan"] = False
                novi_korisnik["korisnicko_ime"] = korisnicko_ime
                novi_korisnik["lozinka"] = lozinka
                korisnici.korisnici.append(novi_korisnik)

                prikaz_korisnika()
                return
        if postoji:
            print("\nKoriscniko ime ili clanska karta vec postoje.\n")


def brisanje_korisnika():
    # Function for deleting users from the system
    # After the users are printed out, the librarian can ..
    # filter out the one due for deletion with the user's membership card number
    # After the user is picked out, he can be deleted (deletion status changed from False => True) *bool

    while True:
        svi_korisnici = []
        izabran = []
        br_zaduzenja = 0
        r_b = 0
        provera = False
        for korisnik in korisnici.korisnici:
            if not korisnik["izbrisan"]:
                r_b += 1
                svi_korisnici.append(korisnik)
                print("{}  | Clanska karta: {} |"
                      "\t\t Ime: {:>7} \t\t|"
                      "\t\t Prezime: {:>10} \t\t|"
                      "\t\t Korisnicko ime: {:>10} \t\t|"
                      "\t\t Lozinka: {:>15} \t\t|"
                      "\t\t Izbrisan: {}".format(r_b,
                                                 korisnik["clanska_karta"],
                                                 korisnik["ime"],
                                                 korisnik["prezime"],
                                                 korisnik["korisnicko_ime"],
                                                 korisnik["lozinka"],
                                                 korisnik["izbrisan"]))
                provera = True
        if not provera:
            print("\nSvi korisnici su zaduzeni!\n")
            continue
        try:
            selekcija = int(input("\nUnesite redni broj korisnika za brisanje: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj!\n")
        else:
            proveren = False
            for korisnik in range(len(svi_korisnici)):
                if selekcija == korisnik + 1:
                    izabran.append(svi_korisnici[korisnik]["clanska_karta"])
                    proveren = True
            if not proveren:
                print("\nUneli ste nepostojeci redni broj!\n")
                continue
            for zaduzenje in zaduzenja.zaduzenja:
                if izabran[0] == zaduzenje["clanska_karta"]:
                    if zaduzenje["datum_razduzivanja"] == "/":
                        br_zaduzenja += 1
                    else:
                        pass
            za_brisanje = False
            for korisnik in korisnici.korisnici:
                if br_zaduzenja == 0:
                    if korisnik["clanska_karta"] == izabran[0]:
                        korisnik["izbrisan"] = True
                        za_brisanje = True
            if not za_brisanje:
                print("\nKorisnika nije moguce obrisati. Zaduzen je.\n")
                continue
            return False


def izmena_korisnika():
    # Function for editing user related data
    # Initial search for the user by his/her membership card number
    # After the user has been found, his data can be edited

    pronadjen = False
    while not pronadjen:
        prikaz_korisnika()
        print("\n(hint) Za povratak na glavni meni unesite br. 1")
        try:
            pretraga = int(input("Unesite broj clanske karte od korisnika kog zelite da izmenite: "))
        except (ValueError, TypeError):
            print("\nMorate uneti broj.\n")
        else:
            if pretraga == 1:
                return False
            for korisnik in korisnici.korisnici:
                if pretraga == korisnik["clanska_karta"]:
                    pronadjen = True
                    print("\nIzaberite opciju za izmenu:\n\n"
                          "1) Ime\n"
                          "2) Prezime\n"
                          "3) Korisnicko ime\n"
                          "4) Lozinka\n ")
                    while True:
                        promena = input("Unesite redni broj: ")
                        if promena == "1":
                            novo_ime = input("Novo Ime: ")
                            korisnik["ime"] = novo_ime
                            prikaz_korisnika()
                            print("\nIme korisnika promenjeno u {}.".format(novo_ime))
                            glavni_meni()
                            return False
                        elif promena == "2":
                            novo_prezime = input("Novo Prezime: ")
                            korisnik["prezime"] = novo_prezime
                            prikaz_korisnika()
                            print("\nIzmenjeno prezime za korisnika - {},  u {}."
                                  .format(korisnik["ime"], novo_prezime))
                            glavni_meni()
                            return False
                        elif promena == "3":
                            novo_korisnicko_ime = input("Novo Korisnicko Ime: ")
                            korisnik["korisnicko_ime"] = novo_korisnicko_ime
                            prikaz_korisnika()
                            print("\nKorisnicko ime za korisnika - {} {},  izmenjeno u {}."
                                  .format(korisnik["ime"],
                                          korisnik["prezime"],
                                          novo_korisnicko_ime))
                            glavni_meni()
                            return False
                        elif promena == "4":
                            nova_lozinka = input("Nova lozinka: ")
                            korisnik["lozinka"] = nova_lozinka
                            prikaz_korisnika()
                            print("\nLozinka izmenjena!")
                            glavni_meni()
                            return False
                        else:
                            print("\nUneli ste nepostojeci redni broj.")
            if not pronadjen:
                print("\nUneli ste nepostojecu clansku kartu, pokusajte ponovo.\n")


def izmena_bibliotekara():
    # Function for editing the currently signed in librarian's data

    for bibliotekar in bibliotekari.bibliotekari:
        if trenutno_prijavljen[0] == bibliotekar["korisnicko_ime"]:
            print("| ID: {} |"
                  "\t\t Ime: {:>7} \t\t|"
                  "\t\t Prezime: {:>10} \t\t|"
                  "\t\t Korisnicko ime: {:>10} \t\t|"
                  "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                      bibliotekar["ime"],
                                                      bibliotekar["prezime"],
                                                      bibliotekar["korisnicko_ime"],
                                                      bibliotekar["lozinka"]))
            print("\nIzaberite opciju za izmenu:\n\n"
                  "1) Ime\n"
                  "2) Prezime\n"
                  "3) Korisnicko ime\n"
                  "4) Lozinka\n\n\n"
                  "5) Izadji ")
            promena = input("Unesite redni broj: ")
            if promena == "1":
                novo_ime = input("Novo Ime: ")
                bibliotekar["ime"] = novo_ime
                print("| ID: {} |"
                      "\t\t Ime: {:>7} \t\t|"
                      "\t\t Prezime: {:>10} \t\t|"
                      "\t\t Korisnicko ime: {:>10} \t\t|"
                      "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                          bibliotekar["ime"],
                                                          bibliotekar["prezime"],
                                                          bibliotekar["korisnicko_ime"],
                                                          bibliotekar["lozinka"]))
                print("\nIme bibliotekara promenjeno u {}.".format(novo_ime))
                glavni_meni()
                return
            elif promena == "2":
                novo_prezime = input("Novo Prezime: ")
                bibliotekar["prezime"] = novo_prezime
                print("| ID: {} |"
                      "\t\t Ime: {:>7} \t\t|"
                      "\t\t Prezime: {:>10} \t\t|"
                      "\t\t Korisnicko ime: {:>10} \t\t|"
                      "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                          bibliotekar["ime"],
                                                          bibliotekar["prezime"],
                                                          bibliotekar["korisnicko_ime"],
                                                          bibliotekar["lozinka"]))
                print("\nIzmenjeno prezime za bibliotekara - {},  u {}.".format(bibliotekar["ime"], novo_prezime))
                return
            elif promena == "3":
                novo_korisnicko_ime = input("Novo Korisnicko Ime: ")
                bibliotekar["korisnicko_ime"] = novo_korisnicko_ime
                print("| ID: {} |"
                      "\t\t Ime: {:>7} \t\t|"
                      "\t\t Prezime: {:>10} \t\t|"
                      "\t\t Korisnicko ime: {:>10} \t\t|"
                      "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                          bibliotekar["ime"],
                                                          bibliotekar["prezime"],
                                                          bibliotekar["korisnicko_ime"],
                                                          bibliotekar["lozinka"]))
                print("\n\nKorisnicko ime za bibliotekara - {} {},  izmenjeno u {}.".format(bibliotekar["ime"],
                                                                                            bibliotekar["prezime"],
                                                                                            novo_korisnicko_ime))
                return
            elif promena == "4":
                nova_lozinka = input("Nova lozinka: ")
                bibliotekar["lozinka"] = nova_lozinka
                print("\n| ID: {} |"
                      "\t\t Ime: {:>7} \t\t|"
                      "\t\t Prezime: {:>10} \t\t|"
                      "\t\t Korisnicko ime: {:>10} \t\t|"
                      "\t\t Lozinka: {:>15} \t\t|".format(bibliotekar["id"],
                                                          bibliotekar["ime"],
                                                          bibliotekar["prezime"],
                                                          bibliotekar["korisnicko_ime"],
                                                          bibliotekar["lozinka"]))
                print("\nLozinka izmenjena!")
                return
            elif promena == "5":
                print("\nPovratak na glavni meni.")
                return
            else:
                print("\nUneli ste nepostojeci broj. Program ce biti prekinut.")


def zaduzivanje():
    # Function for book obligation
    # 1. Search for the book to obligate
    # 2. Pick a book
    # 3. Search for the user
    # 4. Pick a user
    # Final: obligate the selected book under the selected user

    while True:
        zapamti_korisnike = []
        zapamti_knjige = []
        za_zaduzivanje_knjiga = []
        za_zaduzivanje_korisnik = []
        novo_zaduzenje = {}

        vreme = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        r_b = 0

        print("\nPretraga knjiga")
        print("---------------\n")
        try:
            pretraga = input("Pretraga: ")
            if not pretraga:
                raise ValueError
        except ValueError:
            print("\nMorate uneti nesto!")
        else:
            pronadjena = False
            for knjiga in knjige.knjige:
                if pretraga == str(knjiga["id"]) or \
                        pretraga.lower() in knjiga["ime_knjige"].lower() or \
                        pretraga.lower() in knjiga["autor"].lower() or \
                        pretraga == str(knjiga["god_izd"]):
                    pronadjena = True
                    r_b += 1
                    zapamti_knjige.append(knjiga)
                    print(" {} | ID: {} |\t\t Autor: {:>25} \t\t|"
                          "\t\t Ime knjige: {:>25} \t\t|"
                          "\t\t Godina izdavanja: {} \t\t|"
                          "\t\t Ukupan br. primeraka: {} \t\t|"
                          "\t\t Br. slobodnih primeraka: {} \t\t|".format(r_b,
                                                                          knjiga["id"],
                                                                          knjiga["autor"],
                                                                          knjiga["ime_knjige"],
                                                                          knjiga["god_izd"],
                                                                          knjiga["ukupan_br_prim"],
                                                                          knjiga["br_slob_prim"]))
            if not pronadjena:
                print("\nKnjiga koju trazite ne postoji. Pokusajte ponovo.")
                continue
            try:
                selekcija = int(input("\nUnesite redni broj knjige: "))
            except (ValueError, TypeError):
                print("\nMorate uneti broj.")
            else:
                izabrana = False
                for knjiga in range(len(zapamti_knjige)):
                    if selekcija == knjiga + 1:
                        za_zaduzivanje_knjiga.append(zapamti_knjige[knjiga])
                        izabrana = True
                        break
                if not izabrana:
                    print("\nUneli ste nepostojeci redni broj.\n")
                    continue
            while True:
                r_b = 0
                print("\nPretraga korisnika")
                print("---------------\n")
                try:
                    pretraga = input("Pretraga: ")
                    if not pretraga:
                        raise ValueError
                except ValueError:
                    print("\nMorate uneti nesto!")
                else:
                    pronadjen = False
                    for korisnik in korisnici.korisnici:
                        if not korisnik["izbrisan"] and pretraga == str(korisnik["clanska_karta"]) or \
                                not korisnik["izbrisan"] and pretraga.lower() in korisnik["ime"].lower() or \
                                not korisnik["izbrisan"] and pretraga.lower() in korisnik["prezime"].lower() or \
                                not korisnik["izbrisan"] and pretraga in korisnik["korisnicko_ime"]:
                            pronadjen = True
                            r_b += 1
                            zapamti_korisnike.append(korisnik)
                            print("{}  | Clanska karta: {} |"
                                  "\t\t Ime: {:>7} \t\t|"
                                  "\t\t Prezime: {:>10} \t\t|"
                                  "\t\t Korisnicko ime: {:>10} \t\t|"
                                  "\t\t Lozinka: {:>15} \t\t|".format(r_b,
                                                                      korisnik["clanska_karta"],
                                                                      korisnik["ime"],
                                                                      korisnik["prezime"],
                                                                      korisnik["korisnicko_ime"],
                                                                      korisnik["lozinka"]))
                    if not pronadjen:
                        print("\nKorisnik nije pronadjen!\n")
                        continue
                    izabran = False
                    try:
                        selekcija = int(input("\nSelektujte korisnika na osnovu rednog broja: "))
                    except (ValueError, TypeError):
                        print("Morate uneti broj.\n")
                    else:
                        for korisnik in range(len(zapamti_korisnike)):
                            if selekcija == korisnik + 1:
                                za_zaduzivanje_korisnik.append(zapamti_korisnike[korisnik])
                                izabran = True
                                break
                        if not izabran:
                            print("\nUneli ste nepostojeci redni broj.\n")
                            continue
                        slobodna = False
                        for knjiga in za_zaduzivanje_knjiga:
                            novo_zaduzenje["id_knjige"] = knjiga["id"]
                            for knjiga1 in knjige.knjige:
                                if knjiga["id"] == knjiga1["id"]:
                                    if knjiga1["br_slob_prim"] > 0:
                                        slobodna = True
                                        knjiga1["br_slob_prim"] -= 1
                                        break
                        if not slobodna:
                            print("\nKnjigu nije moguce zaduziti. Nema slobodnih primeraka.")
                            zaduzivanje()
                            break
                        for korisnik in za_zaduzivanje_korisnik:
                            novo_zaduzenje["clanska_karta"] = korisnik["clanska_karta"]
                            novo_zaduzenje["datum_zaduzivanja"] = vreme
                            novo_zaduzenje["datum_razduzivanja"] = "/"
                            zaduzenja.zaduzenja.append(novo_zaduzenje)
                        return False
                    break


def razduzivanje():
    # Function for book discharging
    # 1. Search for the book to discharge
    # 2. Pick a book
    # 3. Search for the user
    # 4. Pick a user
    # Final: discharge the selected book under the selected user

    while True:
        svi_korisnici = []
        izabran = []
        sva_zaduzenja = []
        izabrano = []
        vreme = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        r_b = 0
        try:
            pretraga = input("Pretraga korisnika: ")
            if not pretraga:
                raise ValueError
        except ValueError:
            print("\nMorate uneti nesto!\n")
        else:
            pronadjen = False
            for korisnik in korisnici.korisnici:
                if not korisnik["izbrisan"] and pretraga == str(korisnik["clanska_karta"]) or \
                        not korisnik["izbrisan"] and pretraga.lower() in korisnik["ime"].lower() or \
                        not korisnik["izbrisan"] and pretraga.lower() in korisnik["prezime"].lower() or \
                        not korisnik["izbrisan"] and pretraga in korisnik["korisnicko_ime"]:
                    pronadjen = True
                    r_b += 1
                    svi_korisnici.append(korisnik)
                    print("{}  | Clanska karta: {} |"
                          "\t\t Ime: {:>7} \t\t|"
                          "\t\t Prezime: {:>10} \t\t|"
                          "\t\t Korisnicko ime: {:>10} \t\t|"
                          "\t\t Lozinka: {:>15} \t\t|".format(r_b,
                                                              korisnik["clanska_karta"],
                                                              korisnik["ime"],
                                                              korisnik["prezime"],
                                                              korisnik["korisnicko_ime"],
                                                              korisnik["lozinka"]))
            if not pronadjen:
                print("\nKorisnik nije pronadjen. Pokusajte ponovo.\n")
                continue
            r_b = 0
            try:
                selekcija = int(input("Unesite redni broj: "))
            except (ValueError, TypeError):
                print("\nMorate uneti broj!\n")
            else:
                proveren = False
                for korisnik in range(len(svi_korisnici)):
                    if selekcija == korisnik + 1:
                        izabran.append(svi_korisnici[korisnik])
                        for zaduzenje in zaduzenja.zaduzenja:
                            if svi_korisnici[korisnik]["clanska_karta"] == zaduzenje["clanska_karta"] and \
                                    zaduzenje["datum_razduzivanja"] == "/":
                                proveren = True
                                r_b += 1
                                sva_zaduzenja.append(zaduzenje)
                                print(" {} | ID knjige: {} |\t\t Clanska karta: {} \t\t|"
                                      "\t\t Datum zaduzivanja: {:>5} \t\t|".format(r_b,
                                                                                   zaduzenje["id_knjige"],
                                                                                   zaduzenje["clanska_karta"],
                                                                                   zaduzenje["datum_zaduzivanja"]))
                if not proveren:
                    print("\nKorisnik nema nikakva zaduzenja.\n")
                    return False
                try:
                    izbor = int(input("Unesite redni broj: "))
                except (ValueError, TypeError):
                    print("\nMorate uneti broj!\n")
                else:
                    provereno = False
                    for zaduzenje in range(len(sva_zaduzenja)):
                        if izbor == zaduzenje + 1:
                            provereno = True
                            izabrano.append(sva_zaduzenja[zaduzenje])
                    if not provereno:
                        print("\nUneli ste nepostojeci redni broj!\n")
                        continue

                    for zaduzenje in zaduzenja.zaduzenja:
                        for raz in izabrano:
                            if raz["id_knjige"] == zaduzenje["id_knjige"] and \
                                    raz["clanska_karta"] == zaduzenje["clanska_karta"]:
                                zaduzenje["datum_razduzivanja"] = vreme
                                break
                    for knjiga in knjige.knjige:
                        for raz in izabrano:
                            if raz["id_knjige"] == knjiga["id"]:
                                knjiga["br_slob_prim"] += 1
                                break
                    return False

