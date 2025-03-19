
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

def get_friends_favorite_candy_count(friend_favorites):
    candy_count = {}
    for lists in friend_favorites:
        for items in lists[1]:
            if items in candy_count:
                candy_count[items] += 1
            else:
                candy_count[items] = 1
    return candy_count
#print(get_friends_favorite_candy_count(friend_favorites))


def create_new_candy_data_structure(friend_favorites):
    candy_dict = {}  
    
    for friend, candies in friend_favorites:
        for candy in candies:
            if candy not in candy_dict:
                candy_dict[candy] = []  
            candy_dict[candy].append(friend)  
    
    return candy_dict
# print(create_new_candy_data_structure(friend_favorites))

def get_friends_who_like_specified_candy(friend_favorites, candy_name):
    list = []
    
    for friend, candies in friend_favorites:
        
        if candy_name in candies:
            list.append(friend)
    return tuple(list)
# print(get_friends_who_like_specified_candy(friend_favorites, "lollipop"))


candy_dict = {
    'lollipop': ['Sally', 'Bob'], 
    'bubble gum': ['Sally'], 
    'laffy taffy': ['Sally', 'Arlene', 'Carlie'], 
    'milky way': ['Bob', 'Arlene'], 
    'licorice': ['Bob'], 
    'chocolate bar': ['Arlene'], 
    'nerds': ['Carlie'], 
    'sour patch kids': ['Carlie']
    }

def create_candy_set(candy_dict):
    candy_set = set()
    for keys in candy_dict.keys():
        candy_set.add(keys)
    return candy_set
# print(create_candy_set(candy_dict))
