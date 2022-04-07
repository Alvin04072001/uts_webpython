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

@app.route('/tambahbuku', methods=['GET', 'POST'])
def tambahbuku():
        if request.method == 'POST':
                KodeBuku = request.form['KodeBuku']
                Judul = request.form['Judul']
                Stok = request.form['Stok']
                buku = ModelBuku(KodeBuku, Judul, Stok)
                Base.session.add(buku)
                Base.session.commit()
                return redirect(url_for('index'))
        return render_template('dataanggota.html', container= anggota.read())

if __name__ == '__main__':
        app.run(debug=True)

