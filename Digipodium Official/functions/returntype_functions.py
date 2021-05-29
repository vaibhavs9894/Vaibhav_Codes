def mean(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)
m1 = mean(1,2,3,4,5,6)
print(mean(1,2,3,3,4,5))
m2 = m1 * 10
print('meanx10',m2)

def word_counter(sentence):
    if sentence:
        words =  sentence.split()
        count = len(words)
        return count

from string import punctuation

def clean_punc(sentence):
    for char in punctuation:
        sentence = sentence.replace(char,'')
    return sentence

c1 = word_counter('')
c2 = word_counter('hi there, wh,at a,re u doi,ng. this is not easy. Well u got to code!!')

s = 'hi there, what are u doing. this is not easy. Well u got to code!!'
clean_s = clean_punc(s)
count = word_counter(clean_s)
print(s)
print(clean_s)
print(count)

c = word_counter(clean_punc(s))