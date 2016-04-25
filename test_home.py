##################################
import urllib2
import urllib
import sys
import json
import requests
###################################

url_for_internet = "http://api.pressplaytv.in/v1/home?pageLen=1000&pageNum=1"
url_for_hotspot  = "http://pressplaytv.in/api/v1/home?pageLen=1000&pageNum=1"

def check_url(url):
	ret=requests.head(url)
	return ret.status_code

########################## FOR INTERNET COLLECTION API TESTING#################################
def test_internetHome():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for home in value:
				try :
					for sponsor in home["topBarSponsor"]:
						try:
							assert(home["topBarSponsor"]["status"] == True or home["topBarSponsor"]["status"] == true)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["status"]) ) )
						try:
							assert(home["topBarSponsor"]["ppId"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s "%home["topBarSponsor"]["ppId"] ) )
						try:	
							assert(home["topBarSponsor"]["name"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in name %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["name"]) ) )
						try:
							assert(home["topBarSponsor"]["downloadUrl"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in downloadUrl %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["downloadUrl"]) ) )
						try:
							assert(home["topBarSponsor"]["image"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in image %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["image"]) ) )
						try:
							assert(home["topBarSponsor"]["packageName"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in packageName %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["packageName"]) ) )
						try:
							assert(home["topBarSponsor"]["description"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in description %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["description"]) ) )
						try:
							assert(home["topBarSponsor"]["type"] == "sponsor")
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in type %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["type"]) ) )
						try:
							assert(home["topBarSponsor"]["ppId"] in home["topBarSponsor"]["downloadUrl"])
						except AssertionError, e:
							raise( AssertionError( "\nproblem in downloadUrl and ppId ") )
						try:
							assert(home["topBarSponsor"]["ppId"] in home["topBarSponsor"]["logo"])	
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId and logo") )
				except KeyError:
						pass
						try:	
							try:
								assert(home["type"]=="collection" or home["type"]=="channel" or home["type"]=="sponsor" or home["type"]=="video" or home["type"]=="image_ad")
							except AssertionError:
								raise( AssertionError( "\nproblem in type in  ==> %s"%home["ppId"] ) )
							try:	
								assert(home["status"] == True or home["status"] == true)
							except AssertionError:
								raise( AssertionError( "\nproblem in status in  ==> %s"%home["ppId"] ) )
							try:
								assert(home["posterSmall"] != None)
							except AssertionError:
								raise( AssertionError( "\nproblem in posterSmall in  ==> %s"%home["ppId"] ) )
							try:
								assert(type(home["rawId"])== int )
								assert(type(home["newCount"]) == int)	
							except KeyError:
								pass
							try:	
								assert(home["poster"] != None)
							except AssertionError:
								raise( AssertionError( "\nproblem in poster in  ==> %s"%home["ppId"] ) )
							try:	
								assert(home["name"]!=None)
							except AssertionError:
								raise( AssertionError( "\nproblem in name ==> %s"%home["ppId"] ) )
							try:
								assert(home["ppId"]!=None)
							except AssertionError:
								raise( AssertionError( "\nproblem in ppId in ==> %s"%home["ppId"] ) )		
						except KeyError:
							pass
					
########################## FOR HOTSPOT COLLECTION API TESTING#################################
def test_hotspotHome():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for home in value:
				try :
					for sponsor in home["topBarSponsor"]:
						try:
							assert(home["topBarSponsor"]["status"] == True or home["topBarSponsor"]["status"] == true)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["status"]) ) )
						try:
							assert(home["topBarSponsor"]["ppId"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s "%home["topBarSponsor"]["ppId"] ) )
						try:	
							assert(home["topBarSponsor"]["name"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in name %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["name"]) ) )
						try:
							assert(home["topBarSponsor"]["downloadUrl"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in downloadUrl %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["downloadUrl"]) ) )
						try:
							assert(home["topBarSponsor"]["image"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in image %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["image"]) ) )
						try:
							assert(home["topBarSponsor"]["packageName"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in packageName %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["packageName"]) ) )
						try:
							assert(home["topBarSponsor"]["description"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in description %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["description"]) ) )
						try:
							assert(home["topBarSponsor"]["type"] == "sponsor")
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId==> %s in type %s "%(home["topBarSponsor"]["ppId"]%home["topBarSponsor"]["type"]) ) )
						try:
							assert(home["topBarSponsor"]["ppId"] in home["topBarSponsor"]["downloadUrl"])
						except AssertionError, e:
							raise( AssertionError( "\nproblem in downloadUrl and ppId ") )
						try:
							assert(home["topBarSponsor"]["ppId"] in home["topBarSponsor"]["logo"])	
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId and logo") )
				except KeyError:
						pass
						try:
							assert(home["type"]=="collection" or home["type"]=="channel" or home["type"]=="sponsor" or home["type"]=="video")
						except AssertionError:
							raise( AssertionError( "\nproblem in type in  ==> %s"%home["ppId"] ) )
						try:	
							assert(home["status"] == True or home["status"] == true)
						except AssertionError:
							raise( AssertionError( "\nproblem in status in  ==> %s"%home["ppId"] ) )
						try:
							assert(home["posterSmall"] != None)
						except AssertionError:
							raise( AssertionError( "\nproblem in posterSmall in  ==> %s"%home["ppId"] ) )
						try:
							assert(type(home["rawId"])== int )
							assert(type(home["newCount"]) == int)	
						except KeyError:
							pass
						try:	
							assert(home["poster"] != None)
						except AssertionError:
							raise( AssertionError( "\nproblem in poster in  ==> %s"%home["ppId"] ) )
						try:	
							assert(home["name"]!=None)
						except AssertionError:
							raise( AssertionError( "\nproblem in name ==> %s"%home["ppId"] ) )
						try:
							assert(home["ppId"]!=None)
						except AssertionError:
							raise( AssertionError( "\nproblem in ppId in ==> %s"%home["ppId"] ) )		