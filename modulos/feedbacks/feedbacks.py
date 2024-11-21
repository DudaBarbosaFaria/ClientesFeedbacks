from flask import Blueprint, render_template, request, redirect, flash
from models import Feedbacks, Cliente
from database import db

bp_feedbacks = Blueprint('feedbacks', __name__, template_folder="templates")

@bp_feedbacks.route("/")
def index():
    f = Feedbacks.query.all()
    return render_template("feedbacks.html", feedbacks=f)


@bp_feedbacks.route("/add")
def add():
    c = Cliente.query.all()
    return render_template("feedbacks_add.html", clientes=c)


@bp_feedbacks.route("/save", methods=['POST'])
def save():
    comentario = request.form.get("comentario")
    data = request.form.get("data")
    id_cliente = request.form.get("id_cliente")

    if comentario and data and id_cliente:
        db_feedback = Feedbacks(comentario, data, id_cliente)
        db.session.add(db_feedback)
        db.session.commit()
        flash("Feedback salvo!")
        return redirect("/feedbacks")
    else:
        flash("Preencha tudo!")
        return redirect("/feedbacks/add")


@bp_feedbacks.route("/remove/<int:id>")
def remove(id):
    f = Feedbacks.query.get(id)
    try:
        db.session.delete(f)
        db.session.commit()
        flash("Feedback removido!")
    except:
        flash("Feedback inválido!")
    return redirect("/feedbacks")


@bp_feedbacks.route("/edit/<int:id>")
def edit(id):
    f = Feedbacks.query.get(id)
    c = Cliente.query.all()
    return render_template("feedbacks_editar.html", feedback=f, cliente=c)


@bp_feedbacks.route("/edit-save", methods=['POST'])
def edit_save():
    comentario = request.form.get("cometario")
    data = request.form.get("data")
    id_cliente = request.form.get("id_cliente")
    id_feedback = request.form.get("id_feedback")
    
    if comentario and data and id_feedback and id_cliente:
        f = Feedbacks.query.get(id_feedback)
        f.comentario = comentario
        f.data = data
        f.id_cliente = id_cliente
        db.session.commit()
        flash("Feedback editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/feedbacks")