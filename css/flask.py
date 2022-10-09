from flask import Flask, render_template, request
from flask import Flask, render_template, redirect, url_for
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET KEY'] = 'tyX0gyofGdxSyluQ6AQyZVet6Lxgasvsl'
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    url = 'http://api.ipstack.com/{}?access_key=22f31c0c11f77e5f87f8210630047dad'.format(ip_addr)
    r = requests.get(url)
    j = json.loads(r.text)
    longt = j['longtitude']
    latit= j['latitude']
    
    form = InitialiseForm()
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', form=form)
    
    return render_template("index.html")


class InitialiseForm(FlaskForm):
    userID = StringField('What is your UserID?', validators=[DataRequired()])
    country = StringField('Which country do you live in?', validators=[DataRequired()])
    geoloc = StringField('What is your postal code?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LogForm(FlaskForm):
    tagID = StringField('Type the 10 character Tag ID', validators=[DataRequired()])
    date = datetime.now()
    submit = SubmitField('Submit')


def notify():
    from pywebpush import webpush, WebPushException
    WEBPUSH_VAPID_PRIVATE_KEY = 'xxx'

    items = Subscriber.query.filter(Subscriber.is_active == True).all()
    count = 0
    for _item in items:
        try:
            webpush(
                subscription_info=_item.subscription_info_json,
                data="Please Log Your Wear Now",
                vapid_private_key=WEBPUSH_VAPID_PRIVATE_KEY,
                vapid_claims={
                    "sub": "mailto:aweare.info@gmail.com"
                }
            )
            count += 1
        except WebPushException as ex:
            logging.exception("webpush fail")


    return "{} notification(s) sent".format(count)