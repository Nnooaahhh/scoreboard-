from flask import jsonify

# ... (your existing code)

@app.route('/get_live_scores')
def get_live_scores():
    # Modify this part to fetch live scores from your database
    # Replace the dummy data with actual data from your database
    live_scores = [
        {'sport': 'Football', 'team1': 'Team A', 'score1': 14, 'team2': 'Team B', 'score2': 21},
        {'sport': 'Basketball', 'team1': 'Team C', 'score1': 102, 'team2': 'Team D', 'score2': 98},
        # Add more sports and scores as needed
    ]
    return jsonify(live_scores)

# ... (rest of your existing code)
