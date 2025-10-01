# Scenario
# A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

# The functions:
# are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
# take one argument (the value corresponding to their names)
# Complete the code in the editor.

# Run your code and check whether your output is the same as ours.
# Here is some information to help you:
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.

# # Expected output
# # 60.31143162393162
# # 31.36194444444444
# # 23.52145833333333
# # 3.9007393587617467
# # 7.490910297239916
# # 10.009131205673757

# def liters_100km_to_miles_gallon(literkms):
#     MilesPerGallon = 100*3.785411784/(1.609344*literkms)
#     return round(MilesPerGallon, 2)

# def miles_gallon_to_liters_100km(gallonmiles):
#     Liters100km = 100*3.785411784/(1.609344*gallonmiles)
#     return round(Liters100km, 2)



# # print(liters_100km_to_miles_gallon(3.9))
# # print(liters_100km_to_miles_gallon(7.5))
# # print(liters_100km_to_miles_gallon(10.))
# # print(miles_gallon_to_liters_100km(60.3))
# # print(miles_gallon_to_liters_100km(31.4))
# # print(miles_gallon_to_liters_100km(23.5))

# # for i in range(11):
# #     print(i)



# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)




# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# #for item in (d1, d2):
# #    d3.update(item)
# d3.update(d1)
# d3.update(d2)

# print(d3)




