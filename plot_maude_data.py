import matplotlib.pyplot as plt

def remove_parenthesis_newline(string):
    return string.strip('() ').replace('\n','')

#split by space if not inside parenthesis or nested parenthesis, remove new line
# spaces, trailing comma. Split data and convert to int/float
def get_data_from_string(string):
    open_parenthesis = 0
    splitted = []
    last_space_index = -1
    for i in range(len(string)):
        if string[i] == '(':
            open_parenthesis += 1
        elif string[i] == ')':
            open_parenthesis -= 1
        elif string[i] == ' ' and open_parenthesis == 0:
            sub_string = string[last_space_index+1:i].replace(' ','')
            if sub_string != '':
                sub_string = remove_parenthesis_newline(sub_string)
                sub_string = sub_string.split(',')
                data_tuple = float(sub_string[1])
                splitted.append(data_tuple)
            last_space_index = i

    sub_string = string[last_space_index+1:].replace(' ','')
    if sub_string != '':
        sub_string = remove_parenthesis_newline(sub_string).rstrip(',')
        sub_string = sub_string.split(',')
        data_tuple = float(sub_string[1])
        splitted.append(data_tuple)
    return splitted

def get_data_from_path(path):
    file = open(path, 'r')
    raw_data = file.read()
    raw_data = raw_data.replace('\n','')
    splitted_data = get_data_from_string(raw_data)
    return splitted_data

def calculate_violations(data, qa):
    violation_count = 0
    violation_expression = None
    if qa == 'aq':
        violation_expression = lambda d : d < 0
    elif qa== 'temp':
        violation_expression = lambda d : d < 18 or d >22

    for d in data:
        if violation_expression(d):
            violation_count += 1

    return violation_count

def main():
    comfort_temp_path = 'ComfortTempLog.txt'
    comfort_aq_path = 'ComfortAirqualityLog.txt'

    eco_temp_path = 'EcoTempLog.txt'
    eco_aq_path = 'EcoAirqualityLog.txt'

    meta_temp_path = 'MetaTempLog.txt'
    meta_aq_path = 'MetaAirqualityLog.txt'

    comfort_temp_data = get_data_from_path(comfort_temp_path)
    comfort_aq_data = get_data_from_path(comfort_aq_path)
    comfort_temp_violation = calculate_violations(comfort_temp_data, 'temp')
    comfort_aq_violation = calculate_violations(comfort_aq_data, 'aq')
    print('Comfort temp violation: ',comfort_temp_violation, ' AQ violation ',comfort_aq_violation)

    eco_temp_data = get_data_from_path(eco_temp_path)
    eco_aq_data = get_data_from_path(eco_aq_path)
    eco_temp_violation = calculate_violations(eco_temp_data, 'temp')
    eco_aq_violation = calculate_violations(eco_aq_data, 'aq')
    print('Eco temp violation: ',eco_temp_violation, ' AQ violation ',eco_aq_violation)

    meta_temp_data = get_data_from_path(meta_temp_path)
    meta_aq_data = get_data_from_path(meta_aq_path)
    meta_temp_violation = calculate_violations(meta_temp_data, 'temp')
    meta_aq_violation = calculate_violations(meta_aq_data, 'aq')
    print('Metacontrol temp violation: ',meta_temp_violation, ' AQ violation ',meta_aq_violation)


    fig, axs = plt.subplots(3, 2)
    fig.suptitle('Smart Home World')

    axs[0, 0].set_title("Comfort controller temperature")
    axs[0, 0].plot(comfort_temp_data)
    axs[0, 0].set(xlabel='Time step', ylabel='Temperature')
    axs[0, 0].axhline(y = 18, color = 'k', linestyle = '--')
    axs[0, 0].axhline(y = 22, color = 'k', linestyle = '--')

    axs[0, 1].set_title("Comfort controller air quality")
    axs[0, 1].plot(comfort_aq_data, 'r')
    axs[0, 1].set(xlabel='Time step', ylabel='Air quality')
    axs[0, 1].axhline(y = 0, color = 'k', linestyle = '--')

    axs[1, 0].set_title("Eco controller temperature")
    axs[1, 0].plot(eco_temp_data)
    axs[1, 0].set(xlabel='Time step', ylabel='Temperature')
    axs[1, 0].axhline(y = 18, color = 'k', linestyle = '--')
    axs[1, 0].axhline(y = 22, color = 'k', linestyle = '--')

    axs[1, 1].set_title("Eco controller air quality")
    axs[1, 1].plot(eco_aq_data, 'r')
    axs[1, 1].set(xlabel='Time step', ylabel='Air quality')
    axs[1, 1].axhline(y = 0, color = 'k', linestyle = '--')

    axs[2, 0].set_title("Meta controller temperature")
    axs[2, 0].plot(meta_temp_data)
    axs[2, 0].set(xlabel='Time step', ylabel='Temperature')
    axs[2, 0].axhline(y = 18, color = 'k', linestyle = '--')
    axs[2, 0].axhline(y = 22, color = 'k', linestyle = '--')

    axs[2, 1].set_title("Meta controller air quality")
    axs[2, 1].plot(meta_aq_data, 'r')
    axs[2, 1].set(xlabel='Time step', ylabel='Air quality')
    axs[2, 1].axhline(y = 0, color = 'k', linestyle = '--')

    plt.show()

if __name__ == "__main__":
    main()
