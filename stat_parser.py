import get_data
import re
from list_tools import average_by_x

class StatParser:
    def __init__(self, target_name: str = None, target_character: str = None, perge_short_games: bool = True) -> None:
        self.x_axis = []
        self.y_axis = []
        self.target_name = target_name
        self.target_character = target_character
        self.jsons = get_data.get_slp_jsons(perge_short_games, True, target_name, True, self.target_character)

        self.__STAT_TYPES = {
            "lcancelratios" : self.__populate_lcancelratio,
            "neutralwinratios" : self.__populate_neutralwinratio,
            "openingsperkillratios" : self.__populate_openingsperkillratio
        }


    #Populates the X axis in such a way that every file is places equally apart in order of time; regardless of how far appart in time each replay may have happened
    def populate_x_axis_equal_time_spacing(self) -> None:
        for js in self.jsons:
            replay_time = self.parse_time_var(js["metadata"]["startAt"])
            self.x_axis.append(replay_time)
        self.x_axis.sort()
        for i in range(len(self.x_axis)):
            self.x_axis[i] = i
    
    #Populate the y axis with a list of data
    def populate_y_axis_basic(self, data: list) -> None:
        for dat in data:
            self.y_axis.append(dat)
    
    def parse_time_var(self, time_str: str) -> int:
        ret = re.split(r"-|:|T|Z", time_str)
        ret = "".join(ret)
        return int(ret)

    def __populate_lcancelratio(self):
        self.populate_x_axis_equal_time_spacing()

        data_success = get_data.get_data_from_jsons(self.jsons, self.target_name, ["stats", "actionCounts", "PLAYERID", "lCancelCount", "success"])
        data_fail = get_data.get_data_from_jsons(self.jsons, self.target_name, ["stats", "actionCounts", "PLAYERID", "lCancelCount", "fail"])
        data_ratios = []
        for i in range(len(data_success)):
            data_ratios.append(data_success[i] / (data_success[i] + data_fail[i]) * 100.0 if (data_success[i] + data_fail[i]) > 0 else 0)
        
        data_avs = average_by_x(data_ratios, 20)

        self.populate_y_axis_basic(data_avs)

    def __populate_neutralwinratio(self):
        self.populate_x_axis_equal_time_spacing()

        data = get_data.get_data_from_jsons(self.jsons, self.target_name, ["stats", "overall", "PLAYERID", "neutralWinRatio", "ratio"])

        data = average_by_x(data, 120, True)

        self.populate_y_axis_basic(data)
    
    def __populate_openingsperkillratio(self):
        self.populate_x_axis_equal_time_spacing()

        data = get_data.get_data_from_jsons(self.jsons, self.target_name, ["stats", "overall", "PLAYERID", "openingsPerKill", "ratio"])

        data = average_by_x(data, 120, True)

        self.populate_y_axis_basic(data)

    def populate_stat(self, stat: str) -> None:
        if self.__STAT_TYPES.get(stat, 0):
            self.__STAT_TYPES[stat]()
        else:
            raise Exception(f"Attempted to populate stats with the stat \"{stat}\" on StatParser object {self}")



        



    

