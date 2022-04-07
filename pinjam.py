from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

# Declarative base yang akan di-inherit oleh setiap model
Base = declarative_base()


class PinjamanModel(Base):

    __tablename__ = 'tpinjaman'
    KodePinjam = Column(Integer, primary_key=True)
    KodeBuku = Column(Integer, ForeignKey("tbuku.KodeBuku"), nullable=False)
    NIM = Column(Integer, ForeignKey("tanggota.NIM"), nullable=False)
    TglPinjam = Column(String(20), nullable=False)

    def __init__(self, KodePinjam, KodeBuku, NIM, TglPinjam):
        self.KodePinjam = KodePinjam
        self.KodeBuku = KodeBuku
        self.NIM = NIM
        self.TglPinjam = TglPinjam

    def __repr__(self):
        return 'Pinjaman: {kodePinjam: %d, kodeBuku: %d, nim: %d, tanggalPinjam: %s}' % \
               (self.kodePinjam, self.kodeBuku, self.nim, self.tanggalPinjam)


class Pinjam_CRUD:
    def __init__(self, engine: Engine):
        self.engine = engine

    def create(self, pinjam: PinjamanModel):
        with Session(self.engine) as session:
            session.add(pinjam)
            session.commit()

    def update(self, kode_pinjam, newPinjaman: PinjamanModel):
        with Session(self.engine) as session:
            the_pinjaman: PinjamanModel = self.read_one(kode_pinjam)
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
            return session.query(PinjamanModel)

    def read_one(self, kode_pinjam):
        with Session(self.engine) as session:
            stmt = select(PinjamanModel).where(PinjamanModel.kodePinjam == kode_pinjam)
            return session.scalars(stmt).one()
