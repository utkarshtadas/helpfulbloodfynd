from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy

#from app import app
db = SQLAlchemy()
# -----------------------------DONOR PAGE--------------------------------------
class Donor(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    bloodgroup = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)

# -----------------------------RECIPIENT PAGE--------------------------------------
class Recipient(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    bloodgroup = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(12), nullable=True)


# -----------------------------CONTACT PAGE--------------------------------------
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

