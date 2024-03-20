import flask
from flask import jsonify, make_response, request
import datetime

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(
                    'id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'id', 'job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators = request.json['collaborators'],
        start_date=datetime.datetime.strptime(request.json['start_date'], '%Y-%m-%d %H:%M:%S'),
        end_date=datetime.datetime.strptime(request.json['end_date'], '%Y-%m-%d %H:%M:%S'),
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['POST'])
def edit_jobs(jobs_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in ['job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'] for key in request.json):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()
    j = jobs.to_dict(only=('job', 'team_leader', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
    for k in request.json.keys():
        j[k] = request.json[k]
    jobs.job = j['job']
    jobs.team_leader = j['team_leader']
    jobs.work_size = j['work_size']
    jobs.collaborators = j['collaborators']
    jobs.start_date = datetime.datetime.strptime(j['start_date'], '%Y-%m-%d %H:%M:%S')
    jobs.end_date = datetime.datetime.strptime(j['end_date'], '%Y-%m-%d %H:%M:%S')
    jobs.is_finished = j['is_finished']
    db_sess.commit()
    return jsonify({'success': 'OK'})
