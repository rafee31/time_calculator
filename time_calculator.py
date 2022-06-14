def add_time(start, duration, day_of_week=False):

  days_index={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
  days_array=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

  duration_tuple=duration.partition(":")
  duration_hrs=int(duration_tuple[0])
  duration_mins=int(duration_tuple[2])

  start_tuple=start.partition(":")
  start_hrs=int(start_tuple[0])
  start_mins_tuple=start_tuple[2].partition(" ")
  start_mins=int(start_mins_tuple[0])
  am_pm=start_mins_tuple[2]
  am_pm_flip={"AM":"PM","PM":"AM"}

  amount_of_days=int(duration_hrs/24)

  end_mins=start_mins+duration_mins
  if(end_mins>=60):
    start_hrs+=1
    end_mins=end_mins%60

  amount_of_am_pm_flips=int((start_hrs+duration_hrs)/12)
  end_hrs=(start_hrs+duration_hrs)%12

  if(am_pm=="PM" and start_hrs+(duration_hrs%12)>=12):
    amount_of_days+=1
  
  if(end_mins<=9):
    end_mins="0" + str(end_mins)

  if(end_hrs==0):
    end_hrs=12

  if(amount_of_am_pm_flips%2==1):
    am_pm = am_pm_flip[am_pm]

  return_time=str(end_hrs)+ ":" + str(end_mins) + " "+ am_pm

  if(day_of_week):
    day_of_week=day_of_week.lower()
    index=int((days_index[day_of_week]) + amount_of_days) %7
    new_day=days_array[index]
    return_time += ", " + new_day

  if(amount_of_days==1):
    return return_time + " " + "(next day)"
  elif(amount_of_days>1):
    return return_time+ " (" + str(amount_of_days) + " days later)"

  return return_time