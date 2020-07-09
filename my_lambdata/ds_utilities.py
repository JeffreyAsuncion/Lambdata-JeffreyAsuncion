def enlarge(n):
    '''This function will multiple the input b 100'''
    return n * 100

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
    import numpy as np
    from sklearn.model_selection import train_test_split
  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.50, random_state=42)

    return X_train, y_train, X_val, y_val, X_test, y_test

def states_abbr_to_full(XX):
    '''
    function takes an abbreviation
    return full name of US State
    '''
    abbr_to_full = {
          'AK': 'Alaska',
          'AL': 'Alabama',
          'AR': 'Arkansas',
          'AS': 'American Samoa',
          'AZ': 'Arizona',
          'CA': 'California',
          'CO': 'Colorado',
          'CT': 'Connecticut',
          'DC': 'District of Columbia',
          'DE': 'Delaware',
          'FL': 'Florida',
          'GA': 'Georgia',
          'GU': 'Guam',
          'HI': 'Hawaii',
          'IA': 'Iowa',
          'ID': 'Idaho',
          'IL': 'Illinois',
          'IN': 'Indiana',
          'KS': 'Kansas',
          'KY': 'Kentucky',
          'LA': 'Louisiana',
          'MA': 'Massachusetts',
          'MD': 'Maryland',
          'ME': 'Maine',
          'MI': 'Michigan',
          'MN': 'Minnesota',
          'MO': 'Missouri',
          'MP': 'Northern Mariana Islands',
          'MS': 'Mississippi',
          'MT': 'Montana',
          'NA': 'National',
          'NC': 'North Carolina',
          'ND': 'North Dakota',
          'NE': 'Nebraska',
          'NH': 'New Hampshire',
          'NJ': 'New Jersey',
          'NM': 'New Mexico',
          'NV': 'Nevada',
          'NY': 'New York',
          'OH': 'Ohio',
          'OK': 'Oklahoma',
          'OR': 'Oregon',
          'PA': 'Pennsylvania',
          'PR': 'Puerto Rico',
          'RI': 'Rhode Island',
          'SC': 'South Carolina',
          'SD': 'South Dakota',
          'TN': 'Tennessee',
          'TX': 'Texas',
          'UT': 'Utah',
          'VA': 'Virginia',
          'VI': 'Virgin Islands',
          'VT': 'Vermont',
          'WA': 'Washington',
          'WI': 'Wisconsin',
          'WV': 'West Virginia',
          'WY': 'Wyoming'
    }
    return abbr_to_full.get(XX.upper())

def states_full_to_abbr(fullName):
    '''
    function takes full name of US State
    return an abbreviation
    '''
    full_to_abbr  =  {
      'Alabama': 'AL',
      'Alaska': 'AK',
      'American Samoa': 'AS',
      'Arizona': 'AZ',
      'Arkansas': 'AR',
      'California': 'CA',
      'Colorado': 'CO',
      'Connecticut': 'CT',
      'Delaware': 'DE',
      'District of Columbia': 'DC',
      'Florida': 'FL',
      'Georgia': 'GA',
      'Guam': 'GU',
      'Hawaii': 'HI',
      'Idaho': 'ID',
      'Illinois': 'IL',
      'Indiana': 'IN',
      'Iowa': 'IA',
      'Kansas': 'KS',
      'Kentucky': 'KY',
      'Louisiana': 'LA',
      'Maine': 'ME',
      'Maryland': 'MD',
      'Massachusetts': 'MA',
      'Michigan': 'MI',
      'Minnesota': 'MN',
      'Mississippi': 'MS',
      'Missouri': 'MO',
      'Montana': 'MT',
      'National': 'NA',
      'Nebraska': 'NE',
      'Nevada': 'NV',
      'New Hampshire': 'NH',
      'New Jersey': 'NJ',
      'New Mexico': 'NM',
      'New York': 'NY',
      'North Carolina': 'NC',
      'North Dakota': 'ND',
      'Northern Mariana Islands': 'MP',
      'Ohio': 'OH',
      'Oklahoma': 'OK',
      'Oregon': 'OR',
      'Pennsylvania': 'PA',
      'Puerto Rico': 'PR',
      'Rhode Island': 'RI',
      'South Carolina': 'SC',
      'South Dakota': 'SD',
      'Tennessee': 'TN',
      'Texas': 'TX',
      'Utah': 'UT',
      'Vermont': 'VT',
      'Virgin Islands': 'VI',
      'Virginia': 'VA',
      'Washington': 'WA',
      'West Virginia': 'WV',
      'Wisconsin': 'WI',
      'Wyoming': 'WY'
    }
    return full_to_abbr.get(fullName.upper().title())

if __name__ == '__main__' :
    y = int(input("Choose a number: "))
    print(y, enlarge(y))
    z = input("Enter state abbr: ")
    states_abbr_to_full(z)
    a = input("Enter full state name ")
    states_full_to_abbr(a)




