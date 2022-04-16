from crypt import methods
from flask import Flask, jsonify, render_template, request, session
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_an_example'



@app.route('/')
def start():
  '''
  This should display the starting board game. 

  '''
  session['board'] = boggle_game.make_board()
  session['scores'] = []
  session['times_played'] = 0
  return render_template("welcome.html", board = session['board'])

@app.route('/guess')
def guess(): 
  '''
  This should include check to see if the submitted word was a match

  '''
  args = request.args
  match = boggle_game.check_valid_word(session['board'], args.get("guess"))
  # return jsonify({'info' : info})
  return jsonify({'info' : match})

@app.route('/save')
def save():
  '''
  This will than save the score and how many times this user has played

  '''
  args = request.args
  session['scores'] = args.get('scores')
  session['times_playes'] = session['times_played'] + 1
  resp = jsonify(success=True)
  resp.status_code = 200
  return resp
    