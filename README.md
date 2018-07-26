# detroit
buildingdetroit.org

current plan is to first get the data for all past sales/auctions
https://buildingdetroit.org/properties/pastlistings/

the main listing site is rendered using Javascript so BS will not be helpful
but we just need a list of the past properties from this page
once we have those, the listing pages are primarily HTML so BS will work

- Interactive property map: https://cityofdetroit.github.io/demo-tracker/
- Previous own it now sales: https://data.detroitmi.gov/Property-Parcels/Own-It-Now-Sales/pyf3-v3vc
- Previous side lot sales: https://data.detroitmi.gov/Property-Parcels/Side-Lot-Sales/mfsk-uw55
- Previous auction sales: https://data.detroitmi.gov/Property-Parcels/DLBA-Auctions-Closed/tgwk-njih
- All current props for sale: https://data.detroitmi.gov/Property-Parcels/DLBA-Properties-for-Sale/gfhb-f4i5
- All DLBA properties: https://data.detroitmi.gov/Property-Parcels/Land-Bank-Inventory/vsin-ur7i
- building permits: https://data.detroitmi.gov/Property-Parcels/Building-Permits/xw2a-a7tf


IDEA: use the above datasets accessible via open data portal
this will give us our "frame". we can use the addresses from those
to crawl the actual website since most property listings (current and past)
look like:
https://buildingdetroit.org/properties/560-hague/
where the end part is the address. Some older properties have and additional
ID after the address but we can deal with these separately. should be a relatively straightforward loop through
property names

