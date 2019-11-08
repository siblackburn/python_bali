import requests
import json

from flask import current_app as app
from flask import render_template, request, redirect, jsonify, session

from . import oath_client


# homepage
@app.route('/')
def hello():
    return render_template('index.html', user=get_current_user(), calendars=get_calendars())

def get_calendars():
    
    access_token = session.get('access_token')
    if access_token is None:
        return None

    uri = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
    response = requests.get(uri, headers={'Authorization': 'Bearer ' + access_token})
    calendars = [item['summary'] for item in response.json()['items']]
    return calendars

def get_current_user():
    access_token = session.get('access_token')
    if access_token is None:
        return None

    google_provider_cfg = requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    userinfo_response = requests.get(userinfo_endpoint, headers={'Authorization': 'Bearer ' + access_token})
    return userinfo_response.json()['name']


@app.route("/login")
def login():

    if get_current_user():
        return redirect('/')

    # Find out what URL to hit for Google login
    google_provider_cfg = requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = oath_client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile", "https://www.googleapis.com/auth/calendar.readonly"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def login_callback():

    # Get Google's authorizatin code
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = oath_client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(app.config['GOOGLE_CLIENT_ID'], app.config['GOOGLE_CLIENT_SECRET']),
    )

    # Parse, and save the token in the session
    tokens = oath_client.parse_request_body_response(json.dumps(token_response.json()))
    session['access_token'] = tokens['access_token']
    return redirect('/')


@app.route("/logout")
def logout():
    session.pop('access_token', None)
    return redirect('/')