import argparse
import re
import matplotlib.pyplot as plt
from stat_parser import StatParser

def main(
    player_code: str,
    stat: str,
    character: str
        ):

    plt.style.use('seaborn-paper')

    lcancels_sp = StatParser(player_code, character)

    lcancels_sp.populate_lcancelratio()

    
    plt.plot(lcancels_sp.x_axis, lcancels_sp.y_axis)
    plt.title('LCancel stats vs time', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Amount', fontsize=14)
    plt.grid(True)
    plt.show()

def average_of_int_list(my_list: list) -> float:
    sum = 0
    none_count = 0
    for item in my_list:
        if item is not None:
            sum += item
    return sum / (len(my_list) - none_count)



def get_args() -> dict:
    parser = argparse.ArgumentParser(
        prog = "Slippi file stats",
        description = "Creates graphs of different melee stats from slp files."
    )
    parser.add_argument("-n", "--player-code", type = str, help = "The connect code of the player you want to run data on.")
    parser.add_argument("-s", "--stat", type = str, help = "The stat you want to calculate")
    parser.add_argument("-c", "--character", type = str, help = "If this argument is used, only games where the player plays a specific character are included.")

    args = parser.parse_args()

    return args



if __name__ == "__main__":
    main(**vars(get_args()))