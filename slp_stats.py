import argparse
import re
import matplotlib.pyplot as plt
from stat_parser import StatParser

def main(
    player_code: str,
    stat: str,
    character: str
        ):

    player_code = "SCTR#790"
    character = "Ganondorf"

    plt.style.use('seaborn-paper')

    lcancels_sp = StatParser(player_code, character)

    lcancels_sp.populate_lcancelratio()

    #populate_axis(jsons, x_axis, y_axis, player_code, "damageperopening")

    
    plt.plot(lcancels_sp.x_axis, lcancels_sp.y_axis)
    plt.title('LCancel stats vs time', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Amount', fontsize=14)
    plt.grid(True)
    plt.show()

    # print(get_data.get_data_from_jsons(jsons, player_code, ["stats", "overall", "PLAYERID", "inputsPerMinute", "ratio"]))
    # print(get_data.get_data_from_jsons(jsons, player_code, ["stats", "actionCounts", "PLAYERID", "lCancelCount", "fail"]))







# def populate_axis(jsons: list, x_axis: list, y_axis: list, target_name: str, stat_type: str = "lcancels") -> None:

#     data = []

#     for js in jsons:
#         replay_time = parse_time_var(js["metadata"]["startAt"])
#         player_id = None
#         if js["players"][0]["connectCode"] == target_name:
#             player_id = 0
#         elif js["players"][1]["connectCode"] == target_name:
#             player_id = 1
#         else:
#             print(f"WARNING: Target player '{target_name}' not found in file '{js['metadata']['startAt']}'")

        

#         # if stat_type == "lcancels":
#         #     lcancel_stats = js["stats"]["actionCounts"][player_id]["lCancelCount"]
#         #     success_percentage = lcancel_stats["success"] / (lcancel_stats["fail"] + lcancel_stats["success"]) * 100.0 if (lcancel_stats["fail"] + lcancel_stats["success"]) != 0 else None
#         #     y_axis.append((lcancel_stats["success"],lcancel_stats["fail"], success_percentage))

#         # elif stat_type == "inputsperminute":
#         #     y_axis.append(js["stats"]["overall"][player_id]["inputsPerMinute"]["ratio"])

#         # elif stat_type == "damageperopening":
#         #     y_axis.append(js["stats"]["overall"][player_id]["damagePerOpening"]["ratio"])

#         # elif stat_type == "openingsperkill":
#         #     y_axis.append(js["stats"]["overall"][player_id]["openingsPerKill"]["ratio"])

        
#         x_axis.append(replay_time)
    
#     x_axis.sort()
#     for i in range(len(x_axis)):
#         x_axis[i] = i

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