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

@app.route("/anggota")
def index():
        return render_template('anggota.html', container= anggota.read())

if __name__ == '__main__':
        app.run(debug=True)

