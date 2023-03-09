---
id: wq47kompa7e6bb61ovt4rug
title: Negotiation
desc: ''
updated: 1668961731236
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
- **When you want something, you always have to propose something in return**
- **When you say what your expectations are, this is the max you'd get. This is the first number in the deal and be careful when setting it**
- The first number you give should be high but also justifiable!

Common tasks:
- extend deadline = buys you negotiation time
- create auction
- click with recruiter, feel their vibe
- find upper bound of their budget

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

- заплата
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

week 4 They do not have more budget for this position. I have maxed out what they can give me

Overall the negotiation went the best possible way. I could extend the deadline, found their max budget and could click with
the recruiter and be on the same vibe.


## Yelp
week 0 - asked for expectations

week 1- made me offer which is below my expectations by 10k. I asked if they can make a raise

They gave me 1 week deadline, a bit pushy in my opinion. Not sure if they are in a hurry or not. They seem keen to hire me
as gave me IC3 level.

week 1 super small increase on salary, as I did not push for it and was not able to react straight away in the conversation.
I was not clear in what I wanted.... Said that my TC expectation is 125 but di not say how exactly to reach that TC
Should have said something like if you make my base x then I will sign the contract. I instead said something like if you
could come closer to the 125 TC the I will be happy.

When you want something, you always have to propose something in return! So basic advice...

Summary: Made me good offer, but I am left with the feeling I did not optimize my negotiation process. I am not confident
that I have maxed out their budget. Also problem was that I did not have good enough competing offer to show them. So
it was a bit tricky to find their maximum.

Clicking with the recruiter was a bit harder too. I could not 'feel' her vibe.

## Capital One
week 1 made me offer. I asked for 20% bump and said would stop other interviews and they did offer me that bump. Closed deal.

---

**Examples. Salary Negotiation**

## Yelp

### Chit chat
London weather was pretty nice last week, with lots of sunshine so I did enjoy that a lot. It one of the things London misses and we do not get
it that much.

### HR Questions

Thank you for having this catch-up. I wanted to have it because I have some questions about yelp and the offer which I wanted to ask you

- As far as I understand most people work remotely at Yelp and that also includes the DS position for MultiLoc. I am generally quite flexible whether to WFH or office and do not have strong preference for either. But still I want  to ask what are the plans at Yelp in terms of return to office vs remote work for the future.

- Given that most of the work is done remotely and for this position I will be based in London, are people allowed to work from different locations from other cities in the UK or even outside the UK? It's not like I have any plans to move out from London, I love it here, I am just asking.

-  The offer has 150k dollars gross in stocks. How much of this amount would be taxed?
-  Did you have the chance to talk with the hiring comitte regarding the compensation update we talked about on Tuesday?

### Salary expectations

After I had the call with Boris yesterday and he explaned on what I will be working on, I am keen on joining Yelp. I do think that is a great place to be at and I enjoyed a lot all the  conversations I had so far - with you on Tuesday, with Jackie in the begining, then I met Sebastian on the first technical and finally I liked the interviews with Kristen, Samantha and Feud. They are all cool and smart people and I can see myself working with you guys.

If you can increase the base to 95k then the Total compensation of you offer would match my intial expectations of 125, then I would be very keen on jump in your ship and sign the contract. That's my current position in terms of compensation package.

 If you are asked "How much does the other company offer?" - 120k in cash



## Smarkets

27.07.2022
My current offer is 100k cash + 15k Stocks. 

Would you be able to match that? If not can you ask what is the closest amount to which you get to this figure of 115k

I do want  to work at Hanson with you Ajay, Quiang, Alexandru, Simon and you.
I think you are a cool bunch of people to hang out with.

That's why I want to try to make this work and was wondering if its part of your budget to meet my competing offer.

---

ASK FOR SIGN ON BONUS

first of all I want to thank you for organising the whole interview process. It was a pleasure for me to meet you guys and I really enjoyed the chats that I had.

I really appreciate this opportunity and this was probably one of the smoothest interview processes I have ever had. You were very responsive to emails and gave feedback after interviews very quickly.

I am also very happy to hear that I receive this offer for a Quant. It is what I want to do and would love to do it at your company with the people I met during the interviews. It is a good offer and I am greatful for it. I will need some time to think about it because I am actively interviewing at other places as well.


Is the price negotiatable?

Email - catch up before the weekend 

# CHIT CHAT
How was your week? 
I am very good thanks. Yesterday I was in Nottingham for a trip with few of my collugues
and we went to Alton Towers which is a theme park in a village near Nottingham. It has lots of rollercoasters, a few cascles, mini golf and other attractions.
It was my first time on a rollercoaster so it was fun. Though it could be a bit stressful as some of the rides were inverted - your head was directed downwards and your legs upwards.
That was a bit scary, but yeah I am alife so it's fine.

# QUESTIONS
Let's get down to business.  Thank you for your time and for having this call. I wanted to have a quick catch up with you before the weekend, update you on my situation and ask some questions as well.

Do you know what are the future plans for Hanson? Cause last week I met Sean and this week I learn he is not in the company anymore. So there is some restructuring and I would like to know more about it.

How would that affect quants?
How many quant roles you are looking to fill?

I received the official offer on wednesday in hellosign and had the chance to read it. I have one question which is pretty standard and I am sure you have heard it many times: is the salary is negotiatable?

# SITUATION
In my opinion 99 is a very beautiful number symetric and 9 brings luck and success in asian culture. So 99 is beautiful, isn't it?

My situation is the following I am currently interviewing at many other places and for some of them the interviews will take long time which could go up to 15 weeks. 3 months + 3 months notice period = joining you next year - which super slow and  I realise is far from optimal for you and me. So in order to join Hanson early I will have to stop these interviews. However the salary ranges that these companies offer are between 100k and 130k and that its a bit higher than Hansons offer. Still as you should already know I did enjoy meeting you guys, there was definitely chemistry in the air during the inteviews, I can see myslef working with you guys, it was great experience and I am sure you also known there is a match, so i want to try to make this work. On the other hand i dont want to leave too much money on the table. So I wanted to ask you, are you a able to meet me in the lower bound of the range that is 100k 99k? If yes i am willing to consider stopping the other interview processes, start working for you as early as possible and sign the contract.

first 3 months 80k then 100k

## Anthony talk

Situation
- one of my onsites got delayed for next week (people take thier summer vactions now so its a bit slower)
- waiting result from another onsite
- flexible in terms of negotiation (sign on bonus?)
- appart from base salary do you offer other components such as sign-on bonuses

Questions
Last time I asked you last time about the plans for Hanson and the transition situation. Are there any further updates on that,
are there any changes I should know about  that happened between our last chat and now?

Yelp - onsite
DE Shaw, Akuna Capital, Hudson River Trading

## Trailstone

# Why interested
Quant Dev is the position I am interested in. I would like to build stuff for the front office team and help with making successfull trading strategies.
I am currently looking for a position which has the balance between  Software Engineering, Maths and Finance and that is why I applied for this position

Also after going through the whle interview prorcess I think you are cool bunch of people to hang out with. So yeah I would love to work with you.

# Salary
- is the salary negotiatable
- the salary range I am looking for is around 140k
- I currently have an offer for 120k so this is my lower bound. However, if you offer me 140k I will be able to make the decision much easier
as opposed if you matched this number. If you offer me 120k I will need to think about it, as the offer I currently have is based in London, on the other hand I can see my self working with you so I 'll I will have to think through it during the weekend.
- My offer is for a Quant dev position at a sports trading company

In terms of location, I do not have a strong preference to be in London or in Berlin. If I end up working at Trailstone I'd love to come down to Berlin and work with you.
However, as I am based in London and I just moved a few months ago, ideally I would like to stay here. And the offer I got from the other company is based in London.
So in the end if that's the only variable which differs in my two offers then I would choose to stay in London. But otherwise I am flexible in terms of location.

# Rank two places
In terms of role both places are exatly what I am looking for and that is Quant dev
In terms of culture both places are also very similar.
I am basically 50/50




















