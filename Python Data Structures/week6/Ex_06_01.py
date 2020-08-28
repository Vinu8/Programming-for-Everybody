'''
10.2 Write a program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line
by finding the time and then splitting the string a second
time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out
the counts, sorted by hour as shown below.

'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = []
hour = []
hour_dict = {}

for line in handle:
    if line.startswith('From '):
        wds = line.split()
        time = wds[5].split(':')
        hour.append(time[0])


for i in hour:
    hour_dict[i] = hour_dict.get(i, 0) + 1

hour_sorted = sorted([(k,v) for k,v in hour_dict.items()])

for key, val in hour_sorted:
    print(key, val)
