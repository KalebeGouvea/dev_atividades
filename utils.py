from sqlalchemy import log
from models import Pessoas, Usuarios

#Insere dados na tabela pessoa
def insere_pessoa():
    pessoa = Pessoas(nome='Kalebe', idade=25)
    pessoa.save()

#Consulta dados na tabela pessoa, todos ou individualmente
def consulta_pessoa():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Gouvea').first()
    #print(pessoa)

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Kalebe').first()
    pessoa.nome = 'Gouvea'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Gouvea').first()
    pessoa.delete()

#Insere um novo usuário na tabela Usuários
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

#Consulta todos os usuários na tabela Usuários
def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoa()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoa()
    insere_usuario(login='admin', senha='321')
    insere_usuario(login='teste', senha='4321')
    consulta_usuarios()