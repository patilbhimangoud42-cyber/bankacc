def bank_details(Acc_name, Acc_num, Acc_type):
    result = (
        f"Account Name : {Acc_name} \n"
        f"Account Number : {Acc_num}\n"
        f"Account Type : {Acc_type}"
    )
    return result

if __name__ == "__main__":
    Acc_name= "bhimangouda"
    Acc_num="8324676"
    Acc_type ="Savings"
    print(bank_details(Acc_name, Acc_num, Acc_type))
