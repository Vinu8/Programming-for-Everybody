'''
9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program
creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the
file. After the dictionary is produced, the program reads
through the dictionary using a maximum loop to find the most
prolific committer.

'''
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mail_list = []
mail_dict = {}
biggest = None

for line in handle:
    if line.startswith('From '):
        from_line = line.split()
        email = from_line[1]
        mail_list.append(email)

        for email in mail_list:
            mail_dict[email] = mail_dict.get(email, 0) + 1
        
for key, value in mail_dict.items():
    if biggest == None or value > biggest:
        biggest = value
        freq_mail = key

print(freq_mail, biggest)
'''

# Refactored code

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_ids = []
email_dict = dict()

for line in handle:
    if line.startswith('From '):
        mail_list = line.split()
        email_ids.append(mail_list[1])

for i in email_ids:
    email_dict[i] = email_dict.get(i, 0) + 1

big_word = None
big_count = None
for key, value in email_dict.items():
    if big_count is None or value > big_count:
        big_count = value
        big_word = key

print(big_word, big_count)
         
