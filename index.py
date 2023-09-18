from flask import Flask, render_template
from firebase_con import FirebaseModel
from datetime import datetime
import asyncio

app = Flask(__name__)
firebase_connect = FirebaseModel()


@app.route('/')
def index():

    # init
    experiences = asyncio.run(firebase_connect.get('experiences'))
    user = asyncio.run(firebase_connect.get('user'))
    work = asyncio.run(firebase_connect.get('work'))
    project = asyncio.run(firebase_connect.get('projects'))

    return render_template('home.html',
                           user=user[0], projects=project, work=work, experiences=experiences)


@app.template_filter('ctime')
def timectime(s):
    return datetime.fromtimestamp(s.timestamp()).strftime("%m/%d/%Y")


@app.template_filter('yservice')
def countYearsService(date_start, date_end):
    x = datetime.date(date_end) - datetime.date(date_start)
    # year
    year = x.days // 365 if x.days >= 365 else 0
    # months
    months = (x.days - year * 365) // 30
    # days
    days = (x.days - year * 365 - months * 30)

    year = f'{year}y /' if year != 0 else ""
    months = f'{months}m /' if months != 0 else ""
    days = f'{days} Days' if days != 0 else ""

    return f'{year} {months} {days}'


# Render
app.run(debug=False) if __name__ == '__main__' else None
