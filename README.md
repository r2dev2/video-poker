# video-poker

Video poker project for Lynbrook Intro to CS.

## Setup

```bash
python3 setup.py
```

## Usage

### Single Player

#### Text-based

```bash
python3 game.py
```

With audio:

```bash
python3 game.py --audio
```

#### Gui-based

```bash
python3 gui.py
```

With audio:

```bash
python3 gui.py --audio
```

### Double Player

1. On each client, run ``python3 client.py``.
2. One person must enter player 1 and the other must enter that he or she is player 2.
3. Once ``Sending has started``, run ``python3 host.py`` on the machine which will host this.
4. In the clients, enter your name (5 chars or less).
5. Enter in the number of credits you have.
6. Enter how much you want to bet.
7. Enter the indeces of the cards you want to hold.
8. Enter ``Y`` to continue or ``N`` to stop.
9. The winning player is displayed in the terminal with ``host.py``.

## Other notes

* This project was made in an introduction to computer science class. Because of this, the code quality is not up to great standards.
* If running with audio is not working on your computer, you need to install vlc media player of the same version as your python. Example: for 32 bit python, you need 32 bit vlc.
* The multiplayer funcitonality uses predefined accounts on the Free Internet Chess Server. Therefore, two people cannot run the multiplayer at the same time. We did not know about servers during this project.
