import pandas as pd

def validate():
    pass

def test_validate():
    child_identifiers = pd.DataFrame([[1234], [1234], [346546]], columns=['LAchildID'])

    result = validate(child_identifiers)

    # assert len(result) == 2