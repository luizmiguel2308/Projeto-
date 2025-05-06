from peewee import *
db = SqliteDatabase('escola.db')

class BaseModel(Model):
    class Meta:
        database = db
        
        
class Estudante(BaseModel):
    nome = CharField()
    idade = IntegerField()
    cpf = CharField(unique=True)
    
    def __str__(self):
        return f"{self.nome} ( {self.idade} anos ) - CPF: {self.cpf}"
    
class Livro(BaseModel):
    nome = CharField()
    autor = CharField()
    categoria = CharField()
    
    def __str__(self):
        return f"{self.nome}, {self.autor} - ({self.categoria})"

class Emprestimo(BaseModel):
    data_emp = DateField()
    estudante = ForeignKeyField(Estudante)
    livro = ForeignKeyField(Livro)
    
    def __str__(self):
        return f" foi emprestado em {self.data_emp}, por: {self.estudante}, {self.livro}"
    
db.connect()
db.create_tables([Estudante, Livro, Emprestimo])
    



