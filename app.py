from flask import Flask, render_template, request,\
        flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
# from tanggota import *
from buku import *
# from tkembali import *
# from tpinjaman import *

engine = create_engine("sqlite:///dbperpustakaan.db")
app = Flask(__name__)

CRUD_Buku = CRUD_Buku(engine)

