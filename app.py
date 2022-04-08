from flask import Flask, render_template, request,\
        flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from anggota import *
from pinjam import *
from kembali import *
from buku import *

engine = create_engine("mysql://root:@localhost/dbperpustakaan")
app = Flask(__name__)

buku = CRUD_Buku(engine)
anggota = CRUD_Anggota(engine)
pinjam = CRUD_Pinjam(engine)
kembali = CRUD_Kembali(engine)

@app.route('/')
# Menampilkan data buku
def index():
        return render_template('index.html', container= buku.read())

@app.route('/tambahbuku', methods=['GET','POST'])
# Menambah data buku
def tambahbuku():
        if request.method == 'POST':
                KodeBuku = request.form['kbuku']
                Judul = request.form['jbuku']
                Stok = request.form['sbuku']
                tambah = ModelBuku(KodeBuku, Judul, Stok)
                buku.create(tambah)
                return redirect(url_for('index'))
        else:
                return render_template('tambahbuku.html')

@app.route('/hapusbuku/<KodeBuku>', methods=['GET','POST'])
# Menghapus data buku
def hapusbuku(KodeBuku):
        buku.delete(KodeBuku)
        return redirect(url_for('index'))

@app.route('/dataanggota')
# Menampilkan data anggota
def dataanggota():
        return render_template('dataanggota.html', container= anggota.read())

@app.route('/tambahanggota', methods= ['GET', 'POST'])
# Menambah data anggota
def tambahanggota():
        if request.method == 'POST':
                NIM = request.form['nim']
                NamaMhs = request.form['namamhs']
                Jurusan = request.form['jurusanmhs']
                tambah = ModelAnggota(NIM, NamaMhs, Jurusan)
                anggota.create(tambah)
                return redirect(url_for('dataanggota'))
        else:
                return render_template('tambahanggota.html')

@app.route('/hapusanggota/<NIM>', methods=['GET','POST'])
# Menghapus data anggota
def hapusanggota(NIM):
        anggota.delete(NIM)
        return redirect(url_for('dataanggota'))

@app.route('/dataanggota/ubahanggota/<NIM>', methods=['POST'])
def ubahanggota(NIM):
    the_anggota: ModelPinjam = CRUD_Anggota.read_one(NIM)
    nim = request.form['nim']
    the_anggota.NIM = nim
    CRUD_Anggota.update(NIM, the_anggota)
    return redirect(url_for('datapinjambuku'))

if __name__ == '__main__':
        app.run(debug=True)

