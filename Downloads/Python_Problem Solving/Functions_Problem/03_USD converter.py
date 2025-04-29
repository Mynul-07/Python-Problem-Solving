def converter(usd_val):
    bd_taka = usd_val * 120
    print(f"{usd_val} USD = {bd_taka} BDT")


converter(int(input("Enter the amount in USD: ")))
