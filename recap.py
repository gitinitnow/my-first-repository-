# this is an iteration 

i = 0 

while i <= 4:  #i =< 4 is the condition 
    print("Hello everybody")
    i = i + 4 

#%% lists

beatles=["John", "Paul", "George", "Ringo"]

print(beatles)

print(["beatles"]) #indices start at 0, not 1 

#can contain anything we want, numbers, strings, etc 

numbers = [0, 3, -11, 99]

mixed_values = [1,  True, 0.4, "asdf"]

print(len(beatles)) #identifies the length of a list 
#%% Exercise 2: Create a function that receives a list as a paramter and prints each element of the list individually 

def print_list(list): #defines a function 
    index = 0 #starting point 

    while index <= len(list) -1: #condition
        print(list[index]) #will print whatever value is on the specific index
        index = index + 1 #will add to the index, so what it prints will change per +1 

elements = ["Karmele", "Santiago", "Isi"]
print_list(elements)

#%% Operations 

ramones = [
    "Johnnie",
    "Joey",
    "Markee",
    "Dee-dee"
]

philippes = ["Philippie", "Pepe"]
print(ramones + philippes) #combines the two lists, ramones & philippes 
print(philippes * 4)

print(ramones)

#%%
beatles = [ 
    "John",
    "Paul",
    "Ringo",
    "George"
]

beatles [3] = "Marco" #changes the value of the index to what we specificy, originally index 3 was George (since they start at 0), but now it is Marco 

print(beatles)

#%%

coding_club = [] 

coding_club.append("Karmele")

coding_club.append("Philippe") 

print(coding_club)

coding_club.pop(0) #removes the value at the specified index

print(coding_club) 

#%%
elements = [ 
    "John",
    "Paul",
    "Ringo",
    "George"
]

def print_list_with_for(list):
    for element in list: 
        print(element) 

elements = ["John, Paul, Ringo, George"]
print_list_with_for(elements)

#%%
elements = [ 
    "Marco",
    "Martin",
    "Mel"
]

def print_list_with_for(list):
    for element in list: 
        print(element) 

elements = ["Marco, Martin, Mel"]
print_list_with_for(elements)

#%%

siblings = ["Mel, Martin, Marco"]
print(siblings)

#%% 