import pandas as pd

def validate(ChildIdentifiers):
    # read in ChildIdentifiers as a dataframe
    df = ChildIdentifiers

    # set up a condition that looks for duplicated values in the LAchildID column
    duplicated = df.duplicated(subset='LAchildID', keep=False)

    # Slice out duplicated rows
    df = df[duplicated]

    # Return a list of the indexes of failing rows
    failing_rows = list(df.index)

    return failing_rows

def test_validate():
    child_identifiers = pd.DataFrame([[1234], [1234], [346546]], columns=['LAchildID'])

    result = validate(child_identifiers)

    assert len(result) == 2
    assert result == [0, 1]