#import csv
import pandas as pd

def read_barred(file):
	'''this function returns a list of names of interest, 
	with the name of file as the argument'''
	#names = []
	#with open(file, newline='') as f:
		#reader = csv.reader(f)
		#for row in reader:
			#names.append(names[1])
	#return names
	df = pd.read_csv(file)
	
	return df








	