# itd - In The Dark

An Adventure / Escape Game for python hackers.

# Recomandation for the best experience

The game is intended for "hacky" pythonistas. The ones who find their way, even in the dark !

You can do whatever you want to solve the game. But some behavior would lead to a lesser interesting experience.

We recommand to:
- Have autocompletion in your REPL (just pip install readline, or pyreadline if you don't)
- Avoid reading the `itd` package code, at least before you solved the game.
- Avoid inspecting any object named `ITD_*` and any attibutes named `_ITD_*`.
- Do not reload the `itd` package, it would reset your progression.

## Security Concern

You may wory about what the game is alowed to do, like format your drive or access and use sensible information.
But that is true for any game you install...

You can solve those concerns by inspecting the code, but that would ruin the experience for you.

You may however run the code inside a contained env like a docker or alike...

Note that this first episode of `In The Dark` does not require an internet connection.

# Usage

install `itd` in a virtual env:
```
$ python -m venv ITD.venv
$ source .\ITD.venv\bin\activate
(ITD.venv) $ pip install itd
```

If you don't have completion on your python REPL, install one.

You should try readline first: `pip install readline`

It may fail with a red warning (i.e. on Windows), in which case you can install pyreadline: `pip install pyreadline`


Run the python REPL and `import itd`, enjoy.
```
(ITD.venv) $ python
Python 3.7.0 ...
Type "help", "copyright", "credits" or "license" for more information.
>>> import itd

------------------------------------------------------------
| You just woke up.
| Your head hurts.
| You're in some sort of cockpit, all systems look down.
|
| You're in the dark...
| Let's search what's around here !
------------------------------------------------------------

[In The Dark] #1
You're in the dark...
Let's search what's around here !
```

Here is a first tip: there are a few way to "access" things in python, that's where you search when you're in the dark ;)
