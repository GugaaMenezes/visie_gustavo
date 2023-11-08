from app import db

class PersonModels(db.Model):
    __tablename__ = 'pessoas'
    id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    rg = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    funcao = db.Column(db.String(100))
    
    def __init__(self, nome, rg, cpf, data_nascimento, data_admissao, funcao=None):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.data_admissao = data_admissao
        self.funcao = funcao
        
        
            
    def serialize(self):
        return {
            'id_pessoa': self.id_pessoa,
            'nome': self.nome,
            'rg': self.rg,
            'cpf': self.cpf,
            'data_nascimento': self.data_nascimento.strftime("%d/%m/%Y %H:%M:%S"),
            'data_admissao': self.data_admissao.strftime("%d/%m/%Y %H:%M:%S"),
            'funcao': self.funcao
        }
