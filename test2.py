from esp32 import Partition

for p in Partition.find(Partition.TYPE_APP):
    print(p)
    
print("active partition2:", Partition(Partition.RUNNING).info()[4])