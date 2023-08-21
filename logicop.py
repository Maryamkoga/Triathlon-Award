#input participant details
intro = int(input("Enter participant number:"))
print("Hello Participant" , intro)

#input time taken to complete each event
swimming = int(input("Enter time taken to complete swimming event in minutes:"))
cycling = int(input("Enter time taken to complete swimming event in minutes:"))
running = int(input("Enter time taken to complete running event in minutes:"))

#total time to complete triathlon
total_time = swimming + cycling + running 
print("Total time taken to complete triathlon is" , total_time)

#determining award each participant gets
if total_time <= 100: 
    print("Provincial Colours")
#within 5 minutes
elif  total_time > 100 and total_time <= 105:
    print("Provincial Half Colours")
# within 10 minutes
elif total_time > 105 and total_time <= 110:
    print("Provincial Scroll")
else:
    print("No award")
