import pickle
import auction

def menu():
    print("Select a task by typing one of the following letters:")
    print("'i' shows the highest bid of an item,")
    print("'s' to save all winning bids to a file,")
    print("'q' to exit.")
    userChoice = input("Choice: ")
    
    if userChoice == "i":
        return "i"
    elif userChoice == "s":
        return "s"
    elif userChoice == "q":
        return "q"
    
    return None
    
        
def item_offers(item, data):
    offers = []
    for x in range(1, len(data)):
        t = [data[x][0], auction.bid(data[x][0],item,data)]
        offers.append(t)
    
    return offers

def item_winner(item, data):
    offers = item_offers(item, data)
    bidders = auction.sort_list(offers,1)
    highestBidder = bidders[0]
    
    if highestBidder[1] == 0:
        highestBidder = []
    
    return highestBidder


def all_winners_dict(data):
    winnersDict = {}
    for x in range(1, len(data[0])):
        winnersDict[data[0][x]] = item_winner(data[0][x],data)
      
    return winnersDict   

def save_auction_data(data):
    try:
        filename = "auction_winners.db"
        f = open(filename,"b")
        winners = all_winners_dict(data)
        pickle.dump(winners,filename)
        f.close()
        print("Dictionary data successfully written to file.")

    except:
        print("Could not write dictionary data to file")
    
    
def task():
    data = auction.get_auction_data("auctiondata.txt")
    while True:
        menuReturn = menu()
        print(menuReturn)
        if menuReturn == "i":
            auctionItemName = input("Hvilken gjenstand skal du sjekke? ")
            itemWinner = item_winner(auctionItemName, data)
            print("Vinnern av", auctionItemName, "er", itemWinner[0], "som bød", itemWinner[1], "KR")
        elif menuReturn == "s":
            save_auction_data(data)
        elif menuReturn == "q":
            print("Goodbye!")
            break
        else:
            print("Please write a valid input")

task()