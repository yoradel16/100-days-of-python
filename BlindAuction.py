# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from Assets import blind_auction
def highest_bidder(bids):
    bidder = max(bids, key=bids.get)
    print("\n" * 20)
    print(f"The highest bidder is {bidder} with a bid of ${bids.get(bidder)}")

bids = {}
continue_bidding = True
print(blind_auction.logo)
while continue_bidding:
    name = input("What is your name?: ").capitalize()
    bid = int(input("What is your bid?: $"))
    add_bidder = input("Are there other bidders? Type 'yes' or 'no'. ").lower()
    bids[name] = bid
    if add_bidder == 'no':
        continue_bidding = False
        highest_bidder(bids)
    else:
        print("\n" * 20)
