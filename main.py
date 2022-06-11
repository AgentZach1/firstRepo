import json


details = {
     '' : '',
     'firstName' : 'Luke',
     'lastName': 'Marks',
     'preferredName': 'Luke',
     'email_address': 'BigLukeDT@gmail.com',
     'phone_areacode': '571',
     'phone_prefix' : '364',
     'phone_suffix' : '4945',
     'Country_date_6' : 'United States of America',
     'streetAddress_date_6' : '43923 Glenhazel Dr',
     'streetAddress2_date_6' : '',
     'city_date_6' : '',
     'statename_date_6' : '',
     'zipcode_date_6' : '',
     'fsea-control-7_fsea-control-7' : '', #figure out how to work this
     'paymentControl$paymentInfoControl$txtCardNumber' : '',
     'paymentControl$paymentInfoControl$txtSecurityCode' : '',
     'paymentControl$paymentInfoControl$txtZip' : '',
     'paymentControl$paymentInfoControl$txtNameOnCard' : '',
     'paymentControl$paymentInfoControl$txtConfirmationMail' : '',
     'state_date_6' : 'VA',
     'paymentControl$paymentInfoControl$ddlMonth' : '',
     'paymentControl$paymentInfoControl$ddlYear' : '',
     'ddlMonths' : '',
     'ddlDays' : '',
     'ddlYears' : '',
     '' : ''
}

with open("sample.json", "w") as outfile:
    json.dump(details, outfile)