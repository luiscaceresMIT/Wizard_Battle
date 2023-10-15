from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__,
            template_folder='/Users/luiscaceres/Library/Mobile Documents/com~apple~CloudDocs/IdeaProjects/Wizard_Battle/frontend/templates',
            static_folder='/Users/luiscaceres/Library/Mobile Documents/com~apple~CloudDocs/IdeaProjects/Wizard_Battle/frontend/static')

app.secret_key = 'some_secret_key'  # Used for session management

# Dummy data for warriors
WARRIORS = ["Legolas", "Frodo", "Gandalf", "Aragorn", "Saruman", "Sauron"]

@app.route('/')
def index():
    return render_template('index.html', warriors=WARRIORS)

@app.route('/choose_warrior', methods=['POST'])
def choose_warrior():
    warrior = request.form.get('warrior')
    if warrior and warrior in WARRIORS:
        session['warrior'] = warrior
        return redirect(url_for('player_details'))
    return redirect(url_for('index'))

@app.route('/player_details', methods=['GET', 'POST'])
def player_details():
    if 'warrior' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        player_name = request.form.get('player_name')
        wallet_details = request.form.get('wallet_details')
        if player_name and wallet_details:
            session['player_name'] = player_name
            session['wallet_details'] = wallet_details
            return redirect(url_for('battle'))
    return render_template('player_details.html')

@app.route('/battle')
def battle():
    if 'warrior' not in session or 'player_name' not in session:
        return redirect(url_for('index'))
    # TODO: Implement battle logic here
    return render_template('battle.html')

@app.route('/result')
def result():
    if 'warrior' not in session or 'player_name' not in session:
        return redirect(url_for('index'))
    # TODO: Calculate the total score and display the results
    return render_template('result.html')

if __name__ == "__main__":
    app.run(port=20001, debug=True)
