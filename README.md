# Corridinha

Este projeto tem como finalidade uma aplicação para que vários usuários possam se cadastrar e utilizar os recursos, os quais incluem cadastramento de treinos, competições, visualização, definição de metas e sugestão de treinos.

## Equipe

Realizadores:

* Bruno Santana dos Santos Araujo Holanda
* Eric Gonçalves Albuquerque
* João Guilherme Bezerra Omena Fragoso
* João Vitor Assumpção Passos
* Mircio Ferreira dos Santos Neto


Orientadoras:
* Izabella Nunes de Vasconcelos
* Ana Carolina Candido de Melo

## Ferramentas
Para o usuário utilizar a aplicação, as seguintes ferramentas serão necessárias:

* [Python](https://www.python.org/)
* [Interpretador (Recomenda-se o uso do VS Code)](https://code.visualstudio.com/)

### Preparando o ambiente

* Baixe o Python e o VS Code na máquina
* [Baixe os arquivos do Git em sua máquina e execute com o VS Code](https://github.com/iampassos/projeto-fp-cesar/archive/refs/heads/main.zip)

## Instruções de uso

0. Para iniciar a aplicação, abra com o VS Code na pasta onde contém todos os arquivos baixados do git, abra o terminal de comando e digite `python -m src.main.py`

1. Informe usuário e senha

   1.1. Caso não esteja cadastrado, cadastre um nome de usuário, e-mail e senha. (Obs: o e-mail deve conter "@" em algum lugar)

2. Após o login ser efetuado, aparecerá um terminal de comandos para o usuário digitar a funcionalidade que deseja usar.

   2.1. Comando [1]: [ **Treino e competições** ]: este comando serve para que o usuário possa visualizar, filtrar as visualizações, adicionar, remover treinos e sugerir treinos.

      2.1.1. Obs: O comando para alterar dados pode fazer de forma individual para cada um, caso o usúario diseje manter uma propriedade do treino inalterada, basta deixar o campo vazio e clicar na tecla 'Enter'.

      2.1.2 Obs: em 'Sugerir Treinos', o usuário deve digitar um valor maior que zero. Esse valor é uma porcentagem de dificuldade, a qual será utilizada como base para todo o histórico de treinos. Caso não existam treinos no banco de dados, ele usará um valor padrão!

   2.2. Comando [2]: [Metas]: Este comando serve para que o usuário informe uma meta que deseja cumprir. A aplicação irá calcular o progresso em relação à meta com base nos treinos cadastrados no mês atual.

   2.3. Comando [3]: [ **Gerenciamento de conta** ]: este comando serve para que o usuário possa atualizar senha, nome de cadastro e deletar a conta. Obs.: para que a conta seja deletada, o usuário deve digitar corretamente o seu nome cadastrado!


## Fluxograma

[Visualização do fluxograma pela plataforma Miro](https://miro.com/welcomeonboard/dm5FQTQ4TThRQXlYa2VJNUhEdUZrMjZIRm5saWlZdVlUWDl2Uk94OHdlVUhqSmQwUmR0OU5FRW9zSzVPczZQNXwzNDU4NzY0NTk4NTE3ODQ2MjIzfDI=?share_link_id=639727423592)
