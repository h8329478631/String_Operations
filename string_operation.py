#Slicing operations on self name

Name = "Harshal Warke"

#------------Positive Indexing-------------
#String is H a r s h a l  space   W a r  k  e
#index is  0 1 2 3 4 5 6    7     8 9 10 11 12

#------------Negative Indexing-------------
#String is  H   a   r   s   h  a  l  space   W  a   r  k  e
#index is  -13 -12 -11 -10 -9 -8 -7   -6    -5  -4 -3 -2 -1


#----------------------- positive + positive index -----------------------

slice1_1 = Name[0:7]   # From index 0 to 6
slice1_2 = Name[8:14]  # From index 8 to end
slice1_3 = Name[0:5]   # From index 0 to 4
slice1_4 = Name[8:11]  # From index 8 to 10
slice1_5 = Name[3:7]   # From index 3 to 6

print("----------------------- positive + positive index --------------------------------------------------------------------------------------")
print("This is a Name - ",Name)
print(slice1_1)  #Op is Harshal
print(slice1_2)  #Op is Warke
print(slice1_3)  #Op is Harsh
print(slice1_4)  #Op is War
print(slice1_5) #OP is shal



#----------------------- negative + negative index -----------------------

slice2_1 = Name[-13:-6]  # From -13 to -7
slice2_2 = Name[-5:]     # From -5 to end
slice2_3 = Name[-13:-8]  # From -13 to -9
slice2_4 = Name[-5:-2]   # From -5 to -3
slice2_5 = Name[-10:-6]  # From -10 to -7

print("----------------------- neagative + negative index --------------------------------------------------------------------------------------")
print("This is a Name - ",Name)
print(slice2_1)  #Op is Harshal
print(slice2_2)  #Op is Warke
print(slice2_3)  #Op is Harsh
print(slice2_4)  #Op is War
print(slice2_5) #OP is shal


#----------------------- positive + negative index -----------------------

slice3_1 = Name[0:-6]   # From 0 to -7
slice3_2 = Name[8:]     # From 8 to end
slice3_3 = Name[0:-8]   # From 0 to -9
slice3_4 = Name[8:-2]   # From 8 to -3
slice3_5 = Name[3:-6]   # From 3 to -7

print("----------------------- positive + negative index --------------------------------------------------------------------------------------")
print("This is a Name - ",Name)
print(slice3_1)  #Op is Harshal
print(slice3_2)  #Op is Warke
print(slice3_3)  #Op is Harsh
print(slice3_4)  #Op is War
print(slice3_5) #OP is shal



#----------------------- negative + positive index -----------------------

slice4_1 = Name[-13:7]  # From -13 to 6
slice4_2 = Name[-5:13]  # From -5 to 12
slice4_3 = Name[-13:5]  # From -13 to 4
slice4_4 = Name[-5:11]  # From -5 to 10
slice4_5 = Name[-10:7]  # From -10 to 6

print("----------------------- negative + positive index --------------------------------------------------------------------------------------")
print("This is a Name - ",Name)
print(slice4_1)  #Op is Harshal
print(slice4_2)  #Op is Warke
print(slice4_3)  #Op is Harsh
print(slice4_4)  #Op is War
print(slice4_5) #OP is shal



#----------------------- positive index with negative step -----------------------

slice6_1 = Name[::-1]    # Reverse full string
slice6_2 = Name[::-2]    # Reverse with step 2
slice6_3 = Name[6::-1]   # Reverse from index 6 to start
slice6_4 = Name[10:7:-1] # Reverse from 10 to 8
slice6_5 = Name[6:2:-1]  # Reverse from 6 to 3
 


print("----------------------- positive index with negative setp size --------------------------------------------------------------------------------------")
print("This is a Name - ",Name)
print(slice6_1)  #Op is ekraW lahsraH
print(slice6_2)  #Op is erWlhrH
print(slice6_3)  #Op is lahsraH
print(slice6_4)  #Op is raW
print(slice6_5) #OP is lahs

#----------------------- positive index with positive step -----------------------

slice7_1 = Name[::1]     # Full string (normal step)
slice7_2 = Name[::2]     # Every 2nd character
slice7_3 = Name[0:7:2]   # From 0 to 6, step 2
slice7_4 = Name[8:13:2]  # From 8 to 12, step 2
slice7_5 = Name[3:10:3]  # From 3 to 9, step 3


print("----------------------- positive index with positive step size -----------------------")
print("This is a Name - ", Name)
print(slice7_1)  # Op is Harshal Warke
print(slice7_2)  # Op is HrhlWre
print(slice7_3)  # Op is Hrhl
print(slice7_4)  # Op is Wre
print(slice7_5)  # Op is sla






