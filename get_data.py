import os
import json
import re

def get_slp_jsons(short_game_purge: bool = True, no_target_player_purge: bool = True, target_name: str = None, character_specific_purge: bool = None, target_character: str = None) -> list:
    ret = []
    os.chdir("slpfiles")
    all_dirs = os.listdir()
    for file_name in all_dirs:
        if re.search(r"\.slp", file_name):
            json_slp_file_name = os.path.splitext(file_name)[0] + ".json"
            if json_slp_file_name in all_dirs:
                print(f"Using existing json file for {file_name}.")
                with open(json_slp_file_name, "r") as json_file:
                    json_load = json.load(json_file)
                    if json_load["metadata"] is not False:
                        ret.append(json_load)
            else:
                print(f"Generating new json file for slp file {file_name}...")
                temp_dict = {}
                temp_dict["stats"] = json.loads(os.popen(f"node ../getstats.js {file_name}").read())
                temp_dict["players"] = json.loads(os.popen(f"node ../getplayers.js {file_name}").read())
                temp_dict["metadata"] = json.loads(os.popen(f"node ../getmetadata.js {file_name}").read())
                json_string = ""

                if len(temp_dict["metadata"]["players"]) > 2:
                    #Skip over replays with doubles or anything more than 2 players.
                    print(f"Skipping file {file_name} because it has more than 2 players")
                    json_string = '{"metadata" : false}'
                else:
                    json_string = json.dumps(temp_dict, indent = 4, sort_keys = True)
                    ret.append(temp_dict.copy())
                with open(json_slp_file_name, "w") as json_file:
                    json_file.write(json_string)
    
    os.chdir("..")

    if short_game_purge:
        print("Purging short games")
        ret = purge_short_games(ret)
    if no_target_player_purge:
        print("Purging games without target name")
        ret = purge_games_without_name(ret, target_name)
    if character_specific_purge:
        print(f"Purging games where the target player is not character {target_character}")
        ret = purge_games_without_character(ret, target_name, target_character)
            
    return ret

def purge_short_games(jsons: list, exclusion_time = 1800) -> list:
    ret = []
    for js in jsons:
        if js["metadata"]["lastFrame"] > exclusion_time:
            ret.append(js)
    return ret

def purge_games_without_name(jsons: list, target_name: str) -> list:
    ret = []
    for js in jsons:
        if js["players"][0]["connectCode"] == target_name or js["players"][1]["connectCode"] == target_name:
            ret.append(js)
    return ret

def purge_games_without_character(jsons: list, target_name: str, target_character: str) -> list:
    ret = []
    player_id = None
    character_id = character_to_id(target_character)
    for js in jsons:
        if js["players"][0]["connectCode"] == target_name:
            player_id = 0
        elif js["players"][1]["connectCode"] == target_name:
            player_id = 1

        if js["players"][player_id]["characterId"] == character_id:
            ret.append(js)
    
    return ret

def get_data_from_jsons(jsons: list, target_name: str, stat_path: list):
    data = []
    player_id = None
    for js in jsons:
        if js["players"][0]["connectCode"] == target_name:
            player_id = 0
        elif js["players"][1]["connectCode"] == target_name:
            player_id = 1
        else:
            print(f"WARNING: Target player '{target_name}' not found in file '{js['metadata']['startAt']}'")

        stat = js
        for key in stat_path:
            if key == "PLAYERID":
                stat = stat[player_id]
            else:
                stat = stat[key]
                
        data.append(stat.copy() if isinstance(stat, dict) else stat)
    
    return data

def character_to_id(character_name: str):
    CHARACTERS = {
        "falcon": 0,
        "dk" : 1,
        "donkey_kong" : 1,
        "fox" : 2,
        "g&w" : 3,
        "kirby": 4,
        "bowser": 5,
        "link": 6,
        "luigi": 7,
        "mario": 8,
        "marth": 9,
        "mewtwo": 10,
        "ness": 11,
        "peach": 12,
        "pikachu": 13,
        "ice_climbers": 14,
        "ics": 14,
        "jigglypuff": 15,
        "samus": 16,
        "yoshi": 17,
        "zelda": 18,
        "falco": 20,
        "young_link": 21,
        "yink": 21,
        "dr_mario": 22,
        "drmario": 22,
        "roy": 23,
        "pichu": 24,
        "ganondorf": 25,
        "ganon": 25
    }
    ret = CHARACTERS[character_name.lower()]
    if ret is None: 
        raise Exception("Invalid character")
    return ret 