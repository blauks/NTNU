def get_auction_data(filename):

  # Code that collects the data, not shown here.

  # Instead we hard code the return value.

    return [['Customer','vase','maleri','sykkel','bilbane','tv'],

            ['Per',100,0,200,0,1500],

            ['Ida',110,50,200,0,1500],

            ['Ottar',200,600,200,0,1700],

            ['Dag',200,600,200,0,1700],

            ['Lise',400,600,0,0,0]]
        
    
def bid(customer, item, data):

    column = data[0].index(item)

    for i in data:

        if i[0] == customer:

            return i[column]

 

def sort_list(liste,column):

    return sorted(liste,key=lambda l:l[column], reverse=True)

 