# Slippi-statss

Slippi stats is a collection of python scripts that use matplotlib to generate graphs of game data. 

## slp_stats.py

`slp_stats.py` can be run on the command line to generate graphs.

Arguments:

- `-n` `--player-code` The connect code of the player you want to run data on.
- `-s` `--stat` The stat you want to calculate
- `-c` `--character` If this argument is used, only games where the player plays a specific character are included.

An example command would look like this:

```bash
python -u slp_stats.py -n "SCTR#790" -s "lcancels" -c "Ganondorf"
```

## Dependencies

Make sure to run the following command to install [slippi-js](https://github.com/project-slippi/slippi-js) before trying to run any of the scripts

```bash
npm install @slippi/slippi-js```
