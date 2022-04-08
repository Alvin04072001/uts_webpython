from sqlalchemy import Column, String, Integer
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

Base = declarative_base()

class ModelBuku(Base):

    __tablename__ = 'tbuku'
    KodeBuku = Column(Integer, primary_key=True)
    Judul = Column(String(50), nullable=False)
    Stok = Column(Integer, nullable=False)

    def __init__(self, KodeBuku, Judul, Stok):
        self.KodeBuku = KodeBuku
        self.Judul = Judul
        self.Stok = Stok

    def __repr__(self):
        return '[%d, %s, %d]' % \
               (self.KodeBuku, self.Judul, self.Stok)

class CRUD_Buku :
    def __init__(self, engine: Engine):
        self.engine = engine

    def create (self, buku: ModelBuku):
        with Session(self.engine) as session:
            session.add(buku)
            session.commit()

    def read (self):
        with Session(self.engine) as session:
            return session.query(ModelBuku)

    def update (self, KodeBuku, newBuku: ModelBuku):
        with Session(self.engine) as session:
            the_buku: ModelBuku = self.read_one(KodeBuku)
            the_buku.judulBuku = newBuku.JudulBuku
            the_buku.stok = newBuku.Stok
            session.add(the_buku)
            session.commit()

    def delete(self, KodeBuku):
        with Session(self.engine) as session:
            buku = self.read_one(KodeBuku)
            session.delete(buku)
            session.commit()

    def read_one(self, KodeBuku):
        with Session(self.engine) as session:
            stmt = select(ModelBuku).where(ModelBuku.KodeBuku == KodeBuku)
            return session.scalars(stmt).one()