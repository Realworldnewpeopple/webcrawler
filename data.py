from crawler import getlink
import json

def main(dat):
	for i in range(0,len(dat['CIN'])):
		try:
			soup=getlink(dat['url'],dat['CIN'][i])
			with open( r"./saved_data/"+str(dat['CIN'][i])+".txt" ,"w") as oFile:
				oFile.write(str(soup.html))
				oFile.close()
		except:
			print("Captch error")
			soup=getlink(dat['url'],dat['CIN'][i])
			with open( r"./saved_data/"+str(dat['CIN'][i])+".txt" ,"w") as oFile:
				oFile.write(str(soup.html))
				oFile.close()
			continue

if __name__ == "__main__":
	with open("./json/input.json", "r+") as data:
		json_data=json.load(data)
	
	main(json_data)
