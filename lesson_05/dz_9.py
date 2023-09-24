
chess_players = {"Carlsen, Magnus": 1865,
                 "Firouzja, Alireza": 2804,
                 "Ding, Liren": 2799,
                 "Caruana, Fabiano": 1792,
                 "Nepomniachtchi, Ian": 2773}

new_dict = {}

for key, value in chess_players.items():
    if value > 2000:
        new_dict[value] = key

print(new_dict)
