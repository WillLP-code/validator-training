import pandas as pd

def validate(Header, ChildIdentifiers):
    # PersonBirthDate (N00066) must be on or before ReferenceDate (N00603) or null
    header = Header
    ci_df = ChildIdentifiers

    ref_date = header["ReferenceDate"].iloc[0]

    # removes na rows as they pass
    not_na = ci_df["PersonBirthDate"].notna()
    ci_df = ci_df[not_na]

    # slices birtdays after ref date
    after_ref = ci_df['PersonBirthDate'] > ref_date
    ci_df = ci_df[after_ref]

    failing_rows = list(ci_df.index)

    return failing_rows


    

def test_validate():
    fake_header = pd.DataFrame({"ReferenceDate":["31/03/2024"]})
    fake_header["ReferenceDate"] = pd.to_datetime(fake_header["ReferenceDate"], format="%d/%m/%Y")

    fake_identifiers = pd.DataFrame({"PersonBirthDate":["01/06/2021", # pass
                                                        "01/06/2024", # fail
                                                        "31/03/2024", # pass
                                                        "01/04/2024", # fail
                                                        pd.NA #pass
                                                        ]})
    
    fake_identifiers["PersonBirthDate"] = pd.to_datetime(fake_identifiers["PersonBirthDate"], format="%d/%m/%Y")

    result = validate(Header=fake_header, ChildIdentifiers=fake_identifiers)

    assert len(result) == 2
    assert result == [1, 3]




