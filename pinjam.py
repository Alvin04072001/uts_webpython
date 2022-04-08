from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from anggota import ModelAnggota
from buku import ModelBuku

# Declarative base yang akan di-inherit oleh setiap model
Base = declarative_base()


class ModelPinjam(Base):

    __tablename__ = 'tpinjam'
    KodePinjam = Column(Integer, primary_key=True)
    KodeBuku = Column(Integer, ForeignKey(ModelBuku.KodeBuku), nullable=False)
    NIM = Column(Integer, ForeignKey(ModelAnggota.NIM), nullable=False)
    TglPinjam = Column(String(20), nullable=False)

    def __init__(self, KodePinjam, KodeBuku, NIM, TglPinjam):
        self.KodePinjam = KodePinjam
        self.KodeBuku = KodeBuku
        self.NIM = NIM
        self.TglPinjam = TglPinjam

    def __repr__(self):
        return 'Pinjaman: {kodePinjam: %d, kodeBuku: %d, nim: %d, tanggalPinjam: %s}' % \
               (self.kodePinjam, self.kodeBuku, self.nim, self.tanggalPinjam)


class CRUD_Pinjam:
    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self, pinjam: ModelPinjam):
        with Session(self.engine) as session:
            session.add(pinjam)
            session.commit()

    def update(self, kode_pinjam, newPinjaman: ModelPinjam):
        with Session(self.engine) as session:
            the_pinjaman: ModelPinjam = self.read_one(kode_pinjam)
            the_pinjaman.kodeBuku = newPinjaman.kodeBuku
            the_pinjaman.nim = newPinjaman.nim
            the_pinjaman.tanggalPinjam = newPinjaman.tanggalPinjam
            session.add(the_pinjaman)
            session.commit()

    def delete(self, kode_pinjam):
        with Session(self.engine) as session:
            the_pinjaman = self.read_one(kode_pinjam)
            session.delete(the_pinjaman)
            session.commit()

    def read(self):
        with Session(self.engine) as session:
            return session.query(ModelPinjam)

    def read_one(self, KodePinjam):
        with Session(self.engine) as session:
            stmt = select(ModelPinjam).where(ModelPinjam.kodePinjam == KodePinjam)
            return session.scalars(stmt).one()
