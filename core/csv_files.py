import csv
#
# # First approach
# with open('/Users/abichevo/PycharmProjects/inerview_python/documents/apple_interview', 'r') as csv_file:
#     #csv_reader = csv.reader(csv_file, delimiter=',')
#     data = csv_file.readlines()
#     print(data)
#     for line in data[1::]:
#         line = line.strip(" ").split(",")
#         if len(line) == 6:
#             end_time = line[3]
#             start_time = line[2]
#             if int(end_time) - int(start_time) > 90 * 60:
#                 if int(line[-1]) > int(line[-2]):
#                     print(line[1])
#                 else:
#                     print(line[0])



# Second approach
#
# file = "Home Team,Away Team,Start Time,End Time,Home Score,Away Score\nGiants,Athletics,638988124,639009724,3,0\nYankees,Red Socks,640651324,640654924,5,2\nAstros,White Socks,672180124,672187324,1,4\nDodgers,Padres,677458504,677458624,12,9\nRockies,Marlins,674780224,674783944,8,9\nBlue Jays,Cardinals,674575144,674600344,7,15\nBlue Jays,Cardinals,674600344,7,15"
#
# data = file.split('\n')
# print(data)
# for line in data[1::]:
#     line = line.strip(" ").split(",")
#     if len(line) == 6:
#         try:
#             end_time = line[3]
#             start_time = line[2]
#             if int(end_time) - int(start_time) > 90*60:
#                 if int(line[-1]) > int(line[-2]):
#                     print(line[1])
#                 else:
#                     print(line[0])
#         except ValueError:
#             print("Wrong data, check the data provided.")

# Third aproach Dictionary.
with open('/Users/abichevo/PycharmProjects/inerview_python/documents/apple_interview', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            dict = {", ".join(row)}
            line_count += 1
        print(f'\t{row["Home Team"]} plays with {row["Away Team"]} start time is {row["Start Time"]}, end time is {row["Start Time"]}. The score is {row["Home Score"]}:{row["Away Score"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

print(dict)

