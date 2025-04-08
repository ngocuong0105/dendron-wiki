---
id: 9y9xx3g5m34va97bublk8pa
title: Second Price Auction
desc: ''
updated: 1744115138233
created: 1744108990937
---

Did you know that Yelp (and most other tech companies) use second price auction for the ad bidding system? I certainly didn't :sweat_smile:. In this framework the winning advertiser pays the amount of the second-highest bid rather than their own bid. This incentivizes advertisers to bid their true value without fear of overpaying. The point is to charge the advertiser only as much as he would need to pay to win the auction - maximizing her return on investment. It is also mathematically proven that this strategy is 'optimal' reaching Nash Equilibrium.
In the standard first price auction where highest bidder pays the price that was submitted, bidders are incentivized to bid less than their true valuation of the ad slot - only then their payoff is positive if they win the slot or 0 if not. More interestingly that for the auctioneer (i.e Yelp) the expected revenue is the same when running either type of auctions

- https://en.wikipedia.org/wiki/Vickrey_auction#Revenue_equivalence_of_the_Vickrey_auction_and_sealed_first_price_auction
- [Generalized Second Price Bid-Sealed](https://en.wikipedia.org/wiki/Generalized_second-price_auction)