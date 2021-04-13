from flask import Blueprint, jsonify
from flask import request
from flask_jwt import current_identity, jwt_required

from app import db
from app.mod_note import Note
from .model import NoteCategory

mod_category = Blueprint('category', __name__, url_prefix='/api')


@mod_category.route('/category', methods=["GET"])
@jwt_required()
def get_list():
    categories = NoteCategory.query.filter_by(user_id=current_identity.id).all()
    return jsonify(categories=[c.serialize() for c in categories]), 200


@mod_category.route('/category', methods=["POST"])
@jwt_required()
def post():
    payload = request.get_json(True)
    category = NoteCategory(payload['name'], current_identity.id)
    db.session.add(category)
    db.session.commit()
    return jsonify(category.serialize()), 201


@mod_category.route('/category/<category_id>/note', methods=["PUT"])
@jwt_required()
def assign_note(category_id):
    category = NoteCategory.query.filter_by(id=category_id, user_id=current_identity.id).first()
    if not category:
        return jsonify(error="Category not found"), 404
    payload = request.get_json(True)
    if 'note_id' not in payload:
        return jsonify(error="You have to specify note id in request body"), 400
    note = Note.query.filter_by(id=payload['note_id'], user_id=current_identity.id).first()
    if not note:
        return jsonify(error="Note not found"), 400
    note.category_id = category_id
    db.session.commit()
    return jsonify(notes=[n.serialize() for n in category.notes], category=category.serialize())


@mod_category.route('/category/<int:category_id>/note', methods=["DELETE"])
@jwt_required()
def unassign_note(category_id):
    category = NoteCategory.query.filter_by(id=category_id, user_id=current_identity.id).first()
    if not category:
        return jsonify(error="Category not found"), 404
    payload = request.get_json(True)
    if 'note_id' not in payload:
        return jsonify(error="You have to specify note id in request body"), 400
    note = Note.query.filter_by(id=payload['note_id'], user_id=current_identity.id).first()
    if not note:
        return jsonify(error="Note not found"), 400
    if note.category_id != category_id:
        return jsonify(error="Note is not in this category"), 400
    note.category_id = None
    db.session.commit()
    return jsonify(), 204
