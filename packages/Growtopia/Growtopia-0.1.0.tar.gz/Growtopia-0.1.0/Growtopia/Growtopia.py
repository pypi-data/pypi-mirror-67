import os, random, socket, requests
class Growtopia:
	def __init__(self,path=os.getenv("LOCALAPPDATA")+"\\Growtopia"):
		
		"""Growtopia class for setting the Growtopia folder path
		
		Parameters:
			path (Path): Path to Growtopia folder, default is %LOCALAPPDATA%\Growtopia
		"""
		
		if !os.path.isdir(path):
			raise self.Exceptions.InvalidGrowtopiaPath("The Growtopia path is invalid.")
		
		self.path = path
	
	def loadSaveDat(self, path=os.getenv("LOCALAPPDATA")+"\\Growtopia\\save.dat"):
		
		"""Loads Growtopia custom save.dat file
			
		Parameters:
			path (Path): Path to the save.dat file, default is %LOCALAPPDATA%\Growtopia\save.dat
		"""
		
		if !os.path.isexist(path):
			raise self.Exceptions.InvalidGrowtopiaPath("Wrong file path!")
		
		self.saveDatPath = path
		
	def login(self, username, password, version="3.38"):
	
		"""Login to your account and return Account object
		
		Example:
			>> myAccount = Growtopia.login("Gogo333", "GogoIsTheBest", "1.00")
			>> print(myAccount.world)
			WHITETOPIANS
			>> myAccount.warp("WHITETOPIANS2")
			True
			>> pprint(myAccount.friends)
			[{
				"name": "HanzHaxors",
				"status": "online",
				"currentWorld": "WHITETOPIANS"
			 },{
				"name": "Seth",
				"status": "online",
				"currentWorld": "WHITETOPIANS"
			 },{
				"name": "Hamumu",
				"status": "offline",
				"currentWorld": ""
			}]
		
		Parameter:
			username (string): Username to login
			password (string): Password to complete the login process
			version (string float): String that contain float number of current Growtopia version
		"""
		
		try:
			float(version)
		except:
			raise InvalidGrowtopiaVersion("Invalid Growtopia version you should put float number without any letter(s)")
		
		# LOGIN PROCESS
		theSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
		theSock.sendto(bytes(msg, "utf-8"), ())
		
		# SendPacket(2, "tankIDName|" + uname + "\ntankIDPass|" + upass + "\nrequestedName|SmileZero\nf|0\nprotocol|38\ngame_version|" + ver + "\nfz|13812200\nlmode|0\ncbits|0\nhash2|"+hash2+"\nmeta|" + generateMeta() + "\nfhash|-716928004\nrid|" + generateRid() + "\nplatformID|0\ndeviceVersion|0\ncountry|cz\nhash|" + hash + "\nmac|" + generateMac() + "\nwk|" + generateRid() + "\nzf|13837395" + token, peer)
		# TODO:
		# [x] Version
		# [ ] hash2
		# [ ] Meta
		# [ ] RId
		# [ ] hash
		# [ ] token
		# [ ] peer
		# [ ] SendPacket in python
	
	def isServerUp():
		
		"""Function to check wheter the Growtopia server is up or not
		
		Type: bool
		"""
	
		txt = requests.get("https://growtopiagame.com/").text
		if "Server is up" in txt:
			return True
		elif "Server is down for maintenance" in txt:
			return False
	
	
	# Classes
	class Exceptions:
		class InvalidGrowtopiaPath(Error):
			"""If the Growtopia Path is invalid or its a file, then raise this"""
		class WrongCredential(Error):
			"""If the credential is wrong, raise this"""
		class InvalidGrowtopiaVersion(Error):
			"""Raised when user put letter 'V' or anything else instead of
			floating numbers
			"""
	
	class Generate:
		def Mac():
			return ':'.join('%02x'%random.randrange(256) for _ in range(5))