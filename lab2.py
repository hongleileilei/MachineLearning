# ESE590
# Honglei Liu

# Weekly Lab
# Weekly Lab 1 is in class Memory
# Weekly Lab 2 is in class Clustering
# Data set chosen: Abalone

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import random
# Weekly Lab 1
class Memory():
	def __init__(self):
		self.sex_idx = {'M':[], 'F':[], 'I':[]}

		self.length = []
		self.dia = []
		self.height = []

		self.whole_wei = []
		self.shuck_wei = []
		self.visce_wei = []
		self.shell_wei = []

		self.ring = []

	def push_index(self, info: str, index: int) -> None:
		attri = info.split(',')
		attri[-1] = attri[-1][:-1]

		self.sex_idx[attri[0]].append(index)

		self.length.append(float(attri[1]))
		self.dia.append(float(attri[2]))
		self.height.append(float(attri[3]))
		self.whole_wei.append(float(attri[4]))
		self.shuck_wei.append(float(attri[5]))
		self.visce_wei.append(float(attri[6]))
		self.shell_wei.append(float(attri[7]))
		self.ring.append(int(attri[8]))

	def test(self) -> None:
		difference = [i for i in self.sex_idx['M'] + self.sex_idx['I'] if i not in self.sex_idx['M'] or i not in self.sex_idx['I']] 
		print(difference)

	def max_min(self) -> None:
		print("max age in data: ",1.5+max(self.ring))
		print("min age in data: ",1.5+min(self.ring))
		less_10 = 0
		less_20 = 0
		more_20 = 0
		for ring in self.ring:
			ring = ring + 1.5
			if ring < 10:
				less_10 += 1
			elif ring < 20:
				less_20 += 1
			else:
				more_20 += 1
		print("less than 10 has: ", less_10)
		print("10 to 20 has: ", less_20)
		print("more than 20 has: ", more_20)
		print("number of male: ",len(self.sex_idx['M']))
		print("number of female: ",len(self.sex_idx['F']))
		print("number of infant: ",len(self.sex_idx['I']))
		pass

	def plotting(self) -> None:
		# Plotting three Graphs, one for diameters, one for weights and one for ring

		#print(self.sex_idx)
		length_m, length_f, length_i = [], [], []
		dia_m, dia_f, dia_i = [], [], []
		height_m, height_f, height_i = [], [], []
		w_wei_m, w_wei_f, w_wei_i = [], [], []
		k_wei_m, k_wei_f, k_wei_i = [], [], []
		v_wei_m, v_wei_f, v_wei_i = [], [], []
		s_wei_m, s_wei_f, s_wei_i = [], [], []
		ring_m, ring_f, ring_i = [], [], []

		for sex in self.sex_idx:
			if sex == 'M':
				for index in range(len(self.sex_idx[sex])):
					length_m.append(self.length[self.sex_idx[sex][index]])
					dia_m.append(self.dia[self.sex_idx[sex][index]])
					height_m.append(self.height[self.sex_idx[sex][index]])
					w_wei_m.append(self.whole_wei[self.sex_idx[sex][index]])
					k_wei_m.append(self.shuck_wei[self.sex_idx[sex][index]])
					v_wei_m.append(self.visce_wei[self.sex_idx[sex][index]])
					s_wei_m.append(self.shell_wei[self.sex_idx[sex][index]])
					ring_m.append(self.ring[self.sex_idx[sex][index]])
			elif sex == 'F':
				for index in range(len(self.sex_idx[sex])):
					length_f.append(self.length[self.sex_idx[sex][index]])
					dia_f.append(self.dia[self.sex_idx[sex][index]])
					height_f.append(self.height[self.sex_idx[sex][index]])
					w_wei_f.append(self.whole_wei[self.sex_idx[sex][index]])
					k_wei_f.append(self.shuck_wei[self.sex_idx[sex][index]])
					v_wei_f.append(self.visce_wei[self.sex_idx[sex][index]])
					s_wei_f.append(self.shell_wei[self.sex_idx[sex][index]])
					ring_f.append(self.ring[self.sex_idx[sex][index]])
			elif sex == 'I':
				for index in range(len(self.sex_idx[sex])):
					length_i.append(self.length[self.sex_idx[sex][index]])
					dia_i.append(self.dia[self.sex_idx[sex][index]])
					height_i.append(self.height[self.sex_idx[sex][index]])
					w_wei_i.append(self.whole_wei[self.sex_idx[sex][index]])
					k_wei_i.append(self.shuck_wei[self.sex_idx[sex][index]])
					v_wei_i.append(self.visce_wei[self.sex_idx[sex][index]])
					s_wei_i.append(self.shell_wei[self.sex_idx[sex][index]])
					ring_i.append(self.ring[self.sex_idx[sex][index]])				


		plt.figure(1)
		plt.subplot(2,2,1)
		plt.scatter(length_m, w_wei_m, color = 'red')
		plt.scatter(length_f, w_wei_f, color = 'green')
		plt.scatter(length_i, w_wei_i, color = 'blue')
		plt.title('length(x) vs whole weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,2)
		plt.scatter(length_m, k_wei_m, color = 'red')
		plt.scatter(length_f, k_wei_f, color = 'green')
		plt.scatter(length_i, k_wei_i, color = 'blue')
		plt.title('length(x) vs shuck weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,3)
		plt.scatter(length_m, v_wei_m, color = 'red')
		plt.scatter(length_f, v_wei_f, color = 'green')
		plt.scatter(length_i, v_wei_i, color = 'blue')
		plt.title('length(x) vs viscera weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,4)
		plt.scatter(length_m, s_wei_m, color = 'red')
		plt.scatter(length_f, s_wei_f, color = 'green')
		plt.scatter(length_i, s_wei_i, color = 'blue')
		plt.title('length(x) vs shell weight(y). (male: red, female: green, infant: blue)')
		#plt.axis('off')
		plt.show()

		plt.figure(2)
		plt.subplot(2,2,1)
		plt.scatter(dia_m, w_wei_m, color = 'red')
		plt.scatter(dia_f, w_wei_f, color = 'green')
		plt.scatter(dia_i, w_wei_i, color = 'blue')
		plt.title('diameter(x) vs whole weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,2)
		plt.scatter(dia_m, k_wei_m, color = 'red')
		plt.scatter(dia_f, k_wei_f, color = 'green')
		plt.scatter(dia_i, k_wei_i, color = 'blue')
		plt.title('diameter(x) vs shuck weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,3)
		plt.scatter(dia_m, v_wei_m, color = 'red')
		plt.scatter(dia_f, v_wei_f, color = 'green')
		plt.scatter(dia_i, v_wei_i, color = 'blue')
		plt.title('diameter(x) vs viscera weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,4)
		plt.scatter(dia_m, s_wei_m, color = 'red')
		plt.scatter(dia_f, s_wei_f, color = 'green')
		plt.scatter(dia_i, s_wei_i, color = 'blue')
		plt.title('diameter(x) vs shell weight(y). (male: red, female: green, infant: blue)')
		#plt.axis('off')
		plt.show()

		plt.figure(3)
		plt.subplot(2,2,1)
		plt.scatter(height_m, w_wei_m, color = 'red')
		plt.scatter(height_f, w_wei_f, color = 'green')
		plt.scatter(height_i, w_wei_i, color = 'blue')
		plt.title('height(x) vs whole weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,2)
		plt.scatter(height_m, k_wei_m, color = 'red')
		plt.scatter(height_f, k_wei_f, color = 'green')
		plt.scatter(height_i, k_wei_i, color = 'blue')
		plt.title('height(x) vs shuck weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,3)
		plt.scatter(height_m, v_wei_m, color = 'red')
		plt.scatter(height_f, v_wei_f, color = 'green')
		plt.scatter(height_i, v_wei_i, color = 'blue')
		plt.title('height(x) vs viscera weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,4)
		plt.scatter(height_m, s_wei_m, color = 'red')
		plt.scatter(height_f, s_wei_f, color = 'green')
		plt.scatter(height_i, s_wei_i, color = 'blue')
		plt.title('height(x) vs shell weight(y). (male: red, female: green, infant: blue)')
		#plt.axis('off')
		plt.show()

		plt.figure(4)
		plt.subplot(2,2,1)
		plt.scatter(ring_m, w_wei_m, color = 'red')
		plt.scatter(ring_f, w_wei_f, color = 'green')
		plt.scatter(ring_i, w_wei_i, color = 'blue')
		plt.title('rings(x) vs whole weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,2)
		plt.scatter(ring_m, k_wei_m, color = 'red')
		plt.scatter(ring_f, k_wei_f, color = 'green')
		plt.scatter(ring_i, k_wei_i, color = 'blue')
		plt.title('rings(x) vs shuck weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,3)
		plt.scatter(ring_m, v_wei_m, color = 'red')
		plt.scatter(ring_f, v_wei_f, color = 'green')
		plt.scatter(ring_i, v_wei_i, color = 'blue')
		plt.title('rings(x) vs viscera weight(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(2,2,4)
		plt.scatter(ring_m, s_wei_m, color = 'red')
		plt.scatter(ring_f, s_wei_f, color = 'green')
		plt.scatter(ring_i, s_wei_i, color = 'blue')
		plt.title('rings(x) vs shell weight(y). (male: red, female: green, infant: blue)')
		#plt.axis('off')
		plt.show()

		plt.figure(5)
		plt.subplot(1,3,1)
		plt.scatter(ring_m, length_m, color = 'red')
		plt.scatter(ring_f, length_f, color = 'green')
		plt.scatter(ring_i, length_i, color = 'blue')
		plt.title('rings(x) vs length(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(1,3,2)
		plt.scatter(ring_m, dia_m, color = 'red')
		plt.scatter(ring_f, dia_f, color = 'green')
		plt.scatter(ring_i, dia_i, color = 'blue')
		plt.title('rings(x) vs diameter(y). (male: red, female: green, infant: blue)')
		#plt.show()
		#plt.axis('off')
		plt.subplot(1,3,3)
		plt.scatter(ring_m, height_m, color = 'red')
		plt.scatter(ring_f, height_f, color = 'green')
		plt.scatter(ring_i, height_i, color = 'blue')
		plt.title('rings(x) vs height(y). (male: red, female: green, infant: blue)')
		#plt.axis('off')
		plt.show()


# Weekly Lab 2
class Clustering():
	def __init__(self):
		column_names = ["sex","length","diameter","height","whole weight","shucked weight","viscera weight","shell weight","rings"]
		self.df = pd.read_csv('abalone.data', names = column_names)
		#self.df['sex'] = pd.to_numeric(self.df['sex'])
		print(self.df.head())

		##########
		# we want to implement a k-means clustering in weekly lab 2
		# the reason we choose k equals to 2 is from the paper
		# https://www.researchgate.net/publication/263057551_Decision_Trees_and_Data_Preprocessing_to_Help_Clustering_Interpretation#pf6
		##########
		self.k = 2

		self.centroids = []
		self.prev_cent = []
		# show clusters as index
		self.clusters = []
		self.preprocessing()
	
	def test(self):
		array = self.df.iloc[:,1:8].values
		plt.boxplot(array)
		plt.xlabel("attri idx")
		plt.ylabel("quartile range")
		plt.show()

	def preprocessing(self) -> None:
		for i in range(self.k):
			self.centroids.append([])
			self.centroids[i].append(round(random.uniform(self.df["length"].min(), self.df["length"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["diameter"].min(), self.df["diameter"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["height"].min(), self.df["height"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["whole weight"].min(), self.df["whole weight"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["shucked weight"].min(), self.df["shucked weight"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["viscera weight"].min(), self.df["viscera weight"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["shell weight"].min(), self.df["shell weight"].max()),4))
			self.centroids[i].append(round(random.uniform(self.df["rings"].min(), self.df["rings"].max()),4))
			self.clusters.append([])
			self.prev_cent.append([])
			for _ in range(len(self.centroids[i])):
				self.prev_cent[i].append(0)
		return

	def diff_cent(self) -> bool:
		# Calculate difference between previous centroid
		# return True if all smaller than 0.01
		# else return False, which means need to another iteration
		print()
		print("cent 0 prev and current: ")
		print(self.prev_cent[0])
		print(self.centroids[0])
		print("cent 1 prev and current: ")
		print(self.prev_cent[1])
		print(self.centroids[1])
		print()

		for i in range(len(self.centroids)):
			for j in range(len(self.centroids[i])):
				if abs(self.centroids[i][j] - self.prev_cent[i][j]) == 0:
					continue
				else:
					print("difference disagreement at index: ",i," ",j)
					return False
		return True


	def diff_cal(self, p1: list, p2: list) -> int:
		res = 0
		for i in range(len(p1)):
			res += ((p1[i] - p2[i])**2)
		res = round(res**0.5,4)
		return res

	def recenter(self) -> None:
		arr = self.df.iloc[:,1:9].values
		new_cent = []
		for i in range(len(self.centroids)):
			new_cent.append([])
			for j in range(len(self.centroids[i])):
				new_sum = 0
				for idx in self.clusters[i]:
					new_sum += arr[idx][j]
				new_cent[i].append(round(new_sum/len(self.clusters[i]), 4))
		self.centroids = new_cent.copy()
		return

	def plot(self) -> None:
		arr = self.df.iloc[:,1:9].values
		whole_weight_0 = []
		length_0 = []
		whole_weight_1 = []
		length_1 = []
		cent_x = []
		cent_y = []
		for item in self.centroids:
			cent_x.append(item[0])
			cent_y.append(item[3])
		for i in range(len(arr)):
			if i in self.clusters[0]:
				whole_weight_0.append(arr[i][3])
				length_0.append(arr[i][0])
			else:
				whole_weight_1.append(arr[i][3])
				length_1.append(arr[i][0])				
		
		plt.figure(1)
		plt.scatter(length_0, whole_weight_0,color='red')
		plt.scatter(length_1, whole_weight_1,color='blue')
		plt.scatter(cent_x,cent_y,color = 'yellow')
		plt.show()
		return

	def k_means(self) -> None:
		# Implementing k-means clustering in a 8-dimension matrix
		# ignore sex column and rearrange it to array

		arr = self.df.iloc[:,1:9].values
		iter_count = 0
		diff_cent_res = self.diff_cent()
		while diff_cent_res is False:
			iter_count += 1
			self.prev_cent = self.centroids.copy()
			for i in range(len(arr)):
				diff_0 = self.diff_cal(arr[i],self.centroids[0])
				diff_1 = self.diff_cal(arr[i],self.centroids[1])
				if diff_0 < diff_1:
					self.clusters[0].append(i)
				else:
					self.clusters[1].append(i)
			print("current count of two clusters: No.1: ",len(self.clusters[0])," No.2: ",len(self.clusters[1]))
			# For each iteration, we want to plot the graph and see the changes
			self.plot()

			# re-center the centroid and then continue the loop
			self.recenter()
			for cluster in self.clusters:
				cluster.clear()
			
			diff_cent_res = self.diff_cent()

		print("iteration goes: ",iter_count, " times")
		return

	def decision_tree(self) -> None:
		pass

	def dbscan(self) -> None:
		pass


def main():
	Clu = Clustering()
	#Clu.test()
	Clu.k_means()
	return 0

if __name__ == "__main__":
	main()