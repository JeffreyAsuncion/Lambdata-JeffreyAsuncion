# Lambdata-JeffreyAsuncion
A collection of data science utility functions.

## Installation

```py
pip install -i https://test.pypi.org/simple/ lambdata-jeffreyasuncion==0.0.14
```

## Usage

```py
from my_lambdata.ds_utilities import enlarge

x = 11
print(enlarge(x)
```

# Train/validate/test split function for a dataframe
```py
from my_lambdata.ds_utilities import train_val_test

df = DataFrame
train, val, test = train_val_test(df)


"""py
def train_val_test(X,y):
    '''
    X, y are the feature matrix and target vector
    Splits the data in the following 
    train set 80%
    val set 10%
    test set 10%
    function returns
    X_train, y_train, X_val, y_val, X_test, y_test
    '''
"""

# State abbreviation -> Full Name and visa versa. FL -> Florida, etc. (Handle Washington DC and territories like Puerto Rico etc.)

"""py
def states_abbr_to_full(XX):
    '''
    function takes an abbreviation
    return full name of US State
    '''
"""

"""py
def states_full_to_abbr(fullName):
    '''
    function takes full name of US State
    return an abbreviation
    '''
"""