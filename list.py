Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print(int(len(Belgium)) * "-")
print(Belgium.replace(",", ";"))

Belgium_list = Belgium.split(",")
print(Belgium_list)

Belguim_pop = int(Belgium_list[1])
Brussels_pop = int(Belgium_list[3])
print(Belguim_pop + Brussels_pop)