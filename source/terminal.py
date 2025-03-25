import os
import time
from commands import commands_basic

print("Bem vindo ao Cair, o emulador de terminal totalemnte diferente(ou uma imitação de SO(Sistema Operacional) escrito em python)!")
print("Todos os comandos no README.md")



while True:

    command = input(f"{commands_basic.user}@{commands_basic.hostname} ")

    match command:

        case "newpas":
            commands_basic.newpas()

        case "gg":
            commands_basic.gg()

        case "gg-":
            commands_basic.gga()

        case "remove-f":
            commands_basic.removef(input("caminho completo até o arquivo desde do disco C: até ele(ele é assim por mais segurança porque ele apaga de forma forçada e sem recuperação) "))

        case "ar":
            commands_basic.ar()

        case "exit":
            print("Tchau! Erro encontrado? Aqui: https://github.com/Cubo3D/Cair/issues/new")
            time.sleep(2)
            break

        case _:
            print(f"Raish: {command}: Comando não encontrado")
