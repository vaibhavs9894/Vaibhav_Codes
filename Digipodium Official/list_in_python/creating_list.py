numbers = [1,2,3,4,5,6]
names = ['ravi','ashi','neha','ajay','ritu','raju']

heights = ['ravi',5.6,'ashi',6,'neha',5.1]
info = [True,True,False,True,False]

marks_per_year = [[45,67,45],[67,78,89],[89,89,90]]
teams =[['raju','raja','rani'],['jack','jamie'],['alex','alan']]
smileys= ['😃','✨','😭']

print(numbers,'size = ' ,len(numbers))
print(names,'size = ' ,len(names))
print(heights,'size = ' ,len(heights))
print(marks_per_year,'size = ' ,len(marks_per_year))
print(info,'size = ' ,len(info))
print(teams,'size = ' ,len(teams))
print(smileys)

# generating a large list
one_crore_items = list(range(1,10000001))
even_list = list(range(2,201,2))
print(even_list)