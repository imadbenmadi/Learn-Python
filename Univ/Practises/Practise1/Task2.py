start_time_hourse = int(input("Enter the start time hourse: "))
start_time_minuts = int(input("Enter the start time minutes: "))
event_duration = int(input("Enter the event duration : "))
days = 0
start_time = start_time_hourse * 60 + start_time_minuts
end_time = start_time + event_duration

days = end_time // 1440
end_time = end_time % 1440
print("The end time is: ", days, "days and", end_time // 60, ":", end_time % 60)

