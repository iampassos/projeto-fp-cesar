class Usuario:
    """
    Classe que representa um usuário com nome, e-mail e senha.

    Atributos:
        nome (str): O nome do usuário.
        email (str): O e-mail do usuário.
        senha (str): A senha do usuário.
    """

    def __init__(self, nome: str, email: str, senha: str) -> None:
        """
        Construtor da classe Usuario.

        Argumentos:
            nome (str): O nome do usuário.
            email (str): O e-mail do usuário.
            senha (str): A senha do usuário.
        """
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self) -> str:
        """
        Retorna uma representação da classe Usuario como string.

        Retorna:
            str: A representação do usuário no formato 'nome, email, senha'.

        Exemplo de uso:
            str(usuario_obj)
        """
        return f"{self.nome}, {self.email}, {self.senha}"
