transactions = ["A10.31", "A3.41", "B100.31", "C37.2", "B99.12", "A1.33"]

def calculate_discount(t_array):
    customers = set()
    for transaction in t_array:
        # take first char, add to set
        customers.add(transaction[0])
    
    # from set, create dict with set values as keys
    # donations = dict.fromkeys(customers, []) ***
    donations = {customer: [] for customer in customers}

    # add donation amounts to corresponding customer id in dict
    for transaction in transactions:
        donations[transaction[0]].append(float(transaction[1:]))
    
    # for each customer, calculate 10% of top two donations
    for customer in donations:
        if len(donations[customer]) == 1:
            donations[customer] = round(donations[customer][0] * .10, 2)
        else: 
            max_1 = max(donations[customer])
            donations[customer].remove(max_1)
            max_2 = max(donations[customer])
            donations[customer] = round((max_1 * .10) + (max_2 * .10), 2)
    
    print(donations)

calculate_discount(transactions)

# *** in Python, when you initialize your dictionary with `dict.fromkeys(customers, [])`, 
#     all keys are assigned the same empty list. This means that when you append a 
#     transaction to the list of any key, it appends to the same shared list across all
#     keys, rather than separate lists for each key.
# 
#     Alternatively, `donations = {customer: [] for customer in customers}` effectively 
#     initializes a new dictionary with the same keys, but where each key ('customer' in
#     the 'customers' set) is assigned its own, separate empty array.
#     (the brackets indicate it's a dictionary, "customer : []" indicates that 'customer'
#      and a new, empty array will be they key and value, and "for customer in customers" 
#      says to initialize this for each customer in the customers set.)