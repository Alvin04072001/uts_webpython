from sqlalchemy import Column, String, Integer
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

Base = declarative_base()

# Inisialisasi kelas model anggota
class ModelAnggota(Base):

    __tablename__ = 'tanggota'
    NIM = Column(Integer, primary_key=True)
    NamaMhs = Column(String(60), nullable=False)
    Jurusan = Column(String(30), nullable=False)

    def __init__(self, NIM, NamaMhs, Jurusan):
        self.NIM = NIM
        self.NamaMhs = NamaMhs
        self.Jurusan = Jurusan

    def __repr__(self):
        return 'Anggota: {NIM: %d, NamaMhs: %s, Jurusan: %s}' % (self.NIM, self.NamaMhs, self.Jurusan)

# Kelas prosedur metode CRUD
class CRUD_Anggota:
    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self, anggota: ModelAnggota):
        with Session(self.engine) as session:
            session.add(anggota)
            session.commit()

    def read(self):
        with Session(self.engine) as session:
            return session.query(ModelAnggota)

    def update(self, NIM, anggota: ModelAnggota):
        with Session(self.engine) as session:
            the_anggota: ModelAnggota = self.read_one(NIM)
            the_anggota.nama = newAnggota.NamaMhs
            the_anggota.jurusan = newAnggota.Jurusan
            session.add(the_anggota)
            session.commit()

    def delete(self, NIM):
        with Session(self.engine) as session:
            anggota = self.read_one(NIM)
            session.delete(anggota)
            session.commit()

    def read_one(self, NIM):
        with Session(self.engine) as session:
            stmt = select(ModelAnggota).where(ModelAnggota.NIM == NIM)
            return session.scalars(stmt).one()
