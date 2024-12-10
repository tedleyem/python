# MISC TEAM EXAMPLES, ARRAYS, VARIABLES, AND TEST
# BURN AFTER READING 
# List of NBA teams
nba_teams = [
    "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
    "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
    "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
    "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
    "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
    "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
]

# Set up the argument parser
parser = argparse.ArgumentParser(description='NBA Team Argument List')

# Add argument for team selection
parser.add_argument(
    '--team', 
    choices=nba_teams, 
    required=True, 
    help='Choose an NBA team from the list: ' + ', '.join(nba_teams)

    parser.add_argument('ATL', help="Atlanta Hawks", type=str)
    parser.add_argument('BOS', help="Boston Celtics", type=str)
    parser.add_argument('BKN', help="Brooklyn Nets", type=str)
    parser.add_argument('CHA', help="Charlotte Hornets", type=str)
    parser.add_argument('CHI', help="Chicago Bulls", type=str)
    parser.add_argument('CLE', help="Cleveland Cavaliers", type=str)
    parser.add_argument('DAL', help="Dallas Mavericks", type=str)
    parser.add_argument('DEN', help="Denver Nuggets", type=str)
    parser.add_argument('DET', help="Detroit Pistons", type=str)
    parser.add_argument('GSW', help="Golden State Warriors", type=str)
    parser.add_argument('HOU', help="Houston Rockets", type=str)
    parser.add_argument('IND', help="Indiana Pacers", type=str)
    parser.add_argument('LAC', help="Los Angeles Clippers", type=str)
    parser.add_argument('LAL', help="Los Angeles Lakers", type=str)
    parser.add_argument('MEM', help="Memphis Grizzlies", type=str)
    parser.add_argument('MIA', help="Miami Heat", type=str)
    parser.add_argument('MIL', help="Milwaukee Bucks", type=str)
    parser.add_argument('MIN', help="Minnesota Timberwolves", type=str)
    parser.add_argument('NOP', help="New Orleans Pelicans", type=str)
    parser.add_argument('NYK', help="New York Knicks", type=str)
    parser.add_argument('OKC', help="Oklahoma City Thunder", type=str)
    parser.add_argument('ORL', help="Orlando Magic", type=str)
    parser.add_argument('PHI', help="Philadelphia 76ers", type=str)
    parser.add_argument('PHX', help="Phoenix Suns", type=str)
    parser.add_argument('POR', help="Portland Trail Blazers", type=str)
    parser.add_argument('SAC', help="Sacramento Kings", type=str)
    parser.add_argument('SAS', help="San Antonio Spurs", type=str)
    parser.add_argument('TOR', help="Toronto Raptors", type=str)
    parser.add_argument('UTA', help="Utah Jazz", type=str)
    parser.add_argument('WAS', help="Washington Wizards", type=str)
)

# Parse the arguments
args = parser.parse_args()

# Print the selected NBA team
print(f"Selected NBA Team: {args.team}")


nba_team_shortcodes = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS"
}

