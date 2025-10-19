from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3, random

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_for_session_management' 

# --- Core Logic Functions ---

def classify_age_group(age):
    """Classifies player's age into predefined groups, including seniors."""
    try:
        age = int(age)
    except ValueError:
        return "adults"

    if age <= 12:
        return "kids"
    elif 13 <= age <= 19:
        return "teens"
    elif 20 <= age <= 59:
        return "adults"
    else: # 60+
        return "seniors" # Matches the group found in your uploaded data!

def get_question_by_age(age_group):
    """Fetches a random question, its correct answer, and its options."""
    conn = sqlite3.connect('database/questions.db')
    cur = conn.cursor()
    
    try:
        # Fetch ID, Question, Correct Answer, and Options
        cur.execute(
            "SELECT id, question_text, correct_answer, options FROM questions WHERE age_group = ? ORDER BY RANDOM() LIMIT 1", 
            (age_group,)
        )
        result = cur.fetchone() 
    except sqlite3.OperationalError as e:
        print(f"\n❌ DATABASE ERROR: {e}")
        print("   Action required: You MUST run 'python load_data.py' to create the table!")
        result = None
        
    conn.close()
    return result

# --- Flask Routes ---

@app.route('/')
def home():
    """Landing page: User enters name and age."""
    session.clear()
    return render_template('index.html')

@app.route('/game')
def game():
    """Game page: Player attempts the current challenge."""
    name = request.args.get('name', session.get('player_name', 'Player'))
    age = request.args.get('age', session.get('age', 20))
    
    if not session.get('player_name'):
        session['player_name'] = name
        session['age'] = age
        session['keys'] = 0 
        session['current_question_id'] = None
    
    if session.get('keys', 0) >= 100:
        return redirect(url_for('map_page'))
        
    return render_template('game.html', name=name, age=age)

@app.route('/map')
def map_page():
    """Shows player's progress and directs them to the next challenge."""
    current_keys = session.get('keys', 0)
    player_name = session.get('player_name', 'Adventurer')
    
    win_condition = current_keys >= 100
    
    if not session.get('player_name'):
        return redirect(url_for('home'))
        
    return render_template('map.html', 
                           name=player_name, 
                           keys=current_keys, 
                           win=win_condition)

# --- API Endpoints ---

@app.route('/get_question', methods=['POST'])
def get_question():
    """API: Fetches a question, its options, and sends it to the frontend."""
    data = request.get_json()
    age = data.get('age', session.get('age', 20)) 
    
    age_group = classify_age_group(age)
    question_data = get_question_by_age(age_group)

    if question_data:
        question_id, question, correct_answer, options = question_data
        
        session['current_question_id'] = question_id
        session[f'answer_for_{question_id}'] = correct_answer
        
        return jsonify({
            'id': question_id, 
            'question': question,
            'options': options
        })
    else:
        return jsonify({'id': None, 'question': f"No questions found for the age group '{age_group}'!", 'options': None})

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    """API: Checks the user's answer and calculates the score, redirecting to the map."""
    data = request.get_json()
    user_answer = data.get('answer', '').strip().lower() 
    question_id = data.get('id')
    
    KEY_SCORE_CORRECT = 10
    KEY_SCORE_INCORRECT = -1
    
    correct_answer = session.pop(f'answer_for_{question_id}', None) 
    session.pop('current_question_id', None) 
    
    if correct_answer is None:
        return jsonify({'success': False, 'message': 'Session expired. Returning to map.', 'new_keys': session.get('keys', 0), 'redirect': url_for('map_page')})
    
    is_correct = user_answer == correct_answer.strip().lower()
    
    score_change = KEY_SCORE_CORRECT if is_correct else KEY_SCORE_INCORRECT
    session['keys'] = session.get('keys', 0) + score_change
    session['keys'] = max(0, session['keys'])

    message = f"🎉 Correct! You earned {KEY_SCORE_CORRECT} keys!" if is_correct else f"❌ Incorrect. You lost {abs(KEY_SCORE_INCORRECT)} key. The answer was '{correct_answer}'."
    
    return jsonify({
        'success': True, 
        'message': message, 
        'correct': is_correct,
        'new_keys': session['keys'],
        'redirect': url_for('map_page') 
    })

if __name__ == '__main__':
    app.run(debug=True)
