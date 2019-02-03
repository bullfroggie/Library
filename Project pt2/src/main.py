"""
    Library Service Project 1st year - Programming Fundamentals
    -Singidunum University-

    By: Nikola Lausev
    --------------------------------
    This project is an implementation of a console-based app
    that represents a library system for handling books, users,
    and librarians.

    The program should be run from this module.

    Comments are in English - everything else is in Serbian
"""

import src.bibliotekar as bibliotekar
import src.korisnik as korisnik


def prijava_na_sistem():
    # Login system for users and librarians
    # After login, the user/librarian is granted access to their dedicated main menu

    while True:
        print("\nNARODNA BIBLIOTEKA SRBIJE\n"
              "-------------------------\n")
        print("Izbor za prijavu na sistem")
        print("\n1) Korisnik\n2) Bibliotekar\n\nq) Odustani\n")
        prijava = input("Prijavite se kao: ")

        if prijava == "1":
            print("\nPrijava - Korisnik\n"
                  "------------------")
            korisnik.prijava_korisnik()
        elif prijava == "2":
            print("\nPrijava - Bibliotekar\n"
                  "---------------------")
            bibliotekar.prijava_bibliotekar()
        elif prijava == "q":
            print("\nOdustali ste od prijave i izasli iz programa.")
            return False
        else:
            print("\nVas unos nije validan. Pokusajte ponovo.\n")


prijava_na_sistem()
