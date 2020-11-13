# Rohan's City Guesser

A game in which you must guess what city you are being shown!

## Getting Started

1. [Create a Reddit API Account](https://www.reddit.com/dev/api/)
2. Add your Reddit API Account Details to prawKeys.py
3. Run game.py
4. On your browser, navigate to your localhost with port 5000: localhost:5000

### Prerequisites

To run game.py you will need [Pyhton 3.0+](https://www.python.org/) installed.

## How to Play

- Upon loading you will see a photo of a city, with an entry field above and a scoreboard below.
- Type in the entry field your guess for what city it is
  - abbreviations **should** work ie. 'nyc' for 'New York City'
  - capitalizations do not matter, guesses and answers are not case-sensitive
  - accented symbols **should not** matter: eg. Montreal == Montréal
- Submit your guess and you will be greeted with the next picture, the previous round's outcome, and an updated scoreboard!

## Deployment

This system may be deployed to heroku for a live version of the site, Praw API data held in prawKeys.py should be reconfigured with environment variables.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web Framework
* [PRAW](https://praw.readthedocs.io/en/latest/) - The Python Reddit API Wrapepr
* [spaCy](https://spacy.io/) - Natural Language Processing (NLP)

## Authors

* **Rohan Dawar** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration: [GeoGuessr](https://www.geoguessr.com/) and [City Guesser](https://virtualvacation.us/guess)
* README.md template from [PurpleBooth](https://github.com/PurpleBooth)
* etc

