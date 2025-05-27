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
        return f"{self.nome} ({self.idade} anos) - CPF: {self.cpf}"


class Livro(BaseModel):
    nome = CharField()
    autor = CharField()
    categoria = CharField()

    def __str__(self):
        return f"{self.nome}, {self.autor} - ({self.categoria})"


class Emprestimo(BaseModel):
    estudante = ForeignKeyField(Estudante, backref='emprestimos')
    livro = ForeignKeyField(Livro, backref='emprestimos')
    data_emprestimo = DateField()
    data_devolucao = DateField(null=True)


db.connect()
db.create_tables([Estudante, Livro, Emprestimo])
