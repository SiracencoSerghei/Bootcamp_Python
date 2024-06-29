import os

from logo import logo


def clear():
    if "TERM" in os.environ:
        os.system("clear" if os.name != "nt" else "cls")
    else:
        print("\033[H\033[J", end="")


bids = {}
bidding_finished = False


def show_bidder_winner(bidders_record):
    winner = ""
    max_bid = 0
    for bid in bidders_record:
        if bidders_record[bid] > max_bid:
            max_bid = bidders_record[bid]
            winner = bid
    print(f"The winner is {winner} with a bid of ${max_bid}")


while not bidding_finished:
    print(logo)
    name = input("What is your name? ")
    price = int(input("What is your price? "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "yes":
        clear()
    else:
        bidding_finished = True
        show_bidder_winner(bids)
