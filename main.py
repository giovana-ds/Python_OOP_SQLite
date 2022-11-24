# importar Pessoa.py para diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# exemplo de uso
giovana = Pessoa(1, "Giovana Silveira")
print(giovana)

# mostrar só o nome
print(giovana.nome)

print("\nACESSO AO BANCO:\n")

# chamar o objeto do banco de dados
db = Database()

# instanciar o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

# carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

# criar um objeto com qualquer ator/atriz/diretor/diretora
  novo = Pessoa(0, "Denzel Washington")
  novo = pessoaDAO.save(novo)

# consultar o banco de novo
  pessoas = pessoaDAO.getAll(orderBy=True)
  for pessoa in pessoas:
    print(pessoa)
  