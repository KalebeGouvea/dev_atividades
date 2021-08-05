from models import Pessoas

#Insere dados na tabela pessoa
def insere_pessoa():
    pessoa = Pessoas(nome='Kalebe', idade=26)
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

if __name__ == '__main__':
    #insere_pessoa()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoa()