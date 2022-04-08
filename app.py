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
def index():
        return render_template('index.html', container= buku.read())

@app.route('/dataanggota')
def dataanggota():
        return render_template('dataanggota.html', container= anggota.read())

# @app.route('/editanggota')
# def editanggota():
#         return render_template('editanggota.html', data= anggota.update())

@app.route('/tambahanggota', methods= ['GET', 'POST'])
def tambahanggota():
        if request.method == 'POST':
                NIM = request.form['nim']
                NamaMhs = request.form['namamhs']
                Jurusan = request.form['jurusanmhs']

                tambah = ModelAnggota(NIM, NamaMhs, Jurusan)
                anggota.create(tambah)
                return redirect(url_for('index'))
        else:
                return render_template('tambahanggota.html')


# @app.route('/tambahbuku', methods=['GET', 'POST'])
# def tambahbuku():
#         if request.method == 'POST':
#                 KodeBuku = request.form['KodeBuku']
#                 Judul = request.form['Judul']
#                 Stok = request.form['Stok']
#                 buku = ModelBuku(KodeBuku, Judul, Stok)
#                 Base.session.add(buku)
#                 Base.session.commit()
#                 return redirect(url_for('index'))
#         else:
#                 return render_template('index.html')
#
# @app.route('/tambahanggota', methods=['GET', 'POST'])
# def tambahanggota():
#         if request.method == 'POST':
#                 NIM = request.form['NIM']
#                 NamaMhs = request.form['NamaMhs']
#                 Jurusan = request.form['Jurusan']
#                 anggota = ModelAnggota(NIM, NamaMhs, Jurusan)
#                 Base.session.add(anggota)
#                 Base.session.commit()
#                 return redirect(url_for('index'))
#         else:
#                 return render_template('dataanggota.html')

if __name__ == '__main__':
        app.run(debug=True)

