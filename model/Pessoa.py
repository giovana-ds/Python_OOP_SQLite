class Pessoa:
  # atributos
  id = None
  nome = None

  # método construtor
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  # método para exibição
  def __str__(self):
    return f"{self.nome} ({self.id})"
