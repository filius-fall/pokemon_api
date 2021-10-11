

# Simple Pokemon battle

You can do simple Pokemon battle from python shell. You can 

## Pre-requisites

1. Python 3.3 or greater version



## Installation

1. Download the code by using

   ```
   $ git clone <link-to-repo>
   ```

   or Downloading the zip file and extracting it and then change directory to repo folder

   

2. Create a virtual environment using conda or python venv

   ```bash
   $ conda create -n <name-of-env> python=<any-version-after-3.3>
   					or
   $ python3 -m venv /path/to/new/virtual/environment
   ```

3. Install requirements

```
$ pip install -r requirments.txt
```

## Usage

execute run.py in pokemon folder

```bash
$ python3 run.py
```

Then it will prompt you to enter contender_1 name that is name of pokemon

```bash
$ python3 run.py
Contender 1 enter your pokemon name:

```

Then enter a valid pokemon name then it will prompt you to enter contender 2 name i.e., another pokemon name

```bash
$ python3 run.py
Contender 1 enter your pokemon name:
pikachu
Contender 2 enter your pokemon name:
```

Enter valid second pokemon name. Then it will ask you to mention the attack name

```
Contender 1 enter your pokemon name:pikachu
pikachu
Contender 2 enter your pokemon name:bulbasaur
bulbasaur
Contender 1 its your turn.
Enter your attack:
```

Now enter a valid attack of the pokemon. I will mention how to get list of attack names and stats of pokemon below

```
Enter your attack:thunder-punch
damage given by pikachu to bulbasaur for 2062.5
bulbasaur's health = 9579.081
Contender 2 its your turn
Enter your attack:energy-ball
damage given by bulbasaur to pikachu for 2205.0
pikachu's health = 9448.75

```

then enter second contender attack

When one of the contenders health falls below their hp they loose

```python
Contender 2 its your turn
Enter your attack:energy-ball
damage given by bulbasaur to pikachu for 2205.0
pikachu's health = 102
pikachu is dead. Contender 2 is winner
```



## Features

#### Pokemon stats

You can get stats of any pokemon.

First import Pokemon class from poke_api

```
$ python3
Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from poke_api import Pokemon

```

then initialise an instance for a pokemon name you want stats for

```
>>> pikachu = Pokemon('pikachu')
pikachu
>>> print(pikachu)
| Type            |   Value |
|-----------------+---------|
| hp              |      35 |
| attack          |      55 |
| defense         |      40 |
| special-attack  |      50 |
| special-defense |      50 |
| speed           |      90 |
>>> 
```



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
