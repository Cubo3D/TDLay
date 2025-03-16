import os

user = os.getlogin()
hostname = os.environ.get("COMPUTERNAME")

def newpas():
    pasta = input ("nome da nova pasta: ")
    os.mkdir(pasta)

    if not os.path.exists(pasta):
        os.mkdir(pasta)

    else:
        print(f"O diretório '{pasta}' já existe.")

def gg():
    os.chdir(input ("nome da pasta: "))

def ggh():
    os.system("cd TDLay Environment")

def gga():
    os.system("cd ..")

def remove(caminho):
    os.system(f'powershell -Command Remove-Item -Path "{caminho}" -Recurse -Force')

def ar():
    os.system('dir')
