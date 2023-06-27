---
id: o78bfxkjzbeqkxuasv6bihf
title: CAPI
desc: ''
updated: 1686137478151
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

In the context of CAPI, our matching process consists of two phases, resulting in two match rates. The first phase involves matching transactions to Yelp users based on criteria such as email, phone, and zip code. This yields the match rate for Yelp users <> transactions. In the second phase, we match the transactions associated with Yelp users to Yelp ads, which determines the attribution match rate for Yelp ads <> transactions.
During the first step of matching transactions to Yelp users, we encounter two scenarios:
Transactions with unique Yelp users: In these cases, we can directly utilize the matched Yelp user for ad attribution.
Transactions with multiple potential Yelp users: Due to the ambiguity in uniquely identifying Yelp users based on email, phone, and zip code, we assign a likelihood score to each potential match.  Say for a transaction with amount 100$ we have 3 users with scores 0.5, 0.4, 0.1. The question is how should we use these scores to compute ad attribution amount $?
Potential options:
Select only the user with the highest score (0.5) and match them to the transaction. If this user has seen the ad, we attribute $100; otherwise, we attribute $0.
Retain all three users matched to the transaction. If the first user has seen the ad, we attribute 0.5 * $100; otherwise, we attribute $0. We apply the same logic for the second and third users. Finally, we sum up the attributions for all three users, using the scores as weights (weighted sum with indicator variables and scores are used as weights).
Choose the user with the highest score (0.5) and match them to the transaction. If this user has seen the ad, we attribute 0.5 * $100. If they haven't seen the ad, we proceed to the second user and attribute 0.4 * $100 if they have seen the ad. This process continues for subsequent users until a user who has seen the ad is found.
Same as Option 2, but instead of using simple weighted average, we can use inverse propensity weighting (IPTW). This is a better option when we get scores that are very small.


In essence and assumptions:
Option 1 says: for each transaction match only the top user. Assumes each transaction can be attributed  to at most one user regardless of whether they have seen a Yelp ad or not.
Option 2 says: for each transaction match all potential matchable users.  Assumes each transaction can be attributed to multiple users seeing an Yelp ad and the attributed amount is weighted using the likelihoods of these users being matched to the transaction.
Option 3 says: each transaction must be attributed to an Yelp ad. Users are ranked, and we proceed in descending order until a user who has seen the ad is found. Attribution is computed accordingly.  Assumes each transaction is attributed to exactly one user seeing an Yelp ad.

The order of attribution amounts would likely be Option 2 > Option 3 > Option 1.
Although Option 1 would give us the smallest attribution it appears to be the cleanest approach as each transaction is associated with a maximum of one user (which is what we want, each transaction can be attributed to at most one Yelp user).

Option 1 interpretation
To compute the second match rate (Yelp ads <> transactions), we can conceptualize it as a two-step process.  We aim to estimate P(transaction is attributed to a Yelp ad), which can be expressed as:  P(transaction is attributed to a Yelp ad| transaction is matched to Yelp user) * P(transaction is matched to Yelp user). The two steps involved are as follows:
1. Compute P(transaction is matched to Yelp user) := P(A)
2. Compute P(transaction is attributed to a Yelp ad| transaction is matched to Yelp user) := P(B|A)
Note that these two probabilities, P(A) and P(B|A) should be independent. Only Option 1 calculates them independently by first obtaining the maximum score among users that can match a transaction and subsequently determining if a Yelp ad can be attributed to the transaction.  Options 2 and 3 uses the scores (0.1, 0.4, 0.5 that is P(A)) to compute P(B|A) and hence these two probabilities would not be independent.

For now, Option 1 is the easiest to test out and is the most theoretically sound one, therefore is good to start with. Options 2 and 3 can become relevant only if we encounter very low scores (indicating a small likelihood, P(A) )  and are unable to confidently attribute a Yelp ad to a specific transaction. In such cases, we could use Options 2, 3 and 4  to “distribute” the attribution from a transaction to multiple Yelp users seeing a Yelp ad.

Options 2 and 4 interpretation
These two options use the scores (P(transaction is matched to Yelp user), P(A)) to compute weighted average of the transaction amount. Philosophically speaking we want each transaction to be attributed to at most one Yelp user. These options do not reflect this philosophy. Rather, they match each transaction to multiple users with different levels of certainty, where the levels are measured using these scores. Options 2 and 4 offer a probabilistic point of view of the problem and their main advantage is that we would get more stable results over time, that is attribution amounts would not differ a lot month over month because we use averaging.