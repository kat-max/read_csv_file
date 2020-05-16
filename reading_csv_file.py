import csv


with open("csv_file.csv", "r") as csvfile:
    content = csv.reader(csvfile, delimiter=',')

    which_row = 0
    for row in content:
        if which_row == 0:
            which_row += 1
        else:
            print(f'{row[0]} is{row[2]} and{row[1]} years old.')
            which_row += 1
