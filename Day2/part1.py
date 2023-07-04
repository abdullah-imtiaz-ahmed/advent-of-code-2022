Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"


opponents_moves = {"A": Rock, "B": Paper, "C": Scissors}
my_moves = {"X": Rock, "Y": Paper, "Z": Scissors}

score = {Rock: 1, Paper: 2, Scissors: 3}
outcome = {"lost": 0, "draw": 3, "won": 6}
# Rock defeats Scissors etc
defeats = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

file_name = 'sample_input2.txt'


def file_read_gen(file):
    for line in file:
        line = line.strip()
        yield list(line)


def compute_outcome_of_game(file_name):
    score_of_round = []
    with open(file_name, 'r') as file:
        for round in file_read_gen(file):
            round = [move for move in round if move.strip()]
            opponenets_move = opponents_moves[round[0]]
            my_move = my_moves[round[1]]
            # Won
            if opponenets_move == defeats[my_move]:
                score_of_round.append(outcome['won'] + score[my_move])
            # Draw
            elif opponenets_move == my_move:
                print(round, opponenets_move, my_move, defeats[my_move])
                score_of_round.append(outcome['draw'] + score[my_move])
            # Lost
            else:
                score_of_round.append(outcome['lost'] + score[my_move])
            
    return sum(score_of_round)


if __name__ == "__main__":  
    print(compute_outcome_of_game(file_name))