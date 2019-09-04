import pandas as pd





def train_test_split(df, train_percent=.6, validate_percent=.2, seed=42):
    """
    Function does 3-Way hold out split of Train, Validate, Test
    """
    train, test = train_test_split(df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(
        train, test_size=0.25, random_state=seed)
    return (train, validate, test)



def hape(train, val, test=None, title='Train/Val'):
    print(f'Training Set: {train.shape}')
    print(f'Validation Set: {val.shape}')
    if test is not None:
        print(f'Testing Set: {test.shape}')
