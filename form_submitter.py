import json
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pprint import pprint
from urllib.parse import urljoin
import webbrowser
import sys

from form_extractor import get_all_forms, get_form_details, session

inputData = None

session  = HTMLSession()

with open("data.json", "r") as read_file:
    print("Starting to convert json decoding")
    inputData = json.load(read_file)
          
def makeSubmission():
     url = "https://www.memberplanet.com/s/vazeta/spring/piphilovestriangle"
     all_forms = get_all_forms(url)

     #print(all_forms)
     form_details = get_form_details(all_forms[0])
     
     #This part might not be necessary
     """
     for detail in details:
          match detail["name"]:
               case "firstName":
                    detail["value"] = inputData["firstName"]
                    break
               case "lastName":
                    detail["value"] = inputData["lastName"]
                    break
               case "email_address":
                    detail["value"] = inputData["email_address"]
                    break
               case "phone_areacode":
                    detail["value"] = inputData["phone_areacode"]
                    break
               case "phone_prefix":
                    detail["value"] = inputData["phone_prefix"]
                    break
               case "phone_suffix":
                    detail["value"] = inputData["phone_suffix"]
                    break
               case "Country_date_6":
                    detail["value"] = inputData["Country_date_6"]
                    break
               case "streetAddress_date_6":
                    detail["value"] = inputData["streetAddress_date_6"]
                    break
               case "streetAddress2_date_6":
                    detail["value"] = inputData["streetAddress2_date_6"]
                    break
               case "city_date_6":
                    detail["value"] = inputData["city_date_6"]
                    break
               case "zipcode_date_6":
                    detail["value"] = inputData["zipcode_date_6"]
                    break
               case "fsea-control-7_fsea-control-7":
                    detail["value"] = inputData["fsea-control-7_fsea-control-7"]
                    break
               case "paymentControl$paymentInfoControl$txtCardNumber":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$txtCardNumber"]
                    break
               case "paymentControl$paymentInfoControl$txtSecurityCode":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$txtSecurityCode"]
                    break
               case "paymentControl$paymentInfoControl$txtZip":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$txtZip"]
                    break
               case "paymentControl$paymentInfoControl$txtNameOnCard":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$txtNameOnCard"]
                    break
               case "paymentControl$paymentInfoControl$txtConfirmationMail":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$txtConfirmationMail"]
                    break
               case "state_date_6":
                    detail["value"] = inputData["state_date_6"]
                    break
               case "paymentControl$paymentInfoControl$ddlMonth":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$ddlMonth"]
                    break
               case "paymentControl$paymentInfoControl$ddlYear":
                    detail["value"] = inputData["paymentControl$paymentInfoControl$ddlYear"]
                    break
     """
     # join the url with the action (form request URL)
     url = urljoin(url, form_details["action"])
     #pprint(inputData)
     
     ### This is probably where the bug is. Basically, the session needs to post the correct data format, but idk what that is.
     
     if form_details["method"] == "post":
          res = session.post(url, data=inputData)
     elif form_details["method"] == "get":
          res = session.get(url, params=inputData)
     
     # the below code is only for replacing relative URLs to absolute ones
     soup = BeautifulSoup(res.content, "html.parser")
     for link in soup.find_all("link"):
          try:
               link.attrs["href"] = urljoin(url, link.attrs["href"])
          except:
               pass
     for script in soup.find_all("script"):
          try:
               script.attrs["src"] = urljoin(url, script.attrs["src"])
          except:
               pass
     for img in soup.find_all("img"):
          try:
               img.attrs["src"] = urljoin(url, img.attrs["src"])
          except:
               pass
     for a in soup.find_all("a"):
          try:
               a.attrs["href"] = urljoin(url, a.attrs["href"])
          except:
               pass

     # write the page content to a file
     open("page.html", "w").write(str(soup))
     
     import webbrowser
# open the page on the default browser
     webbrowser.open("page.html")  

#for i, f in enumerate(all_forms, start=1):
#    form_details = get_form_details(f)
    #print(f"{i} #")
    #pprint(form_details)
    #print("="*50)

makeSubmission()