from .ui import login
from .ui import conta
from .ui import dashboard

rodando = True
usuario = None
tela = None

while rodando:
    if not usuario:
        usuario = login.tela_login()
        tela = None

    if tela == "q":
        usuario = None
    elif tela == "1":
        pass
    elif tela == "2":
        pass
    elif tela == "3":
        usuario = conta.tela_conta(usuario)
        tela = "0"
    else:
        tela = dashboard.tela_dashboard(usuario)
