from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

# Declarative base yang akan di-inherit oleh setiap model
Base = declarative_base()


class ModelKembali(Base):

    __tablename__  = 'tkembali'
    KodeKembali = Column(Integer, primary_key=True)
    KodeBuku = Column(Integer, ForeignKey("tbuku.KodeBuku"), nullable=False)
    NIM = Column(Integer, ForeignKey("tanggota.NIM"), nullable=False)
    TglKembali = Column(String(20), nullable=False)

    def __init__(self, KodeKembali, KodeBuku, NIM, TglKembali):
        self.KodeKembali = KodeKembali
        self.KodeBuku = KodeBuku
        self.NIM = NIM
        self.TglKembali = TglKembali

    def __repr__(self):
        return 'Kembali: {kodePinjam: %d, kodeBuku: %d, nim: %d, tanggalKembali: %s}' % \
               (self.kodePinjam, self.kodeBuku, self.nim, self.tanggalKembali)

class CRUD_Kembali:
    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self, kembali: ModelKembali):
        with Session(self.engine) as session:
            session.add(kembali)
            session.commit()

    def update(self, KodeKembali, newKembali: ModelKembali):
        with Session(self.engine) as session:
            the_kembali: ModelKembali = self.read_one(KodeKembali)
            the_kembali.kodeBuku = newKembali.kodeBuku
            the_kembali.nim = newKembali.nim
            the_kembali.tanggalKembali = newKembali.tanggalKembali
            session.add(the_kembali)
            session.commit()

    def delete(self, KodeKembali):
        with Session(self.engine) as session:
            the_kembali = self.read_one(KodeKembali)
            session.delete(the_kembali)
            session.commit()

    def read_one(self, KodeKembali):
        with Session(self.engine) as session:
            stmt = select(ModelKembali).where(ModelKembali.KodeKembali == KodeKembali)
            return session.scalars(stmt).one()