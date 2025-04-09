import json
import pandas as pd

PLAYERS_DIR = 'players/'
ODDS_DIR = 'odds/'

def convert_odds_to_probability(data: pd.DataFrame) -> pd.DataFrame:
    for idx, row in data.iterrows():
        if row['odds'] > 0:
            data.at[idx, 'win_prob'] = 100 / (row['odds'] + 100)
        else:
            data.at[idx, 'win_prob'] = abs(row['odds']) / (abs(row['odds']) + 100)
    
    return data

if __name__ == "__main__":
    """ group_a = pd.read_csv(PLAYERS_DIR + 'group_a.csv')
    group_b = pd.read_csv(PLAYERS_DIR + 'group_b.csv')
    group_c = pd.read_csv(PLAYERS_DIR + 'group_c.csv') """

    odds_raw = open(ODDS_DIR + 'odds.json', 'r').read()
    odds_json = json.loads(odds_raw)
    odds = pd.DataFrame(odds_json['players'])
    odds = convert_odds_to_probability(odds)
    print(odds)