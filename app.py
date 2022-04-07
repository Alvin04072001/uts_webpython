from flask import Flask, render_template, request,\
        flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine("sqlite:///dbperpustakaan.db")
app = Flask(__name__)