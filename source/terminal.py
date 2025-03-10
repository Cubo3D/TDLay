import os
from commands import commands_basic

os.system("cd TDLay\ environment")

while True:

    command = input(f"{commands_basic.user}@{commands_basic.hostname} ")

    if command == "newpas":
        commands_basic.newpas()

    elif command == "gg":
        commands_basic.pasta_antiga = os.getcwd()
        commands_basic.gg()

    elif command == "gg-":
        commands_basic.gg-()

    elif command == "remove":
        commands_basic.remove(input("caminho completo até o arquivo desde do disco C: até ele(ele é assim por mais segurança porque ele apaga de forma forçada e sem recuperação) "))

    elif command == "ar":
        commands_basic.ar()