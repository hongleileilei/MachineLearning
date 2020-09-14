import matplotlib.pyplot as plt
import numpy as np

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

	def test(self):
		difference = [i for i in self.sex_idx['M'] + self.sex_idx['I'] if i not in self.sex_idx['M'] or i not in self.sex_idx['I']] 
		print(difference)

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

		

def main():
	mem = Memory()

	f = open("abalone.data","r")
	lines = f.readlines()
	index = 0
	for line in lines:
		mem.push_index(line, index)
		index += 1
	f.close()
	mem.plotting()
	#mem.test()
	return 0

if __name__ == "__main__":
	main()