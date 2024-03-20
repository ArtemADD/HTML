import flask
from flask import jsonify, make_response, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict(only=(
                              'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                              'hashed_password'))
                 for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>')
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return (
        {
            'user':
                user.to_dict(only=(
                              'id', 'surname', 'name', 'age', 'position', 'speciality', 'address', 'email',
                              'hashed_password'))

        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = User(
        email=request.json['email'],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        hashed_password=request.json['hashed_password']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'id': user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in ['surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password']
                 for key in request.json):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    u = user.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password'))
    for k in request.json.keys():
        u[k] = request.json[k]
    user.surname = u['surname']
    user.name = u['name']
    user.age = u['age']
    user.position = u['position']
    user.speciality = u['speciality']
    user.email = u['email']
    user.hashed_password = u['hashed_password']
    db_sess.commit()
    return jsonify({'success': 'OK'})

