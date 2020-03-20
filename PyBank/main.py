#Terrence Cummings
#03-Python Honework
#PyBank exercise

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
#Initialize counter and tracker variables to null
    num_months=0
    total_profit = 0
    month_data_list = []
    tot_m_to_m_change = 0
    max_incr = 0
    max_decr = 0
#for each month of data
    for row in csvreader:
#add current month's data to the list
        month_data_list.append(row)
#read the current month's data from the list
        current_month=month_data_list[num_months]
#read previous month's data from the list to get change
        prev_month_data = month_data_list[num_months-1]
#from the 2nd month add up the monthly change and check for max incr/decr
        if num_months !=0:
            m_to_m_change = int(current_month[1])-int(prev_month_data[1])
            if m_to_m_change >= max_incr:
                max_incr=m_to_m_change
                max_incr_month = current_month[0]
            if m_to_m_change<= max_decr:
                max_decr=m_to_m_change
                max_decr_month = current_month[0]
            tot_m_to_m_change=tot_m_to_m_change+m_to_m_change
#roll up sum of the total monthly profits
        total_profit = total_profit+int(current_month[1])
#increment the monthly counter variable
        num_months=num_months+1

#print table to terminal
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: "+str(num_months))
    print("Total: $"+str(total_profit))
    avg_change = tot_m_to_m_change/(num_months-1)
    print("Average Change: $"'{:.2f}'.format(avg_change))
    print("Greatest Increase in Profits: "+max_incr_month+" ($"+str(max_incr)+")")
    print("Greatest Decrease in Profits: "+max_decr_month+" ($"+str(max_decr)+")")

#print table to text file PyBank.txt
    f= open("PyBank.txt","w+")
    f.write("Financial Analysis \r\n")
    f.write("--------------------------------- \r\n")
    f.write("Total Months: "+str(num_months)+"\r\n")
    f.write("Total: $"+str(total_profit)+"\r\n")
    f.write("Average Change: $"'{:.2f}'.format(avg_change)+"\r\n")
    f.write("Greatest Increase in Profits: "+max_incr_month+" ($"+str(max_incr)+") \r\n")
    f.write("Greatest Decrease in Profits: "+max_decr_month+" ($"+str(max_decr)+") \r\n")
    f.close()

    