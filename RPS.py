def player(prev_play, opponent_history=[], play_order={}):
    # Reset internal memory tables cleanly between different bot matches
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
        return 'R'

    opponent_history.append(prev_play)
    n = 4  # The golden window depth to comfortably beat all 4 bots

    if len(opponent_history) > n:
        # Log the full pattern sequence that just occurred
        actual_seq = "".join(opponent_history[-(n+1):])
        play_order[actual_seq] = play_order.get(actual_seq, 0) + 1
        
        # Build the lookahead string using the exact current trailing context
        current_n = "".join(opponent_history[-n:])
        predictions = {
            'R': play_order.get(current_n + 'R', 0),
            'P': play_order.get(current_n + 'P', 0),
            'S': play_order.get(current_n + 'S', 0)
        }
        
        # Pick the highest-weighted predicted move
        predicted_move = max(predictions, key=predictions.get)
    else:
        predicted_move = 'R'
        
    # Counter their predicted move perfectly
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    return ideal_response[predicted_move]
