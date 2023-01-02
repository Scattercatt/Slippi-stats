def average_by_x(input_list: list, average_buffer: int = 5, ignore_nones: bool = False):
    if ignore_nones:
        for i in range(len(input_list)):
            input_list[i] = 0 if input_list[i] is None else input_list[i]

    data_avs = []
    for i in range(average_buffer):
        data_avs.append(0)
    if len(input_list) - average_buffer > 0:
        for i in range(len(input_list) - average_buffer):
            average_of_next_x_elements = sum(input_list[i:i+average_buffer]) / float(average_buffer)
            data_avs.append(average_of_next_x_elements)
    return data_avs