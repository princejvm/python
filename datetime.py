from datetime import datetime

now=datetime.now()
print now
print now.year
print now.month
print now.day

""" Print the current date in the form of 
mm/dd/yyyy. """

print '%s/%s/%s' % ( now.month, now.day,now.year)     

# print the current time in the pretty form of hh:mm:ss.
print '%s:%s:%s' % ( now.hour, now.minute,now.second)
