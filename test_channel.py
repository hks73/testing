##################################
import urllib2
import urllib
import sys
import json
import requests
###################################

url_for_internet="http://api.pressplaytv.in/v1/channel?pageLen=1000&pageNum=1"
url_for_hotspot ="http://pressplaytv.in/api/v1/channel?pageLen=1000&pageNum=1"

def check_url(url):
	ret=requests.head(url)
	return ret.status_code

########################## FOR INTERNET CHANNEL API TESTING #################################

def test_internet_channel():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				try :
					for sponsor in channel["topBarSponsor"]:
						try:
							assert(channel["topBarSponsor"]["status"] == True or channel["topBarSponsor"]["status"] == true)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["status"]) ) )
						try:	
							assert(channel["topBarSponsor"]["ppId"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s"%channel["topBarSponsor"]["ppId"] ) )
						try:	
							assert(channel["topBarSponsor"]["name"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["name"]) ) )
						try:	
							assert(channel["topBarSponsor"]["downloadUrl"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in downloadUrl %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["downloadUrl"]) ) )
						try:	
							assert(channel["topBarSponsor"]["image"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["image"]) ) )
						try:	
							assert(channel["topBarSponsor"]["packageName"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in packageName %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["packageName"]) ) )
						try:	
							assert(channel["topBarSponsor"]["description"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in description %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["description"]) ) )
						try:	
							assert(channel["topBarSponsor"]["type"] == "sponsor")
						except AssertionError, e:
							raise( AssertionError( "\nproblem in type ==> %s in status %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["type"]) ) )
							
						assert(channel["topBarSponsor"]["ppId"] in channel["topBarSponsor"]["downloadUrl"])
						assert(channel["topBarSponsor"]["ppId"] in channel["topBarSponsor"]["logo"])	
						
				except KeyError:
					pass
					try:
						assert(channel["type"]=="channel")
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(channel["ppId"]%channel["type"]) ) )
					try:
						assert(channel["status"] == True or channel["status"] == true)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["ppId"]%channel["status"]) ) )
					try:
						assert(channel["ppId"] in channel["posterSmall"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in posterSmall %s "%(channel["ppId"]%channel["posterSmall"]) ) )
					try:
						assert(channel["ppId"] in channel["poster"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in poster %s "%(channel["ppId"]%channel["poster"]) ) )
					
					try:
						assert(channel["ppId"] in channel["posterSmall"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in posterSmall %s "%(channel["ppId"]%channel["posterSmall"]) ) )
					
					try:
						assert(type(channel["newCount"]) == int)	
					except KeyError:
						pass
					try:
						assert(channel["poster"] != None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in poster %s "%(channel["ppId"]%channel["poster"]) ) )
					try:	
						assert(channel["name"]!=None)
					except AssertionError, e:			
						raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(channel["ppId"]%channel["name"]) ) )
					try:
						assert(channel["ppId"]!=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s "%channel["ppId"] ) )
				

def test_all_channel_ids():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				url_for_ids="http://api.pressplaytv.in/v1/channel/"+channel["ppId"]+"?pageLen=1000&pageNum=1"
				response_ids= urllib2.urlopen(url_for_ids)
				data_id = json.loads(response_ids.read())
				for value in data_id["data"]["itemContents"]:
					for keys_data in value:
						try:
							try:	
								assert(keys_data["ppId"]!=None)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s"%keys_data["ppId"])) 
							try:	
								assert(keys_data["poster"]!=None)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in poster %s "%(keys_data["ppId"]%keys_data["poster"]) ) )
							try:	
								assert(keys_data["posterSmall"]!=None)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in posterSmall %s "%(keys_data["ppId"]%keys_data["posterSmall"]) ) )
							try:
								assert(keys_data["status"]=="true" or keys_data["status"]==True )
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(keys_data["ppId"]%keys_data["status"]) ) )
						except KeyError:
								pass

########################## FOR INTERNET CHANNEL API TESTING#################################
def test_hotspot_channel():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				try :
					for sponsor in channel["topBarSponsor"]:
						try:
							assert(channel["topBarSponsor"]["status"] == True or channel["topBarSponsor"]["status"] == true)
						except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["status"]) ) )
						try:	
							assert(channel["topBarSponsor"]["ppId"]!=None)
						except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s"%channel["topBarSponsor"]["ppId"] ) )
						try:	
							assert(channel["topBarSponsor"]["name"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["name"]) ) )
						try:	
							assert(channel["topBarSponsor"]["downloadUrl"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in downloadUrl %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["downloadUrl"]) ) )
						try:	
							assert(channel["topBarSponsor"]["image"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["image"]) ) )
						try:	
							assert(channel["topBarSponsor"]["packageName"] != None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in packageName %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["packageName"]) ) )
						try:	
							assert(channel["topBarSponsor"]["description"]!=None)
						except AssertionError, e:
							raise( AssertionError( "\nproblem in ppId ==> %s in description %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["description"]) ) )
						try:	
							assert(channel["topBarSponsor"]["type"] == "sponsor")
						except AssertionError, e:
							raise( AssertionError( "\nproblem in type ==> %s in status %s "%(channel["topBarSponsor"]["ppId"]%channel["topBarSponsor"]["type"]) ) )
							
						assert(channel["topBarSponsor"]["ppId"] in channel["topBarSponsor"]["downloadUrl"])
						assert(channel["topBarSponsor"]["ppId"] in channel["topBarSponsor"]["logo"])	
						
				except KeyError:
					pass
					try:
						assert(channel["type"]=="channel")
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(channel["ppId"]%channel["type"]) ) )
					try:
						assert(channel["status"] == True or channel["status"] == true)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["ppId"]%channel["status"]) ) )
					try:
						assert(channel["ppId"] in channel["posterSmall"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in posterSmall %s "%(channel["ppId"]%channel["posterSmall"]) ) )
					try:
						assert(channel["ppId"] in channel["poster"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in poster %s "%(channel["ppId"]%channel["poster"]) ) )
					
					try:
						assert(channel["ppId"] in channel["posterSmall"])
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in posterSmall %s "%(channel["ppId"]%channel["posterSmall"]) ) )
					
					try:
						assert(type(channel["newCount"]) == int)	
					except KeyError:
						pass
					try:
						assert(channel["poster"] != None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in poster %s "%(channel["ppId"]%channel["poster"]) ) )
					try:	
						assert(channel["name"]!=None)
					except AssertionError, e:			
						raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(channel["ppId"]%channel["name"]) ) )
					try:
						assert(channel["ppId"]!=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s "%channel["ppId"] ) )
def test_all_channelHotspot():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				url_for_ids="http://pressplaytv.in/api/v1/channel/"+channel["ppId"]+"?pageLen=1000&pageNum=1"
				response_ids= urllib2.urlopen(url_for_ids)
				data_id = json.loads(response_ids.read())
				try:
					for value in data_id["data"]["itemData"]["preRollPool"]:
						try:
							try:
								assert(value["status"]==True)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(value["ppId"]%value["status"]) ) )
							try:	
								assert(value["sponsor_id"]!=None)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in sponsor_id %s "%(value["ppId"]%value["sponsor_id"]) ) )
							try:	
								assert(value["sponsor_id"] in value["playbackUrl"])
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(value["ppId"]%value["playbackUrl"]) ) )
							try:	
								assert(value["ppId"]!=None)
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s %s "%value["ppId"] ) )
							try:	
								assert(value["type"]=="pre_roll")
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(value["ppId"]%value["type"]) ) )
							try:	
								assert(value["playbackUrl"]!=True )
							except AssertionError, e:
								raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(value["ppId"]%value["playbackUrl"]) ) )
						except KeyError:
							pass
				except KeyError:
						pass
					
				try:
					key_value=data_id["data"]["itemData"]["topBarSponsor"]
					try:
						assert(key_value["status"]==True)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(key_value["ppId"]%key_value["status"]) ) )
					try:	
						assert(key_value["name"]!=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(key_value["ppId"]%key_value["name"]) ) )
					try:	
						assert(key_value["url"] !=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in url %s "%(key_value["ppId"]%key_value["url"]) ) )
					try:	
						assert(key_value["image"]!=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(key_value["ppId"]%key_value["image"]) ) )
					try:
						assert(key_value["downloadUrl"]!=None)
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in downloadUrl %s "%(key_value["ppId"]%key_value["downloadUrl"]) ) )
					try:	
						assert(key_value["logo"]!=None )
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s in logo %s "%(key_value["ppId"]%key_value["logo"]) ) )
					try:	
						assert(key_value["ppId"]!=None )
					except AssertionError, e:
						raise( AssertionError( "\nproblem in ppId ==> %s "%key_value["ppId"] ) )

					assert(key_value["ppId"] in key_value["image"])
					assert(key_value["ppId"] in key_value["downloadUrl"])
					assert(key_value["ppId"] in key_value["logo"])
				except KeyError:
					pass
					