def display_main_menu():

    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
 
 
def get_user_input():

    user_input = input()

    string_list = user_input.split(",")

    float_list = []
 
    for value in string_list:

        float_list.append(float(value))
 
    return float_list
 
 
def calc_average(temperature_list):

    return sum(temperature_list) / len(temperature_list)
 
 
def find_min_max(temperature_list):

    return [min(temperature_list), max(temperature_list)]
 
 
def sort_temperature(temperature_list):

    return sorted(temperature_list)
 
 
def calc_median_temperature(temperature_list):

    sorted_list = sorted(temperature_list)

    n = len(sorted_list)

    middle = n // 2
 
    if n % 2 == 1:

        return sorted_list[middle]

    else:

        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
 
 
def main():

    display_main_menu()

    temperatures = get_user_input()
 
    print("Average:", calc_average(temperatures))

    print("Minimum and maximum:", find_min_max(temperatures))

    print("Sorted temperatures:", sort_temperature(temperatures))

    print("Median:", calc_median_temperature(temperatures))
 
 
if __name__ == "__main__":

    main()
 