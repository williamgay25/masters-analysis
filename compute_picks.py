import pandas as pd

PLAYERS_DIR = 'players/'
COMPETITION_NAME = "MASTERS POT - Input Data"
TOURNAMENT_DAYS = 4
HOLES_PER_DAY = 18
TOTAL_HOLES = TOURNAMENT_DAYS * HOLES_PER_DAY
ENTRANTS = 200
BET_SIZE = 10
POT = ENTRANTS * BET_SIZE
PAY_PERCENTAGES = [0.85, 0.1, 0.05]
PAYOUTS = [x * POT for x in PAY_PERCENTAGES]
group_a = pd.read_csv(PLAYERS_DIR + 'group_a.csv')
group_b = pd.read_csv(PLAYERS_DIR + 'group_b.csv')
group_c = pd.read_csv(PLAYERS_DIR + 'group_c.csv')
possible_combos = len(group_a) * len(group_b) * len(group_c)

def log_inputs():
    print("\n" + "=" * 20 + " " + COMPETITION_NAME + " " + "=" * 20 + "\n")

    print(f"There are {ENTRANTS} in the competition.")
    print(f"The bet size for each team is {BET_SIZE}")
    print(f"The total estimated pot for the competition is {POT}")
    print(f"The payouts are structured as follows:" )
    for idx, payout in enumerate(PAYOUTS):
        print(f"You will be paid ${payout} for placing {idx + 1}")
    print(f"There are {len(group_a)} players in group a")
    print(f"There are {len(group_b)} players in group b")
    print(f"There are {len(group_c)} players in group c")
    print(f"There are a total of {possible_combos} possible betting combinations")
    print(f"Each player will play {TOURNAMENT_DAYS} days, {HOLES_PER_DAY} holes per day for a total of {TOTAL_HOLES} total holes")

    print("\n" + "=" * (42 + len(COMPETITION_NAME)) + "\n")

if __name__ == "__main__":
    log_inputs()