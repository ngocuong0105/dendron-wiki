First-price bid-sealed auction (FPBSA) is the standard auction that most people are familiar with. Every participant submits a bid that others are not aware of. All bids are revealed and highest bidder wins and pays the amount they've submitted.

In FPBSA, each bidder is characterized by their monetary valuation of the intem for sale.

The optimal strategy for all bidders is to bid slightly less then their valuation. This type of auction we describe as **non-truthfull** as no bidder reveals their true valuation.

Say Alice valuation for the item on the auction is $a$
- If she bids more than a, then her payoff is either 0 if she does not win the auction, or negative if she wins
- If she bids exactly a, then her payoff is always 0
- If she bids $x < a$, then her payoff is either 0 or $a-x$

$x$ depends on other peoples bids. It should be $\eps$ (say the minimum incremental value in the auction) more than the maximum of all opponents bids and less than $a$.