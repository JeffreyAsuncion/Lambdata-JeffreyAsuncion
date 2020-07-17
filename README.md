# Lambdata-JeffreyAsuncion
A collection of data science utility functions.

## Installation

```py
pip install -i https://test.pypi.org/simple/ lambdata-jeffreyasuncion==0.0.14
```

# Usage

## Enlarge function
```py
from my_lambdata.ds_utilities import enlarge

x = 11
print(enlarge(x)
```

## Train/validate/test split function for a dataframe
```py
from my_lambdata.ds_utilities import train_val_test

df = DataFrame
train, val, test = train_val_test(df)
```

## State abbreviation -> Full Name
```py
from my_lambdata.ds_utilities import states_abbr_to_full

abbr = "NJ"
states_abbr_to_full(abbr)
```

## State Full Name  -> Abbreviation
```py
from my_lambdata.ds_utilities import states_abbr_to_full

fullName = "New Jersey"
states_full_to_abbr(fullName)
```

## Split data into Train, Val, Test, with features Matrix and Target Vector
```py
from my_lambdata.ds_utilities import MyDataSplitter

mds = MyDataSplitter()
X_train, X_val, X_test, y_train, y_val, y_test = 
    mds.train_validation_test_split(self,
                                train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):
```

## Divide the Date into Year, Month, Day columns
```py
from my_lambdata.ds_utilities import MyDataSplitter

mds = MyDataSplitter()
date_divider(date_col):
        return converted_df
```

## Print the split summary of Train, Val, Test
```py
from my_lambdata.ds_utilities import MyDataSplitter

mds = MyDataSplitter()
print_split_summary(X_train, X_val, X_test):
```