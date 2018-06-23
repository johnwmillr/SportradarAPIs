# Python wrapper for SportRadar APIs
[![PyPI version](https://badge.fury.io/py/sportradar.svg)](https://pypi.org/project/sportradar/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/sportradar/)

This is a Python wrapper for the sports APIs provided by [SportRadar](https://developer.sportradar.com/io-docs). You'll need to [sign up](https://developer.sportradar.com/member/register) for an API key to use the service. Luckily, Sportradar provides a free tier that allows for 1,000 API queries a month. The package currently only supports the [Soccer INTL Trial v3](https://developer.sportradar.com/files/indexSoccer.html) API, but I hope to expand it to support their APIs for other sports in the future.

## Installation
The easiest way to use this package is to install it via [PyPI](https://pypi.org/project/sportradar/) using `pip`:

`$pip install sportradar`

If you'd prefer to clone the repository and install it yourself, follow these steps:
1. Clone this repo:
`$git clone https://github.com/johnwmillr/SportradarAPI.git`
2. Enter the directory created:
`$cd SportradarAPI`
3. Install using pip:
`$python setup.py install`


## Usage
Below is a brief demonstration of using the package to download data for the 2018 FIFA World Cup.

```python
import sportradar

# Create an instance of the SportRadar API class
sr = sportradar.API("paste your api key here")

# Get a list of all tournaments
tournaments = sr.get_tournaments().json()

# Get info on the 2018 World Cup (Teams, Rounds, etc.)
worldcup = sr.get_tournament_info(tournaments['tournaments'][4]['id']).json()

# Get more information on each team in the World Cup
teams = []
team_counter = 0
for group in worldcup['groups']:
    for team in group['teams']:
        team_counter += 1
        team_id = team['id']
        team_name = team['name']
        print("({}): {}, {}".format(team_counter, team_name, team_id))
        try:
            teams.append(sportsradar.get_team_profile(team_id).json())
        except Exception as e:
            print("Error: {}".format(e))
        time.sleep(5) # wait 5 seconds before next API call

# Save the team data to a .json file
print("Saving the data...", end="", flush=True)
with open("world_cup_team_data.json", "w") as outfile:
    json.dump(teams, outfile)
print(" Done.")

```

## Example projects
  - [2018 FIFA World Cup player stats](https://www.johnwmillr.com/fifa-world-cup-data/)
