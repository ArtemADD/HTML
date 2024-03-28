from flask_restful.reqparse import RequestParser


class Parser(RequestParser):
    def __init__(self):
        super().__init__()

    def jobs_res(self):
        self.add_argument('job', required=True, type=str)
        self.add_argument('team_leader', required=True, type=int)
        self.add_argument('work_size', required=True, type=int)
        self.add_argument('collaborators')
        self.add_argument('is_finished', required=True, type=bool)

    def user_res(self):
        pass
