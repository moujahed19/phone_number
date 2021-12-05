import phonenumbers
from test import numbers
if len(numbers) < 14 :
    print("the number is  available")
    from phonenumbers import geocoder
    place= phonenumbers.parse(numbers)
    print((geocoder.description_for_number(place,"fr")))

    from phonenumbers import carrier
    company_name=phonenumbers.parse(numbers)
    print(carrier.name_for_number(company_name,"fr"))
    print("thank you !")
else:
 print("the number is not available")

