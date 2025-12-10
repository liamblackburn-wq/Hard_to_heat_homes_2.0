import pandas as pd

df = pd.read_csv("data/TEST_DATA.csv")

def get_details_from_land_reg(properties):
    for property in properties:
        property.set_test_properties('Fictional Company Ltd.', 'Private Company', "000002")

    return properties

# get this function working with set property data 
# return 
# line 41 - properties = Proprietorship Category (1) and Company Registration No. (1) and (maybe) Proprietor Name (1),