from bank import bank_details

def test_bank_details():
    expected_output = (
        "Account Name : bhimangouda \n"
        "Account Number : 8324676 \n"
        "Account Type : Savings  "
        
    )
    assert bank_details("bhimangouda","8324676","Savings") == expected_output
