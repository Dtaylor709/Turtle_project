from datetime import date, datetime


def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')


def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    return date.strftime('%B')


def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
        characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.

    Returns: the formatted string.
    '''
    return f"{text:<{spaces}}"


def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''
    # import csv

    # full_list = []

    # with open (file_name, encoding="utf-8" ) as csv_file:
    #     reader=csv.reader(csv_file)
    #     for line in reader:
    #         # next(reader,None) 
    #         full_list.append(line)

    # return full_list
    
    import csv
    reader = csv.reader(open("data/2020_2021_turtle_data.csv","r"))
    data = []
    for row in reader:
        data.append(row)
    return data
    # print(data)


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''
#     column_total = [
#         ["Nests", 0],
#         ["Hatched Nests", 0],
#         ["False Crawls",0],
#         ["Hit Rocks",0],
#         ["Nest Predation", 0],
#     ]

# # overall the last table
#     for row in monthly_data:
#         nests = row[1]
#         print
        # if column_total == "Nests":
        #     nest_list = row[1:1] + row[2:1]
        # print(nest_list)

    # import venv/numpy as np
    # np.add(first, second, third, fourth, fifth, sixth).tolist() 

    # print(list)
    #

    # nests_total = 0
    # false_crawls_total = 0
    # hit_rocks_total = 0
    # hatched_nests_total=0
    # nest_predation_total=0

    # for row in monthly_data:
    #     # nests_total = int(nests[1:1]) + int(nests[1:2])
    #     nests_total.append(row[1])
    #     # print("row",row[1:2])
    #     # print("row2",row[1:3])
    #     print(nests_total)
    #     # nests = nests_total + int(row[1])
    #     # false_crawls = row[2]
    #     # hit_rocks = row[3]
    #     # hatched_nests = row[4]
    #     # nest_predation = row[5]


    #     print("nests",nests_total)
        # datetime = convert_mmddyyyy_date(row[0])
        # Nests = int(sum(row[1])
        # print(Nests)

        # return date[0]
        # print(month)
        
        # if column == "Nests":
        #     list = items[0]
        #     nests = list[1] + int(row[1])
        #     monthly[0] = [month, nests]

                
    #        monthly = [
    #     ["October", 0],
    #     ["November", 0],
    #     ["December",0],
    #     ["January",0],
    #     ["February", 0],
    #     ["March",0]
    # ]
    # # nests = 0

    # for row in monthly_data:
    #     # print("row",row)
    #     # datetime = convert_mmddyyyy_date(row[0])
    #     month = row[0]
        
        
    #      if month == "October":
    #         october_list = monthly[0]
    #         nests = october_list[1] + int(row[1])
    #         monthly[0] = [month, nests]
    # nests = 0
    # false_crawls = 0
    # hit_rocks = 0
    # hatched_nests=0
    # nest_predation=0


    # # for day in data[1:]:
    # #     print(day[0])

    # print(monthly_data)
    # for item in monthly_data[1:]:
    #     print(item)
    #     nests += int(item[1])
    #     false_crawls += int(item[2])
    #     hit_rocks += int(item[3])
    #     hatched_nests += int(item[4])
    #     nest_predation += int(item[5])

    # # print(nests)
    # # print(false_crawls)
    # # print(hit_rocks)
    # # print(hatched_nests)
    # # print(nest_predation)

    # return [nests,false_crawls, hit_rocks, hatched_nests, nest_predation ]  
    pass

# def output_monthly_statistics(monthly_data):
#     '''Prints a summary of the total number of nests, hatched nests, false crawls,
#        hit rocks and nest predation per month.

#     Args:
#         monthly_data: a list of lists, where each sublist contains the month
#             name and total values for that month.
#     '''
#     # monthy stats the middle table
#     don't need function used daily function instead
   
#     pass

def output_nests_per_month_graph(monthly_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    # print(monthly_data)
    # first table

    # monthly = {
    # 'october':[],
    # 'november':[],
    # 'december': [],
    # 'january':[],
    # 'february': [],
    # 'march':[]
    # }
  
    monthly = [
        ["October", 0],
        ["November", 0],
        ["December",0],
        ["January",0],
        ["February", 0],
        ["March",0]
    ]
    # nests = 0

    for row in monthly_data:
        # print("row",row)
        # datetime = convert_mmddyyyy_date(row[0])
        month = row[0]
        # return date[0]
        # print(month)
        
        if month == "October":
            october_list = monthly[0]
            nests = october_list[1] + int(row[1])
            monthly[0] = [month, nests]
                    
        elif month == "November":
            month_list = monthly[1]
            nests = month_list[1] + int(row[1])
            monthly[1] = [month, nests]
        elif month == "December":
            month_list = monthly[2]
            nests = month_list[1] + int(row[1])
            monthly[2] = [month, nests]
        elif month == "January": 
            month_list = monthly[3]
            nests = month_list[1] + int(row[1])
            monthly[3] = [month, nests]
        elif month == "February": 
            month_list = monthly[4]
            nests = month_list[1] + int(row[1]) 
            monthly[4] = [month, nests]
        elif month == "March":
            month_list = monthly[5]
            nests = month_list[1] + int(row[1])
            monthly[5] = [month, nests]

        
    # print(monthly)

    return monthly

    # need to make the result show X instead of numbers
    

def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    # [nest count, false crawls, 37, 0, 2], # october
    monthly = [
        ["October", 0,0,0,0,0],
        ["November", 0,0,0,0,0],
        ["December",0,0,0,0,0],
        ["January",0,0,0,0,0],
        ["February", 0,0,0,0,0],
        ["March",0,0,0,0,0]
    ]

    # print(monthly)

    # for each day in the data
    #   check which month it is (calculate the month index - if month == "October", month index = 0)
    #   add the number of nests to the nest count for that month
    #       monthly[month index][0] = monthly[month index][0] + number of nests for that day (day[1])
    
    
    for row in data[1:]:
        # print(row)
        datetime = convert_mmddyyyy_date(row[0])
        month = get_month_name(datetime)
        # return date[0]
        # print(month)
        
        if month == "October":
            october_list = monthly[0]
            nests = october_list[1] + int(row[1])
            false_crawls = october_list[3] + int(row[2]) 
            hit_rocks = october_list[4] + int(row[3]) 
            hatched_nests = october_list[2] + int(row[4])          
            nest_predation = october_list[5] + int(row[5]) 
            monthly[0] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
                    
        elif month == "November":
            month_list = monthly[1]
            nests = month_list[1] + int(row[1])
            false_crawls = month_list[3] + int(row[2]) 
            hit_rocks = month_list[4] + int(row[3]) 
            hatched_nests = month_list[2] + int(row[4])          
            nest_predation = month_list[5] + int(row[5]) 
            monthly[1] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
        elif month == "December":
            month_list = monthly[2]
            nests = month_list[1] + int(row[1])
            false_crawls = month_list[3] + int(row[2]) 
            hit_rocks = month_list[4] + int(row[3]) 
            hatched_nests = month_list[2] + int(row[4])          
            nest_predation = month_list[5] + int(row[5]) 
            monthly[2] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
        elif month == "January": 
            month_list = monthly[3]
            nests = month_list[1] + int(row[1])
            false_crawls = month_list[3] + int(row[2]) 
            hit_rocks = month_list[4] + int(row[3]) 
            hatched_nests = month_list[2] + int(row[4])          
            nest_predation = month_list[5] + int(row[5]) 
            monthly[3] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
        elif month == "February": 
            month_list = monthly[4]
            nests = month_list[1] + int(row[1])
            false_crawls = month_list[3] + int(row[2]) 
            hit_rocks = month_list[4] + int(row[3]) 
            hatched_nests = month_list[2] + int(row[4])          
            nest_predation = month_list[5] + int(row[5]) 
            monthly[4] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
        elif month == "March":
            month_list = monthly[5]
            nests = month_list[1] + int(row[1])
            false_crawls = month_list[3] + int(row[2]) 
            hit_rocks = month_list[4] + int(row[3]) 
            hatched_nests = month_list[2] + int(row[4])          
            nest_predation = month_list[5] + int(row[5]) 
            monthly[5] = [month, nests, hatched_nests, false_crawls, hit_rocks, nest_predation]
    
    return monthly
    # print(monthly)
    # print(data[0])
    # for day in data[1:]:
    #     print(day[0])
        
        # print(date)
        
    

if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')
    
    # print(all_data)
    
    monthly_data = transform_daily_to_monthly(all_data)
    
    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')

    print()
    output_nests=output_nests_per_month_graph(monthly_data)
    
    print(f"Number of Nests recorded per month (X = 5 nests): ")
    for month in output_nests:
        number_x = round(month[1] / 5)
        print(f"{month[0]}: {month[1]} {'X'*number_x}")
    
    # output_monthly_statistics(monthly_data)
    
    print("Monthly statistics:")
    for month in monthly_data:
        print(f"{month[0]} {month[1]} {month[2]} {month[3]} {month[4]} {month[5]} ")
    
    output_overall_statistics(monthly_data)
    print("Overall:")



