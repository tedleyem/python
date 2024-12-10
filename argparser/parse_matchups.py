#!/bin/python3 
# quick edumacational exercise on using argparse with nba teams
# https://docs.python.org/3/library/argparse.html#parents
# THIS ISNT USING ARGPARSE PROPERLY YET --DELETE LINE WHEN FIXED 
import argparse
from NBATeams import NBATeams
 
# Set up the argument parser
parser = argparse.ArgumentParser(description='choose two nba teams.')

def parse_args():
    # parse the matchups arguments
    parser = argparse.ArgumentParser(
        prog='NBA Matchups CLI',
        description='Choose two nba teams and get matchup results',
        epilog='Select teams with their ShortCode (ex: --MIA for Miami Heat).',
)
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-o', '--output', help='Save the results to text file')
    parser.add_argument('-c', '--output', help='Save the results to clipboard')
    parser.add_argument('--home', required=True, help='choose first team')
    parser.add_argument('--away', required=True, help='choose second team')
    parser.add_argument('-vs', '--versus', help='add opossing team', required=True)
    return parser.parse_args()

def print_results():
    # this will print results of scraped websites and display them in a table 
    print('No results to show just yet')

# Parse the arguments
args = parser.parse_args()

def main():
    nba = NBATeams()
    # TEST CLASS Module 
    # Get the shortcode for a specific team
    team_name = input("\nEnter the name of an NBA team to get its shortcode: ")
    print(f"Shortcode for {team_name}: {nba.get_shortcode(team_name)}")
        
if __name__ == "__main__":
    main()

