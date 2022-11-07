

d_log = {6:(),7:(('Eric','e')),8:(('John','e'),('Michael','e'),('Eric','x')),9:(),10:(('Terry','e'), ('Eric','e'),('John','x'),('John','e')),
         11:(('John','x'),('Michael','x'))}

amout_inside = 0
# iterates the dict
for time in d_log:
    entry_list, exit_list = [], []
    entry_str, exit_str = '', ''
    comma_ = ''
    # check if having nobody passed door
    if d_log[time] == ():
        print(f'Between {time} and {time + 1} has nobody passed door. ({amout_inside} inside)')
        continue
    # get data of user
    for data in d_log[time]:
        # check if data has 2 or more tuple
        if isinstance(data,tuple):
            # add the name to list of entry or exit
            if data[1] == 'e':
                entry_list.append(data[0])
                amout_inside +=1 # increase amount of people inside by 1 if having entry
            if data[1] == 'x':
                exit_list.append(data[0])
                if amout_inside > 0 : amout_inside -= 1  # decrease amount of people inside by 1 if having exit
        # if data has 1 tuple:
        else:
            # add the name to list of entry or exit
            if d_log[time][1] == 'e':
                entry_list.append(d_log[time][0])
                amout_inside += 1  # increase amount of people inside by 1 if having entry
                break
            else:
                exit_list.append(d_log[time][0])
                if amout_inside > 0 : amout_inside -= 1  # decrease amount of people inside by 1 if having exit
                break
    # choose the separator that is compatible: "only", "and", "," ...
    if len(entry_list)== 0:
        entry_str = ''
    elif len(entry_list) == 1:
        entry_str = f' only {entry_list[0]} entered'
    elif len(entry_list) == 2:
        entry_str = f' {entry_list[0]} and {entry_list[1]} entered'
    else:
        entry_str = ' '+ ', '.join(entry_list[0:-1:1]) + ' and ' + entry_list[-1] + ' entered'

    if len(exit_list) == 0:
        exit_str = ''
    elif len(exit_list) == 1:
        exit_str = f' only {exit_list[0]} exited Secure area'
    elif len(exit_list) == 2:
        exit_str = f' {exit_list[0]} and {exit_list[1]} exited Secure area'
    else:
        exit_str = ' '+ ', '.join(exit_list[0:-1:1]) + ' and ' + exit_list[-1] + ' exited Secure area'

    # the comma between entry and exit
    if entry_str != '' and exit_str != '':
        comma_ = ','
    print(f'Between {time} and {time + 1}' + entry_str + comma_ +  exit_str + '.' + f'({amout_inside} inside)')

# Output:
# Between 6 and 7 has nobody passed door. (0 inside)
# Between 7 and 8 only Eric entered.(1 inside)
# Between 8 and 9 John and Michael entered, only Eric exited Secure area.(2 inside)
# Between 9 and 10 has nobody passed door. (2 inside)
# Between 10 and 11 Terry, Eric and John entered, only John exited Secure area.(4 inside)
# Between 11 and 12 John and Michael exited Secure area.(2 inside)