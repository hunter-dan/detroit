# step 2. crawl through list to extract data
# use the list of URLs collected in step 1 - try URL1, if doesn't exist, try URL2
# loop through the URLs created as part of the past_props_url script
# use beautiful soup to extract key data - include property features
# download affiliated URLs and save with a logical name

# step 3. extract data from affiliated URLs and merge with full dataset


import os
import requests
import csv
from BeautifulSoup import BeautifulSoup

cwd = os.getcwd()
csvFile = os.path.join(cwd, "detroit_pastlistings.csv")

f = open(csvFile)
csv_f = csv.reader(f)

property = []
pdf = []

parcel_id = []
city = []
district = []
state = []
zip = []
neighborhood = []
latitude = []
longitude = []

prop_area = []
bedrooms = []
bathrooms = []
stories = []
garage = []
year_built = []
feature = []
rehabbed = []
water_cut = []
clear_title = []

listing_type = []
price = []
min_offer = []
down_payment = []
sale_date = []

row_count = -1
for row in csv_f:
    row_count = row_count+1
    if row_count != 0:
        print(row_count)
        url1 = row[3]
        url2 = row[4]
        address = row[0]
        pid = row[2]
        prop_condo_report = "https://s3.us-east-2.amazonaws.com/dlba-production-bucket/property_documents/" + str(pid) + "/"  + address + " - Property Condition Report (1).pdf"

        response = requests.get("http://"+url1)
        soup = BeautifulSoup(response.content)
        title = soup.find('title')
        print(title)

        if "find" in title:
            print("URL1 is invalid for " + address)
            response = requests.get("http://"+url2)
            soup = BeautifulSoup(response.content)
            #do the stuff
        else:
            text = soup.findAll(type="text/javascript")[20].string  # grabs the javascript string with all the property data


            text = text.split('[')[1]
            print(text)
            list = str(text.split(':'))
            list = text.split(",")
            print(list)


""" 


        # basic info
        
        < li > < strong > District: < / strong > 2 < / li >
        < li > < strong > Area: < / strong > 1449 < sup > Sq.Ft < / sup > < / li >
        < li > < strong > Year
        Built: < / strong > 1928 < / li >
        < li
        ng - if = "propertydata.is_watercut==0" > < strong > Water
        Line
        Cut: < / strong > No < / li >
        < li
        ng - if = "propertydata.is_watercut==1"


        class ="markred" > < a class ="waterCutToggle markred" href="Javascript:void(0);" > < strong > Water Line Cut:<

            / strong > No < / a > < / li >
        < li > < i


        class ="icons icon-bedroom" > < / i > 3 Beds < / li >

        < li > < i


        class ="icons icon-bathroom" > < / i > 1.5 Baths < / li >
        
        <h2>Neighborhood: <span style="font-size: 24px;">Fitzgerald/Marygrove</h2>
<li>Front porch</li>
<li>Wood floors</li>
<li>Fireplace</li>
 
"""