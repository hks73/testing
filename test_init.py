##################################
import urllib2
import urllib
import sys
import json
import requests
###################################

url_for_internet="http://api.pressplaytv.in/v1/init"
url_for_hotspot="http://pressplaytv.in/api/v1/init"

def check_url(url):
	ret=requests.head(url)
	return ret.status_code

########################## FOR INTERNET INIT API #################################
def test_internet():
	if check_url(url_for_internet)<400:
		response= urllib2.urlopen(url_for_internet)
		data = json.loads(response.read())
		###### PRINT MAIN POINT IN TESTING #########
		if data["data"]["environment"]=="internet":
			print "\n"
			print "Environment ==> "+ data["data"]["environment"]
			print "Login Enabled for DeepLink ==> "+str(data["data"]["loginEnabledForDeepLink"])
	
			######### ASSERT CONDITIONS FOR TESTING #################
			try:
				assert (data["data"]["appUpdate"] == "force" or data["data"]["appUpdate"] == "shallow")
				assert (type(data["data"]["minAppVersion"])== int)	
				print "App Update ==> "+data["data"]["appUpdate"]
			except KeyError:
				pass
			try:
				assert (data["data"]["loginUrl"] == "/login") 
			except AssertionError:
				raise( AssertionError( "\nproblem in loginUrl in init api" ) )	
			try:
				assert(data["data"]["environment"] == "internet")
			except AssertionError:
				raise( AssertionError( "\nproblem in environment in init api" ) )	
			try:
				assert (data["data"]["loginEnabledForDeepLink"]==False or data["data"]["loginEnabledForDeepLink"]==True)
			except AssertionError:
				raise( AssertionError( "\nproblem in loginEnabledForDeepLink in init api" ) )	
			for value in data["data"]["sections"]:
				try:
					assert ((value['header'] == "home" and  value['androidHeader'] == "TRENDING" and value['endpoint'] == "/home") or \
					(value['header'] == "channel" and  value['androidHeader'] == "CHANNELS" and value['endpoint'] == "/channel") or \
					(value['header'] == "collection" and  value['androidHeader'] == "COLLECTIONS" and value['endpoint'] == "/collection"))
				except AssertionError:
					raise( AssertionError( "\nproblem in header,androidHeader,endpoint in init api" ) )

########################## FOR HOTSPOT INIT API #################################

def test_hotspot():
	if check_url(url_for_hotspot)<400:
		response= urllib2.urlopen(url_for_hotspot)
		data = json.loads(response.read())
		if data["data"]["environment"]=="hotspot":
			###### PRINT MAIN POINT IN TESTING #########
			print "\n"
			print "Environment ==> "+ data["data"]["environment"]
			print "Logged ==> "+ str(data["logged"])
			
			######### ASSERT CONDITIONS FOR TESTING #################
			try:
				assert(data["data"]["environment"] == "hotspot")
			except AssertionError:
				raise( AssertionError( "\nproblem in environment in init api" ) )
			try:
				assert (data["logged"] == False or data["logged"] == True ) 
			except AssertionError:
				raise( AssertionError( "\nproblem in logged in init api" ) )
			try:
				assert (data["data"]["loginUrl"] == "/") 
			except AssertionError:
				raise( AssertionError( "\nproblem in loginUrl in init api" ) )	
			try:	
				assert (type(data["data"]["box-id"])== int)
			except AssertionError:
				raise( AssertionError( "\nproblem in box-id in init api" ) )
			try:
				assert (type(data["data"]["content-version"])== int)
			except AssertionError:
					raise( AssertionError( "\nproblem in content-version in init api" ) )
			try:
				assert (data["data"]["app-version"] !="")
			except AssertionError:
				raise( AssertionError( "\nproblem in app-version in init api" ) )
			try:		
				assert (data["data"]["web-media-download"] == 'true' or data["data"]["web-media-download"] == True)
			except AssertionError:
					raise( AssertionError( "\nproblem in web-media-download in init api" ) )
			try:
				assert (data["data"]["app-media-download"] == 'true' or data["data"]["app-media-download"] == True )
			except AssertionError:
					raise( AssertionError( "\nproblem in app-media-download in init api" ) )	
			try:
				assert (data["data"]["appUpdate"] == "force" or data["data"]["appUpdate"] == "shallow")
				assert (type(data["data"]["minAppVersion"])== int)	
				print "App Update ==> "+data["data"]["appUpdate"]
			except KeyError:
					pass
			except AssertionError:
					raise( AssertionError( "\nproblem in appUpdate in init api" ) )
			for value in data["data"]["sections"]:
				try:
					assert ((value['header'] == "home" and  value['androidHeader'] == "TRENDING" and value['endpoint'] == "home") or \
					(value['header'] == "channel" and  value['androidHeader'] == "CHANNELS" and value['endpoint'] == "channel") or \
					(value['header'] == "collection" and  value['androidHeader'] == "COLLECTIONS" and value['endpoint'] == "collection"))
				except AssertionError:
					raise( AssertionError( "\nproblem in header,androidHeader,endpoint in init api" ) )