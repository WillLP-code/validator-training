import pandas as pd

def validator(child_identifiers):
    pass

def test_validate():
    child_identifiers = pd.DataFrame(
        {"UPN": [pd.NA, "X000000000000", "X0000y0000000", "x0000000er00e0"]}
    )

    result = validator(child_identifiers)

    # assert len(result) == 2
