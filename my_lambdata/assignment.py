# my_lambdata/assignment.py

from pandas import DataFrame

# TODO helper function in class DS15 follow along
# State abbreviation -> Full Namd and vice versa.
# FL -> Florida, etc.

def add_state_names_column(my_df):
    '''
    Add a column of corresponding state names to a dataframe

    Params (my_df) a Dataframe with a column called "abbrev" that has state abbreviations.

    Return a copy of the original datafrom,but with an extra column.
    '''
    new_df = df.copy()

    names_map = {"CA": "California",
                 "CO": "Colorado",
                 "CT": "Conn",
                 "DC": "District of Colombia",
                 "TX": "Texas"
                 }

    new_df["name"] = new_df["abbrev"].map(names_map)
    
    #DS15 50:08 timestamp 
     

    return new_df


if __name__ == "__main__" :
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    
    add_state_names_column(df)
    print(df.head())

