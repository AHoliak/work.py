import json
import os

def getAverageForOutput(dir, output, serial_number):
	foundLists=[]
	for filename in os.listdir(dir):
		cur_file = os.path.join(dir, filename)
		if os.path.isfile(cur_file):
			with open(cur_file, 'r') as f:
				# Load the contents of the file into a dictionary
				data = json.load(f)
				for item in data["data"]:
					serialNumber = item["serialNumber"]
					if serialNumber==serial_number and item["output"]==output:
						foundLists.append(item["energyValues"])
	average = []
	
	if len(foundLists) != 3:
		raise ValueError("No data found for this output/serial number combination: "+output+","+serial_number)

	for i in range(len(foundLists)):
		if i>0 and len(foundLists[i]) != len(foundLists[i-1]):
			raise ValueError("energyValues have different length!!!")
		
	for i in range(len(foundLists[0])):
		curSum = 0.0
		for j in range(len(foundLists)):
			curSum += foundLists[j][i]
		average.append(curSum/len(foundLists))
	print(f"serialNumber: {serial_number}; Output: {output}; Average energyValues: {average}")
	return average

getAverageForOutput("NewAirPodsData", "Left", "H2LHF4FF035Y")
print("====")
getAverageForOutput("NewAirPodsData", "Right", "H1CHLV750360")

