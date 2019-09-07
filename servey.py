from flask import Flask, render_template, request, redirect, session# added request
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    # if 'random_num' not in session:
    session['random_num'] = random.randint(1, 100)
    print(session['random_num'])

    return render_template('index.html')

@app.route('/1', methods = ['POST'])
def guess():
    if 'submit_times' in session:
        session['submit_times'] += 1
    else:
        session['submit_times'] = 1

    print(session['random_num'])

    session['type_num'] = int(request.form['number'])
    print(session['type_num'])

    return redirect('/show')

@app.route('/show')
def show():
    if session['submit_times'] == 5:
        true_num = session['random_num']
        return render_template('wrong.html', true_num_on_template = true_num, times_on_template = session['submit_times'])
    elif session['type_num'] > session['random_num']:
        high_low = 'high'
        return render_template('results.html',status = high_low, times_on_template = session['submit_times'])
    elif session['type_num'] < session['random_num']:
        high_low = 'low'
        return render_template('results.html',status = high_low, times_on_template = session['submit_times'])
    elif session['type_num'] == session['random_num']:
        true_num = session['random_num']
        return render_template('correct.html', true_num_on_template = true_num, times_on_template = session['submit_times'])

@app.route('/2', methods = ['POST'])   
def reset():
    session.pop('random_num')
    session.pop('submit_times')
    session.pop('type_num')
    return redirect("/")

@app.route('/3', methods = ['POST'])   
def winner():
    if 'winner_name' in session:
        session['winner_name'] = request.form['winner']
    else:
        session['winner_name'] = request.form['winner']
    return redirect('/winner')

@app.route('/winner')
def show_winner():
    return render_template('winner.html', winner_on_template = session['winner_name'],times_on_template = session['submit_times'])

if __name__ == "__main__":
    app.run(debug=True)