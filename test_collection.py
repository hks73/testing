##################################
import urllib2
import urllib
import sys
import json
import requests
###################################

url_for_internet="http://api.pressplaytv.in/v1/collection?pageLen=1000&pageNum=1"
url_for_hotspot="http://pressplaytv.in/api/v1/collection?pageLen=1000&pageNum=1"

def check_url(url):
	ret=requests.head(url)
	return ret.status_code

########################## FOR INTERNET COLLECTION API TESTING #################################
def test_collection():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				try:
					assert(channel["type"]=="collection")
				except AssertionError, e:
					raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(channel["ppId"]%channel["type"]) ) )
				try:
					assert(channel["type"] in channel["ppId"])
				except AssertionError, e:
					raise( AssertionError( "\nproblem in type and ppId in  %s "%channel["ppId"] ) )
				try:	
					assert(channel["status"] == True or channel["status"])
				except AssertionError, e:
					raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["ppId"]%channel["status"]) ) )
				try:	
					assert(channel["posterSmall"] != None)
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
					raise( AssertionError( "\nproblem in ppId ==> %s"%channel["ppId"]) )

def test_collectionidsinternet():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for collection in value:
				url_for_ids="http://api.pressplaytv.in/v1/collection/"+collection["ppId"]+"?pageLen=1000&pageNum=1"
				response_ids= urllib2.urlopen(url_for_ids)
				data_id = json.loads(response_ids.read())
				for value in data_id["data"]["itemContents"]:
						for sponsor in value:
							try:
								for data in  sponsor["preRollPool"]:
									try:
										assert(data["status"] == True )
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(data["ppId"]%data["status"]) ) )
									try:	
										assert(data["ppId"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s  "%data["ppId"] ) )
									try:	
										assert(data["sponsorId"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in sponsorId %s "%(data["ppId"]%data["sponsorId"]) ) )
									try:	
										assert(data["type"] == "pre_roll")
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(data["ppId"]%data["type"]) ) )
									try:	
										assert(data["sponsorId"] in data["playbackUrl"])
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(data["ppId"]%data["playbackUrl"]) ) )
									try:	
										assert(data["playbackUrl"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(data["ppId"]%data["playbackUrl"]) ) )
							except KeyError:
								pass
							try:
								try:
									assert(sponsor["topBarSponsor"]["status"] ==True)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["status"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s"%sponsor["topBarSponsor"]["ppId"]) )	
								try:
									assert(sponsor["topBarSponsor"]["name"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["name"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["image"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["image"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["logo"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in logo %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["logo"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["description"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in description %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["description"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["type"] == "sponsor")
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["type"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"] in sponsor["topBarSponsor"]["image"])
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["image"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"] in sponsor["topBarSponsor"]["logo"])	
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in logo %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["logo"]) ) )	
							except KeyError:
								pass
						for keys_data in value:
							try:
								try:
									assert(keys_data["name"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(keys_data["ppId"]%keys_data["name"]) ) )
								try:	
									assert(keys_data["ppId"]!=None)
								except AssertionError, e:
									raise( AssertionError( "\nproblem in ppId ==> %s"%keys_data["ppId"])) 
								try:	
									assert(keys_data["type"]=="video" or keys_data["type"]=="channel" )
								except AssertionError, e:
									raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(keys_data["ppId"]%keys_data["type"]) ) )
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
########################## FOR HOTSPOT COLLECTION API TESTING#################################
def test_hotspotcollection():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for channel in value:
				try:
					assert(channel["type"]=="collection")
				except AssertionError, e:
					raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(channel["ppId"]%channel["type"]) ) )
				try:
					assert(channel["type"] in channel["ppId"])
				except AssertionError, e:
					raise( AssertionError( "\nproblem in type and ppId in  %s "%channel["ppId"] ) )
				try:	
					assert(channel["status"] == True or channel["status"])
				except AssertionError, e:
					raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(channel["ppId"]%channel["status"]) ) )
				try:	
					assert(channel["posterSmall"] != None)
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
					raise( AssertionError( "\nproblem in ppId ==> %s"%channel["ppId"]) )

def test_collectionidshotspot():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		for value in data["data"]["pageDetails"]:
			for collection in value:
				url_for_ids="http://pressplaytv.in/api/v1/collection/"+collection["ppId"]+"?pageLen=1000&pageNum=1"
				response_ids= urllib2.urlopen(url_for_ids)
				data_id = json.loads(response_ids.read())
				for value in data_id["data"]["itemContents"]:
						for sponsor in value:
							try:
								for data in  sponsor["preRollPool"]:
									try:
										assert(data["status"] == True )
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(data["ppId"]%data["status"]) ) )
									try:	
										assert(data["ppId"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s  "%data["ppId"] ) )
									try:	
										assert(data["sponsorId"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in sponsorId %s "%(data["ppId"]%data["sponsorId"]) ) )
									try:	
										assert(data["type"] == "pre_roll")
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(data["ppId"]%data["type"]) ) )
									try:	
										assert(data["sponsorId"] in data["playbackUrl"])
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(data["ppId"]%data["playbackUrl"]) ) )
									try:	
										assert(data["playbackUrl"]!=None)
									except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in playbackUrl %s "%(data["ppId"]%data["playbackUrl"]) ) )
							except KeyError:
								pass
							try:
								try:
									assert(sponsor["topBarSponsor"]["status"] ==True)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in status %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["status"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s"%sponsor["topBarSponsor"]["ppId"]) )	
								try:
									assert(sponsor["topBarSponsor"]["name"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["name"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["image"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["image"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["logo"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in logo %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["logo"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["packageName"] != None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in packageName %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["packageName"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["description"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in description %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["description"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["type"] == "sponsor")
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["type"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"] in sponsor["topBarSponsor"]["image"])
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in image %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["image"]) ) )	
								try:
									assert(sponsor["topBarSponsor"]["ppId"] in sponsor["topBarSponsor"]["logo"])	
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in logo %s "%(sponsor["topBarSponsor"]["ppId"]%sponsor["topBarSponsor"]["logo"]) ) )	
							except KeyError:
								pass
						for keys_data in value:
							try:
								try:
									assert(keys_data["name"]!=None)
								except AssertionError, e:
										raise( AssertionError( "\nproblem in ppId ==> %s in name %s "%(keys_data["ppId"]%keys_data["name"]) ) )
								try:	
									assert(keys_data["ppId"]!=None)
								except AssertionError, e:
									raise( AssertionError( "\nproblem in ppId ==> %s"%keys_data["ppId"])) 
								try:	
									assert(keys_data["type"]=="video" or keys_data["type"]=="channel" )
								except AssertionError, e:
									raise( AssertionError( "\nproblem in ppId ==> %s in type %s "%(keys_data["ppId"]%keys_data["type"]) ) )
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
								try:
									assert(keys_data["isPremium"]=="no" or keys_data["isPremium"]=="yes" )
								except KeyError:
									pass
							except KeyError:
								pass