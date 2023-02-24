# Mutation testing (FizzBuzz)

The application demonstrating how mutation testing works, presented at
[Pykonik Tech Talks #61](https://www.pykonik.org/tech-talks/61/).

Mutation tests are presented here using a simple game example:
[FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz).

Slides from the presentation can be found
[here](https://docs.google.com/presentation/d/1yjj20pcdqeyP7RSm9Ydikde8Khv_XT239jPKBTWBFpU/edit?usp=sharing).

## Prerequisites

* Python 3.9

## Setup

* Create a new, clean virtual environment with Python 3.9
* Install requirements:

      pip install -r requirements.txt

## Usage

* Run the FizzBuzz script:

      python fizzbuzz.py 1 15

* Run tests without mutations:

      pytest

* Run tests with mutations:

      mutmut run
      mutmut results
      mutmut show <id>
