from flask import url_for, redirect
from flask import request, session
from flask import jsonify
from flask_oauthlib.client import OAuth

from harambee import app


app.config.from_envvar('HARAMBEE_SETTINGS')

oauth = OAuth()
github = oauth.remote_app(
    'GitHub',
    base_url='https://api.github.com/',
    request_token_url=None,
    authorize_url='https://github.com/login/oauth/authorize',
    access_token_url='https://github.com/login/oauth/access_token',
    consumer_key=app.config['GITHUB_CLIENT_ID'],
    consumer_secret=app.config['GITHUB_SECRET_KEY'],
    request_token_params={'scope': 'user:email'},
)


@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized', _external=True,
                            next=request.args.get('next') or request.referrer or
                            None))

@app.route('/logout')
def logout():
    session.pop('github_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None:
        return 'Access denied: {} {}'.format(request.args['error_reason'],
                                             request.args['error_description'])
    session['github_token'] = (resp['access_token'], )
    me = github.get('/user/emails')
    return jsonify(emails=me.data)

@github.tokengetter
def get_github_token():
    return session.get('github_token')
