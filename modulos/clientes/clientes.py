from flask import Blueprint, render_template, request, redirect, flash
from models import Cliente
from database import db

bp_cliente = Blueprint('cliente', __name__, template_folder="templates")

@bp_cliente.route("/")
def index():
    c = Cliente.query.all()
    return render_template("clientes.html", alunos=c)


@bp_cliente.route("/add")
def add():
    return render_template("clientes_add.html")


@bp_cliente.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    email = request.form.get("email")

    if nome and email:
        db_cliente = Cliente(nome, email)
        db.session.add(db_cliente)
        db.session.commit()
        flash("CLiente salvo!")
        return redirect("/clientes")
    else:
        flash("Preencha tudo!")
        return redirect("/clintes/add")


@bp_cliente.route("/remove/<int:id>")
def remove(id):
    c = Cliente.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("CLiente removido!")
    except:
        flash("Cliente inválido!")
    return redirect("/clientes")


@bp_cliente.route("/edit/<int:id>")
def edit(id):
    c = Cliente.query.get(id)
    return render_template("clientes_editar.html", alunos=c)


@bp_cliente.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    id_cliente = request.form.get("id_cliente")
    
    if nome and email and id_cliente:
        c = Cliente.query.get(id_cliente)
        c.nome = nome
        c.matricula = email
        db.session.commit()
        flash("Cliente editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/clientes")