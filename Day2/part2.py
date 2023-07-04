Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"
Lose = "Lose"
Draw = "Draw"
Win = "Win"

opponents_moves = {"A": Rock, "B": Paper, "C": Scissors}
my_moves = {"X": Lose, "Y": Draw, "Z": Win}

score = {Rock: 1, Paper: 2, Scissors: 3}
outcome = {Lose: 0, Draw: 3, Win: 6}
# Rock defeats Scissors etc
defeats = {Rock: Scissors, Scissors: Paper, Paper: Rock}

file_name = "test_input.txt"


def file_read_gen(file):
    for line in file:
        line = line.strip()
        yield list(line)


def compute_outcome_of_game(file_name):
    score_of_round = []
    with open(file_name, "r") as file:
        for round in file_read_gen(file):
            round = [move for move in round if move.strip()]
            opponenets_move = opponents_moves[round[0]]
            outcome_of_round = my_moves[round[1]]
            # Win
            if outcome_of_round == Win:
                my_move = {value: key for key, value in defeats.items()}[opponenets_move]
                score_of_round.append(outcome[Win] + score[my_move])
            # Draw
            elif outcome_of_round == Draw:
                my_move = opponenets_move
                score_of_round.append(outcome[Draw] + score[my_move])
            # # Lost
            else:
                my_move = defeats[opponenets_move]
                score_of_round.append(score[my_move] + outcome[Lose])

    return sum(score_of_round)


if __name__ == "__main__":
    print(compute_outcome_of_game(file_name))
