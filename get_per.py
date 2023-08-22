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

print("Number of Tx Packets:", total1, "\nNumber of Retransmitted Packets:", total2)

result = total2/total1*100
print ("Percentage:",int(result),"%")
