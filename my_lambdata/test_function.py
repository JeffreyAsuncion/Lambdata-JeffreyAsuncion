from my_lambdata.ds_utilities import enlarge
from my_lambdata.ds_utilities import states_full_to_abbr
from my_lambdata.ds_utilities import states_abbr_to_full

y =  5
print(y, enlarge(y))
# z = input("Enter state abbr: ")
z = "NJ"
print(states_abbr_to_full(z))
# a = input("Enter full state name ")
a = "New York"
print(states_full_to_abbr(a))