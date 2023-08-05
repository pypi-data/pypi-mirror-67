from functools import partial, update_wrapper
from flask import jsonify

def wrapped_partial(func, *args, **kwargs):
    partial_func = partial(func, *args, **kwargs)
    update_wrapper(partial_func, func)
    return partial_func

class HealthCheck(object):
    def __init__(self):
        pass

    def add_db_check(self, app, db):
        app.add_url_rule('/dbhealth', view_func=wrapped_partial(self._check_db, db))

    def _check_db(self, db):
        try:
            db.session.execute('SELECT 1;')
            return jsonify({'state': 'db_healthy'}), 200
        except Exception as e:
            return jsonify({'state': 'db_not_healthy', 'data': str(e)}), 504
