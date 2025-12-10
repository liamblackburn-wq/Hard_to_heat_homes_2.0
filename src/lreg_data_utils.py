import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv("data/TEST_DATA.csv")
print(df)

def get_details_from_land_reg(properties):
    print(type(properties))
    for property in properties:
        print(type(property))
        # property["test_key"] = "test_value"
    return properties

# get this function working with set property data 
# return 
# line 41 - properties = Proprietorship Category (1) and Company Registration No. (1) and (maybe) Proprietor Name (1),

