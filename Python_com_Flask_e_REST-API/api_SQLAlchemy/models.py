''' referenciar um tabela de banco '''
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# criação da base de dados >> nome do banco de dados 'atividades'
engine = create_engine('sqlite:///atividades.db',
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# Classe que gerencia a tabela pessoas
class Pessoas(Base):
    # nome da tabela 'pessoas' >> contendo id, nome e idade
    __tablename__ = 'pessoas'
    # chave primária
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # representação dos dados dos registro do banco
    def __repr__(self):
        return f'<ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}>'

    # salva novos dados na tabela
    def save(self):
        db_session.add(self)
        db_session.commit()

    # deleta registros na tabela
    def delete(self):
        db_session.delete(self)
        db_session.commit()


# classe que gerencia a tabela atividades
class Atividades(Base):
    # nome da tabela 'atividades' >> contendo id, nome, pessoa_id
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    status = Column(String(40))
    # chave estrangeira
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    # ligação com a tabela Pessoas
    pessoa = relationship("Pessoas")

    # representação dos dados dos registro do banco
    def __repr__(self):
        return f'<ID: {self.id}, Nome: {self.nome}, Status: {self.status}, Pessoa: {self.pessoa_id}>'

    # salva novos dados na tabela
    def save(self):
        db_session.add(self)
        db_session.commit()

    # deleta registros na tabela
    def delete(self):
        db_session.delete(self)
        db_session.commit()


# cadastro dos usuarios que poderão ter acesso aos registros >> autenticação
class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))
    status = Column(Boolean)

    def __repr__(self):
        return f'<Usuario: {self.login}, Ativo: {self.status}>'

    # salva novos dados na tabela
    def save(self):
        db_session.add(self)
        db_session.commit()

    # deleta registros na tabela
    def delete(self):
        db_session.delete(self)
        db_session.commit()


# cria banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
