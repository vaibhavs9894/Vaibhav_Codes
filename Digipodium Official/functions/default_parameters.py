def remove_punc(sentence,punctuation='!@#$%^&*()_+`:"[]'):
    for item in punctuation:
        if item in sentence:
            sentence = sentence.replace(item,'')
    print(sentence)

msg = "hi there, )*(!@#*where is th*)(&!@)#e secre!@#)(!*@#)t for the:!@ treasure"
remove_punc(msg,'()*!@#*&:')
remove_punc(msg)

def summer(a,b,c=0,d=0):
    print(a + b + c + d)

summer(12,54)
summer(23,45,67)
summer(23,45,67,23)
summer(23,45,d=23)
summer(a=1,b=2,c=3)