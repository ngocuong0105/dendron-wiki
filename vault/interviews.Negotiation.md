---
id: wq47kompa7e6bb61ovt4rug
title: Negotiation
desc: ''
updated: 1658958341918
created: 1658763383237
---
General tips:
- when they give offer, thank and ask **straight away** whether it is negotiable - sets expectations that you need more.
- use closing deal quickly to get raises, i.e. say I would stop interviewing if you offer x
- always show interest in the company
- competing offers always help...
- you need to click with the recruiter
- search for opportunities to have casual chats/laughs
- try to create a friendly chit chat atmosphere
- money talks should sound casual as if you are just chatting
- delay salary negotiation as late as possible in the interview process
- probation period salary x, if successful salary 1.3x ?
- set three numbers in your head, min, mid, max
- set your goals - what you want...
- **whenever you ask for increase you need to show interest in working for the company!**
They should not feel as if you are just using them to get counter offers


## Evaluating offers framework
- TC
- skills dev
    - Python
    - SQL
    - new technologies/languages
- smartness of coworkers
- potential mentors
- probability to click with coworkers
- probability get annoyed by coworkers
- probability I want to stay >= 1 year
- probability I want to stay >= 2 years
- probability I want to stay >= 3 years
- career dev in 1 year
- career dev in 2+ years
- how much value does it add to CV
    - role prestigiousness
    - company prestigiousness
- rate how interesting is the job
- rate how challenging is the job
- probability to get fired
- opportunities for career switch if don't like it
- free time to study on your own
Bulgarian version for asking dad advice

- заплата 90k
- развитие на технически умения 8/10
- умни колеги 8/10
- умни ментори 7/10
- работа в екип 8/10
- вероятност да остана +1 год 80%
- вероятност да остана +2 год 60%
- вероятност да остана +3 год 40%
- кариерно развитие след 1 год 7/10
- кариерно развитие след 2 год 7/10
- добавена стойност в CV 8/10
- престиж в компания 5/10
- престиж позиция 9/10
- интересна работа свързана с математика 8/10
- колко е трудна работата 8.5/10
- вероятност да ме уволнят 35%
- възможности да сменя работата след това 8/10
- възможност да си прави домашно 4/10

- заплата 115k
- развитие на технически умения 7/10
- умни колеги 6.5/10
- умни ментори 7/10
- работа в екип 5.5/10
- вероятност да остана +1 год 80%
- вероятност да остана +2 год 70%
- вероятност да остана +3 год 30%
- кариерно развитие след 1 год 5/10
- кариерно развитие след 2 год 6/10
- добавена стойност в CV 8/10
- престиж в компания 8/10
- престиж позиция 7/10
- интересна работа свързана с математика 7/10
- колко е трудна работата 7/10
- вероятност да ме уволнят 15%
- възможности да сменя работата след това 8/10
- възможност да си прави домашно 8/10

Comparison plot
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

COMPANY_NAME_1 = 'Smarkets'
COMPANY_NAME_2 = 'Yelp'
VALS_ONE = [8,8,7,8,8,6,4,7,7,8,5,9,8,8.5,10-3.5,8,4]
VALS_TWO = [7,6.5,7,5.5,8,7,3,5,6,8,8,7,7,7,10-1.5,8,8]

fields = ['технически умения', 'умни колеги', 'умни ментори', 'работа в екип', 'вероятност да остана +1 год', 'вероятност да остана +2 год',
'вероятност да остана +3 год', 'кариерно развитие след 1 год', 'кариерно развитие след 2 год', 'добавена стойност в CV',
'престиж в компания', ' престиж позиция', 'интересна работа свързана с математика', 'колко е трудна работата',
'вероятност да НЕ ме уволнят', 'възможности да сменя работата след това', 'възможност да си прави домашно']


df = pd.DataFrame()
df['fields'] = fields + fields
df['company_name'] = [COMPANY_NAME_1] * len(fields) + [COMPANY_NAME_2] * len(fields)
df['value'] = VALS_ONE + VALS_TWO

sns.barplot(x = 'value', y = 'fields', hue= 'company_name', data = df, ci = None,  orient = 'h',)
sns.set(rc={'figure.figsize':(11.7,8.27)})
plt.show()

print(df.groupby('company_name').describe())
```


## Smarkets

week 1 - made me an offer, I asked for increase

week 3 - offered to meet in the middle of the two sides

week 4 - I showed counter offer, lets see how they respond

They do not seem do be in a hurry so harder to close deal using the time argument. Now I got competing offer and will use that.

## Yelp
week 0 - asked for expectations

week 1- made me offer which is below my expectations by 10k. I asked if they can make a raise

They gave me 1 week deadline, a bit pushy in my opinion. Not sure if they are in a hurry or not. They seem keen to hire me as gave me IC3 level.

Tasks:
- say what your numbers in base are for which you can settle straight away


## Capital One
week 1 made me offer. I asked for 20% bump and said would stop other interviews and they did offer me that bump. Closed deal.

