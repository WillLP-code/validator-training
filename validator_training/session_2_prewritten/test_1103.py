import pandas as pd

def validate(Assessments, CINdetails):
    pass


def test_validate():
    sample_ass = pd.DataFrame(
        [
            {
                "LAchildID": "child1",
                "AssessmentActualStartDate": "30/06/2021",  # Fails as referral date is after assessment start
                "CINdetailsID": "CIN1",
            },
            {
                "LAchildID": "child2",
                "AssessmentActualStartDate": "10/09/2021",  #  Passes as assessment starts after referal start date
                "CINdetailsID": "CIN2",
            },
            {
                "LAchildID": "child3",
                "AssessmentActualStartDate": pd.NA,  # Ignored as no Assessment Date recorded
                "CINdetailsID": "CIN3",
            },
            {
                "LAchildID": "child4",
                "AssessmentActualStartDate": "01/12/2021",  # Fails as assessment starts after referral start date
                "CINdetailsID": "CIN4",
            },
            {
                "LAchildID": "child5",
                "AssessmentActualStartDate": "10/02/2022",  # Fails as no Referral Start Date recorded
                "CINdetailsID": "CIN5",
            },
        ]
    )
    sample_refs = pd.DataFrame(
        [
            {
                "LAchildID": "child1",  # Fails
                "CINreferralDate": "01/07/2021",
                "CINdetailsID": "CIN1",
            },
            {
                "LAchildID": "child2",  # Passes
                "CINreferralDate": "01/09/2021",
                "CINdetailsID": "CIN2",
            },
            {
                "LAchildID": "child3",  # Ignored
                "CINreferralDate": "26/05/2000",
                "CINdetailsID": "CIN3",
            },
            {
                "LAchildID": "child4",  # Fails
                "CINreferralDate": "10/12/2021",
                "CINdetailsID": "CIN4",
            },
            {
                "LAchildID": "child5",  # Ignored
                "CINreferralDate": pd.NA,
                "CINdetailsID": "CIN5",
            },
        ]
    )

    sample_ass['AssessmentActualStartDate'] = pd.to_datetime(
        sample_ass['AssessmentActualStartDate'], format="%d/%m/%Y", errors="coerce"
    )
    sample_refs["CINreferralDate"] = pd.to_datetime(
        sample_refs["CINreferralDate"], format="%d/%m/%Y", errors="coerce"
    )

    result = validate(Assessments=sample_ass, CINdetails= sample_refs)

    # assert len(result) == 2

