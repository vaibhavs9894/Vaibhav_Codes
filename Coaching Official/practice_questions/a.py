## wap to create a list of names and then remove names that contain 'a' or 'o' char
names = ['DIVYA SRIVASTAVA','Ayushi Verma','Vaibhav Shrimali','Harshit Tripathi','Nikhil Jaiswal','Ridhi Mishra']

for char in names:
    for c in char:
        print(c)
        if (c=='a' or c=='o'):
            names.remove(char)
print(names) 