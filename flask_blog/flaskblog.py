from flask import Flask, render_template, request
app = Flask(__name__)

Mentors = [
    {
        'mentorid': '1',
        'mentorname': 'bhavya',
        'telegram_invite': 'https://t.me/joinchat/HWPXRXq9IUP0Zq4B',
        'skill': ['cpp','python','java']
    },
    {
        'mentorid': '2',
        'mentorname': 'vasu',
        'telegram_invite': 'https://t.me/joinchat/Ivn17bDpRhIzNZor',
        'skill': ['c#','python','javascript']
    },
    {
        'mentorid': '3',
        'mentorname': 'dhruv',
        'telegram_invite': 'https://t.me/joinchat/IBsz8kjg-61tOPck',
        'skill': ['sql','ruby','css']
    },
    {
        'mentorid': '4',
        'mentorname': 'chiggy',
        'telegram_invite': 'https://t.me/joinchat/ITTgLEMrDJqnElGR',
        'skill': ['cpp','ruby','css']
    }
]

Mentees = [
    {
        'menteeid': '1',
        'menteename': 'vishu',
        'interest': ['cpp','c','css'],
        'matching': ''
    },
    {
        'menteeid': '2',
        'menteename': 'dominic',
        'interest': ['sql','python','java'],
        'matching': ''
    },
    {
        'menteeid': '3',
        'menteename': 'deeksha',
        'interest': ['javascript','python','cpp'],
        'matching': ''
    },
    {
        'menteeid': '4',
        'menteename': 'akhil',
        'interest': ['sql','c#','python'],
        'matching': ''
    }
]


def matching():
    for mentee in Mentees:
        print(mentee)
        for i in mentee['interest']:
            for mentor in Mentors:
                if i in mentor['skill']:
                    mentee['matching']=mentor['mentorid']
                    break


@app.route('/')
@app.route('/home')
def home():
    return render_template('loginpage.html')


@app.route('/MentororMentee')
def mentorormentee():
    return render_template('mentorormentee.html')


@app.route('/mentor')
def mentor():
    return render_template('mentor.html')


@app.route('/mentee')
def mentee():
    return render_template('mentee.html')


@app.route('/matching', methods=['GET'])
def mentee_match():
    matching()
    menteeid=request.args['']
    mentee_name=''
    mentee_interest=''
    mentor_id=''
    mentor_name=''
    mentee_id=''
    telegram=''
    
    for i in Mentees:
        if i['menteeid']==menteeid:
            mentee_id=i['menteeid']
            mentee_name=i['menteename']
            mentee_interest=i['interest']
            mentor_id=i['matching']
    
    for i in Mentors:
        if i['mentorid']==mentor_id:
            mentor_name=i['mentorname']
            telegram=i['telegram_invite']

    return render_template('matching.html', telegram=telegram,mentee_name=mentee_name,mentee_interest=mentee_interest,mentee_id=mentee_id,mentor_name=mentor_name,mentor_id=mentor_id)


if __name__ == '__main__':
    app.run(debug=True)
