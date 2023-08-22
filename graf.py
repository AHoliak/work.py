
import matplotlib.pyplot as plt


with open('number_of_tx_packets.txt') as f:
  my_list1 = [ int(i) for i in f ]
with open('number_of_retransmitted_packets.txt') as f:
  my_list2 = [ int(i) for i in f ]
	
total1=0
total2=0

for n in my_list1:
	total1 += n
for m in my_list2:
	total2 += m 
print("Number of tests:",len(my_list1))
print( "Number of TX packets:",total1, "\nNumber of Retransmitted packets:",total2)

result = total2/total1*100
print ("Percentage of lost packets:",  str(int(result))+"%")


z = [m/n for m, n in zip(my_list2,my_list1)]

final_list=[]
for i in z:
	final_list.append(int(i*100))



plt.xlabel('Number of tests')
# naming the y axis
plt.ylabel('Packets loss (%)')
plt.plot(final_list, color="orange")
plt.show()
