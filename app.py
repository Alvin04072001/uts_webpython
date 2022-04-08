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

@app.route('/index')
def index():
        return render_template('index.html', container= buku.read())

@app.route('/datapinjambuku')
def datapinjambuku():
        return render_template('datapinjambuku.html', container= pinjam.read())

@app.route('/tambahbuku', methods=['GET','POST'])
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
def hapusbuku(KodeBuku):
        buku.delete(KodeBuku)
        return redirect(url_for('index'))

@app.route('/dataanggota')
def dataanggota():
        return render_template('dataanggota.html', container= anggota.read())

@app.route('/tambahanggota', methods= ['GET', 'POST'])
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

@app.route('/pinjam', methods= ['GET', 'POST'])
def pinjambuku():
        if request.method == 'POST':
                KodePinjam = request.form['kodepinjam']
                NIM = request.form['nim']
                KodeBuku = request.form['kodebuku']
                TglPinjam = request.form['tanggal']
                pinjambuku = ModelPinjam(NIM ,KodeBuku, TglPinjam)
                pinjam.create(pinjambuku)
                return redirect(url_for('datapinjambuku'))
        else:
                return render_template('pinjam_buku.html', buku_list = buku.read())

@app.route('/hapusanggota/<NIM>', methods=['GET','POST'])
def hapusanggota(NIM):
        anggota.delete(NIM)
        return redirect(url_for('dataanggota'))

@app.route('/ubahdata/<NIM>', methods=['GET', 'POST'])
def ubahdata(NIM):
        editData = anggota.read_one(NIM=NIM)
        if request.method == 'POST':
                editData.NIM = request.form['nim']
                editData.NamaMhs = request.form['namamhs']
                editData.Jurusan = request.form['jurusanmhs']
                anggota.update(NIM, editData)
                return redirect(url_for('index'))
        else:
                return render_template('editanggota.html')

if __name__ == '__main__':
        app.run(debug=True)

