---
id: o78bfxkjzbeqkxuasv6bihf
title: CAP
desc: ''
updated: 1685095101907
created: 1684243822123
---
CAPI is a product which would help Yelp to measure attribution in a more accurate way. User tracking data using third parties such as IOS and Safari is becoming more difficult so we need to create our own API to do that. Our goal is to collect first party data.

**CAPI meeting**
- Kuny, UK London
- DS within Boris's MLOC Market intelligence and attribution team
- I've joined Yelp November last year, so that makes it a total of 7 months.

I am very excited to meet you all and I look forward to working with you on the Conversion API.

# Questions

Attribute transactions to Yelp's activity

Data.
- Who are the eligible clients for CAPI? And which of them we plan to use for the MVP?

Metrics.
- What is the match rate that we would consider the POC a success? And what was the match rate from the last POC?
- How many campaign data points we have for each client?
- What are the key KPI-s we want to track for our clients using CAPI?


FB CAPI is easy to setup almost no coding.


# Matching transactions to users and attribution of matched transactions

For CAPI we have 2 phases of matching and get 2 match rates in the end. First is match transactions to yelp users (using email, phone, zip etc.).This gives us Yelp users <> transactions match rate. Second, for the transactions we have matched yelp users we match to Yelp ads (that is attribution).  This gives us Yelp ads <> transactions match rate.
For the first step, when we match transactions with yelp users we can have two cases:
Transactions which have unique Yelp users (these we can use directly in ad attribution)
Transactions which have multiple Yelp users (due to not being able to define uniquely what a Yelp user is when using email, phone, zip). Now for each of these users we can have a score measuring the likelihood of being matched with this transaction. Say for a transaction with amount 100$ I have 3 users with scores 0.5, 0.4, 0.1. The question is how should we use these scores to compute ad attribution amount $?
Potential options:
Get only the user with maximum score 0.5 and match it to the transaction. If they have seen the ad, then we attribute 100$ otherwise we attribute 0$
Keep the 3 users matched to the transaction. If the first user has seen an ad we attribute 0.5*100$, otherwise 0. Do the same for user two and three and in the end add all 3 user attributions (weighted sum with indicator variables and scores are used as weights).
Get the user with the highest score 0.5 and match it to the transaction. If they has seen the ad, then we attribute 0.5*100$, if not we go to the second user and if they have seen the ad then we attribute 0.4*100$ and if they haven’t seen the ad we continue with the third user and so on.


In essence and assumptions:
Option 1 says: for each transaction match only the top user. Assumes each transaction can be attributed  to at most one user regardless of whether they have seen a Yelp ad  or not.
Option 2 says: for each transaction match all potential matchable users.  Assumes each transaction can be attributed to multiple users seeing an Yelp ad and the attributed amount is weighted using the likelihoods of these users being matched to the transaction.
Option 3 says: each transaction must be attributed to an Yelp ad. Rank users and go through them in decreasing order until there is a user who saw the ad to compute attribution.  Assumes each transaction is attributed to exactly one user seeing an Yelp ad.
Option 1 seems to me to be the most clean one as each transaction is mapped to at most 1 user. The other two would probably have higher attribution $$$ with Option 2 being strictly higher than Option 3, but aren’t they a bit unreal? 

Essentially, computing the second match rate Yelp ads <> transactions can be thought of as a 2 steps problem process. We want to find an estimate for P(transaction is attributed to a Yelp ad). That is equal to:
P(transaction is attributed to a Yelp ad| transaction is matched to Yelp user) * P(transaction is matched to Yelp user)
Steps:
1. Compute P(transaction is matched to Yelp user) := P(A)
2. Compute P(transaction is attributed to a Yelp ad| transaction is matched to Yelp user) := P(B|A)
Note these two probabilities P(A) and P(B|A) should be independent and only Option 1 computes them independently - firstly gets the maximum of users' scores that can match a transaction and then looks if a Yelp ad can be attributed to the transaction. Options 2 and 3 uses the scores (that is P(A)) to compute P(B|A) and hence these two probabilities would not be independent.

For now, Option 1 is the easiest to test out and is the most theoretically sound one, therefore is good to start with. Options 2 and 3 make sense only if we get very low scores (P(A) is very small) which means we cannot attribute any Yelp ad to a particular transaction with high confidence - then we could use these 2 options to “distribute” the attribution from a transaction to multiple Yelp users seeing a Yelp ad.
