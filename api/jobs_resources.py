from flask import jsonify
from flask_restful import Resource, abort, reqparse
from api.parser import Parser
from data import db_session
from data.jobs import Jobs


class JobsResources(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': jobs.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def __init__(self):
        super().__init__()
        self.parser = Parser()
        self.parser.jobs_res()

    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'team_leader', 'work_size', 'collaborators', 'is_finished')) for item in jobs]})

    def post(self):
        args = self.parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            team_leader=args['team_leader'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'id': jobs.id})


def abort_if_news_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"News {jobs_id} not found")
