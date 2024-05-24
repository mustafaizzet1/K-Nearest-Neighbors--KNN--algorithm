import csv
import tkinter as tk

data = [] #extracted first 8 column data from csv
outcome = [] #extracted outcome from csv

v_0=[]
v_1=[]
v_2=[]
v_3=[]
v_4=[]
v_5=[]
v_6=[]
v_7=[]

with open('diabetes.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Initialize lists to store data and outcome

    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the first 8 columns as data
        data.append(row[:8])
        v_0.append(row[:1][0])
        v_1.append(row[1:2][0])
        v_2.append(row[2:3][0])
        v_3.append(row[3:4][0])
        v_4.append(row[4:5][0])
        v_5.append(row[5:6][0])
        v_6.append(row[6:7][0])
        v_7.append(row[7:8][0])

        # Extract the ninth column onwards as outcome
        outcome.append(row[8:])


for i in range(8):
    exec(f"v_{i}.pop(0)")


v_0 = list(map(float, v_0))
v_1 = list(map(float, v_1))
v_2 = list(map(float, v_2))
v_3 = list(map(float, v_3))
v_4 = list(map(float, v_4))
v_5 = list(map(float, v_5))
v_6 = list(map(float, v_6))
v_7 = list(map(float, v_7))


v_0_max=max(v_0)
v_1_max=max(v_1)
v_2_max=max(v_2)
v_3_max=max(v_3)
v_4_max=max(v_4)
v_5_max=max(v_5)
v_6_max=max(v_6)
v_7_max=max(v_7)
v_max=[]

v_max.append(v_0_max)
v_max.append(v_1_max)
v_max.append(v_2_max)
v_max.append(v_3_max)
v_max.append(v_4_max)
v_max.append(v_5_max)
v_max.append(v_6_max)
v_max.append(v_7_max)


v_0_min=min(v_0)
v_1_min=min(v_1)
v_2_min=min(v_2)
v_3_min=min(v_3)
v_4_min=min(v_4)
v_5_min=min(v_5)
v_6_min=min(v_6)
v_7_min=min(v_7)

v_min=[]
v_min.append(v_0_min)
v_min.append(v_1_min)
v_min.append(v_2_min)
v_min.append(v_3_min)
v_min.append(v_4_min)
v_min.append(v_5_min)
v_min.append(v_6_min)
v_min.append(v_7_min)


for i in range(8):
    exec(f"print('v_{i}_max:', v_{i}_max)")


variables=data[0]
data.pop(0)
outcome.pop(0)

data_preprocessed=[]# preprocessed data


def writingtocsv(data_preprocessed):
    with open("diabetes_preprocessed.csv", 'w', newline='') as csvfile:
        # Creating a CSV writer object
        csvwriter = csv.writer(csvfile)
        # Writing the data row by row
        for row in data_preprocessed:
            csvwriter.writerow(row)

def standardization_calculation(list1,max_value,min_value):
    data_preprocessed = []
    list0 = []
    for value in range(len(list1)):
        if isinstance(list1[value], list):
            list0.append((list1[value] - v_min[value]) / (v_max[value] - v_min[value]))  # calculation for standardization
            data_preprocessed.append(list0)
        else:
            data_preprocessed.append((list1[value] - v_min[value]) / (v_max[value] - v_min[value]))
    return data_preprocessed

def preprocessing(dat):
    data_preprocessed=[]
    for values in dat:
        if isinstance(values, list):
            float_list = [float(x) for x in values] # converting str to float
            max_value=max(float_list)
            min_value=min(float_list)
            data_preprocessed.append(standardization_calculation(float_list,max_value,min_value))
        else:
            max_value = max(dat)
            min_value = min(dat)
            data_preprocessed = standardization_calculation(dat, max_value, min_value)
            break


    return  data_preprocessed





def euclidean_distance(point1,point2):
    squared_diff_sum = 0
    for i in range(len(point1)):
        squared_diff_sum += (point1[i] - point2[i]) ** 2

    return squared_diff_sum ** 0.5

def knn(point2,data_preprocessed,outcome,num):
    distance={}
    for point1 in data_preprocessed:
            length=euclidean_distance(point1, point2)
            distance[length]=int(outcome[data_preprocessed.index(point1)][0])
    sorted_dict_keys = dict(sorted(distance.items()))
    first_5_items = dict(list(sorted_dict_keys.items())[:num])
    return first_5_items

def validation(str_list):
    try:
        print(len(data))
        int_list = [float(x) for x in str_list]
        print(int_list)
        if (v_0_max >= int_list[0] and v_1_max >= int_list[1] and v_2_max >= int_list[2] and v_3_max >= int_list[3] and
            v_4_max >= int_list[4] and v_5_max >= int_list[5] and v_6_max >= int_list[6] and v_7_max >= int_list[7] and int_list[8] <= len(data)):
            print("truee")
            return int_list
        else:
            return None
    except ValueError:
        return None  # Return None to indicate validation failure


        return int_list
    except ValueError:
        print("Error: One or more elements in the list is not convertible to an integer.")
    return data
def get_inputs():
    inputs = [entry.get() for entry in entries]
    return inputs


def diabet_result(dictionary):
    count_1 = 0
    count_0 = 0

    # Iterate through the values of the dictionary and count occurrences of '1' and '0'
    for value in dictionary.values():
        print(value)
        if value == 1:
            count_1 += 1
        elif value == 0:
            count_0 += 1

    # Calculate the total count of values
    total_count = count_1 + count_0

    # Calculate the percentage of occurrences of '1' and '0'
    percentage_1 = (count_1 / total_count) * 100 if total_count > 0 else 0
    percentage_0 = (count_0 / total_count) * 100 if total_count > 0 else 0

    result=[]
    result.append(percentage_1)
    result.append(percentage_0)
    return result
    #return percentage_dict

def process_inputs():

    test_data = preprocessing(data)
    writingtocsv(test_data)
    inputs = validation(get_inputs())
    if inputs is None:
        result_label.config(text="Error: One or more inputs are not valid numbers.")
        return
    num = int(inputs[8])
    inputs.pop(8)
    preprocessed_data = preprocessing(inputs)

    result = knn(preprocessed_data,test_data,  outcome,num)
    result=diabet_result(result)
    return result

# Create the main window
root = tk.Tk()
root.title("Multiple Inputs GUI")
root.geometry("300x400")
# Create entry widgets for eight inputs
entries = []
variables.append("The number of closest records")
for i in variables:
    label = tk.Label(root, text=f"{i}:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

def display_result():
    result = process_inputs()
    result_label.config(text="Diabetes: " + str(result[0]) + ", Not: " + str(result[1]))

# Create a button to get the inputs and display result

button = tk.Button(root, text="Get Inputs and Display Result", command=display_result)
button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()

































