from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# object of sentiment analyzer
sia = SentimentIntensityAnalyzer()

sentences = [
    "Plenty of good food and fresh air will do more good than drugs.",
    "It needs a hearty shock to enable us to shake off that bad habit.",
    "Get out from here",
    "Thanks for sharing information"
]

for sentence in sentences:
    print(f'For the sentence "{sentence}"')
    polarity = sia.polarity_scores(sentence)
    
    pos = polarity["pos"]
    neu = polarity["neu"]
    neg = polarity["neg"]
    print(f'The % of positive sentiment in "{sentence}" is {round(pos*100,2)} %')
    print(f'The % of neutral sentiment in "{sentence}" is {round(neu*100,2)} %')
    print(f'The % of negative sentiment in "{sentence}" is {round(neg*100,2)} %') 

    