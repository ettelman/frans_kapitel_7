## Läsa in binära filer

# with open('bild.png', 'rb') as file:
#     data = file.read()

# with open("ny_bild.png", 'wb') as new_file:
#     new_file.write(data)

# import argparse

# parser = argparse.ArgumentParser(description="Exempel verktyg")

# parser.add_argument("name", help="Här anger du ditt namn")
# parser.add_argument("age", type=int, help="Ange din ålder här")


# parser.add_argument("-c", "--city", help="Ange din stad", default="Okänd stad")
# # parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info")
# parser.add_argument("-m", "--mode", choices=["enkel", "detaljerad"], help="Välj läge")

# args = parser.parse_args()

# if args.mode == "detaljerad":
#     print(f"Hej {args.name}. Du är {args.age}. Du bor i {args.city}")
# else:
#     print(f"Hej {args.name}")

## Undantagshantering ##
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally:
#     print("Slut på try except")

# try:
#     with open("example.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("Fel: Filen finns inte!")
# except Exception as e:
#     print(f"Fel: {e}")


## Os-modulen ##

# import os

# os.chdir("c:\\users\\stefan")

# cwd = os.getcwd()
# print(cwd)

# os.mkdir('test_folder')
# os.rmdir('test_folder')

# if os.path.exists("example.txt"):
#     print("Filen existerar")
#     os.remove('example.txt')
# else:
#     print("Filen existerar inte")

# file_info = os.stat("bild.png")
# print(f"Filstorlek: {file_info.st_size}")

# os.system('dir')

# filepath = os.path.join("math_script", "main.py")
# print(filepath)

# with open(filepath, "r") as file:
    #kod

# import os
# import platform

# if os.name == "nt":
#     print("Windows!!")
#     os.system("dir")
# else:
#     print("Unix!")
#     os.system("ls")

# print(f"Plattform: {platform.system()}")