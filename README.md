# Sportradar APIs
---
[![Build Status](https://travis-ci.org/johnwmillr/SportradarAPIs.svg?branch=master)](https://travis-ci.org/johnwmillr/SportradarAPIs)
[![PyPI version](https://badge.fury.io/py/sportradar.svg)](https://pypi.org/project/sportradar/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/sportradar/)

This is a Python wrapper for the sports APIs provided by [Sportradar](https://developer.sportradar.com/io-docs). You'll need to [sign up](https://developer.sportradar.com/member/register) for an API key to use the service. Sportradar provides a free trial evaluation that provides 1,000 API queries at up to 1 query per second.

## Supported APIs
| Sport         | API Wrapper   | Unit Tests  |
|:--------------|:-------------:|:-----------:|
| [Soccer](https://developer.sportradar.com/files/indexSoccer.html)  :soccer: | :heavy_check_mark: | :heavy_check_mark: |
| [NBA](https://developer.sportradar.com/files/indexBasketball.html#nba-api-v4)  :basketball: | :heavy_check_mark: | :heavy_check_mark: |
| [WNBA](https://developer.sportradar.com/files/indexBasketball.html#wnba-api-v4)  :basketball: | :heavy_check_mark: | :heavy_check_mark: |
| [NCAAMB](https://developer.sportradar.com/files/indexBasketball.html#ncaamb-api-v7)  :basketball: | :heavy_check_mark: | :heavy_check_mark: |
| [NFL](https://developer.sportradar.com/files/indexFootball.html)  :football: | :heavy_check_mark: | :heavy_check_mark: |
| [NHL](https://developer.sportradar.com/files/indexHockey.html)  :trophy: | :heavy_check_mark: | :heavy_check_mark: |
| [Tennis](https://developer.sportradar.com/files/indexTennis.html)  :tennis: | :heavy_check_mark: | :heavy_check_mark: |
| [MLB](https://developer.sportradar.com/files/indexBaseball.html)  :baseball: | :heavy_check_mark: | :heavy_check_mark: |
| [Darts](https://developer.sportradar.com/files/indexDarts.html)   :dart:   | :heavy_check_mark: | :heavy_check_mark: |
| [Beach volleyball](https://developer.sportradar.com/files/indexVolleyball.html) :palm_tree: | :heavy_check_mark: | :heavy_check_mark: |
| [Golf](https://developer.sportradar.com/files/indexGolf.html) :golf: | :heavy_check_mark: | :heavy_check_mark: |
| [NASCAR](https://developer.sportradar.com/files/indexRacing.html#official-nascar-api) :red_car: | :heavy_check_mark: | :heavy_check_mark: |
| [LoL](https://developer.sportradar.com/files/indexeSports.html) :video_game: | :heavy_check_mark: | :heavy_check_mark: |
| [Dota2](https://developer.sportradar.com/files/indexeSports.html) :video_game: | :heavy_check_mark: | :heavy_check_mark: |
| [Cricket](https://developer.sportradar.com/files/indexCricket.html) :cricket: | :heavy_check_mark: | :heavy_check_mark: |
| [Rugby](https://developer.sportradar.com/docs/read/rugby/Rugby_v2) :rugby_football: | :heavy_check_mark: | :heavy_check_mark: |

## Installation
The easiest way to start using this package is via [PyPI](https://pypi.org/project/sportradar/) using `pip`:

`$pip install sportradar`

If you'd prefer to clone the repository and install the package manually, follow these steps:
1. Clone this repo:
`$git clone https://github.com/johnwmillr/SportradarAPIs.git`
2. Enter the cloned directory:
`$cd SportradarAPIs`
3. Install:
`$python setup.py install`

## Usage
Below is a brief demonstration of how to use the package to download data for the 2018 FIFA World Cup.

```python
from sportradar import Soccer

# Create an instance of the Sportradar Soccer API class
sr = Soccer.Soccer("paste your api key here")

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
            teams.append(sr.get_team_profile(team_id).json())
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
