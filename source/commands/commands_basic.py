import os

user = "none"
hostname = "none"

def newpas():
    pasta = input ("nome da nova pasta: ")

    if not os.path.exists(pasta):
        os.mkdir(pasta)

    else:
        print(f"A pasta: '{pasta}' já existe.")

def gg():
    os.chdir(input ("nome da pasta: "))

def gga():
    os.system("cd ..")

def removef(caminho):
    os.system(f'powershell -Command Remove-Item -Path "{caminho}" -Recurse -Force')

def ar():
    os.system('dir')
