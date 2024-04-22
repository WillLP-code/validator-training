import pandas as pd
# list is in square brackets seperated by commas [x1, x2, x3, x4]
# dicitonary is curly brackets with key : value pairs, sep. by commas
# dict_1 = {'key_1':1,
#           'key_2':'two',
#           'key_3':[1, 2, 3]}

def rule_4220(df):
    eth_list = [
        "ABAN",
        "AIND",
        "AOTH",
        "APKN",
        "BAFR",
        "BCRB",
        "BOTH",
        "CHNE",
        "MOTH",
        "MWAS",
        "MWBA",
        "MWBC",
        "NOBT",
        "OOTH",
        "REFU",
        "WBRI",
        "WIRI",
        "WIRT",
        "WOTH",
        "WROM",
    ]

    failing_indices = df[~(df['Ethnicity'].isin(eth_list))].index

    failing_indices = list(failing_indices)

    return failing_indices


def test_rule_4220():
    ChildCharacteristics = pd.DataFrame({
        'Ethnicity':['WIRI', # 0
                    'WBRI', # 1
                    'BOTH', # 2
                    'MWBC', #3
                    'not real ethnicity' # 4, fail
                    ]
    })

    result = rule_4220(ChildCharacteristics)

    expected_results = [4]

    assert len(result) == 1
    assert result == expected_results


