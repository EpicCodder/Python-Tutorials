

# Python os module


import os


# properties inside the os function
# print(dir(os))


# We can read the documentation of os module


###########################################################

# making new folder using os module
# os.mkdir("experiment")

# This will throw error if the folder is already present 


# Now we resolvve the error
# if(not os.path.exists("experiment")):
#     os.mkdir("experiment")


# # This will make 100 folders inside the experiment folder
# for i in range(1, 101):
#     os.mkdir(f"experiment/Day{i}")



# for i in range(1, 101):
#     os.mkdir(f"experiment2/day{i}")


####################################################################

# We can search on google how to rename folders in python


# if not os.path.exists("experiment"):
#     os.mkdir("experiment")


# for i in range(1, 101):
#     os.mkdir(f"experiment/Day{i}")


# It will rename all the file

# for i in range(1, 101):
#     os.rename(f"experiment/Day{i}", f"experiment/Tutorial {i}")

#####################################################################33

# How we can see and print all the directories in the folder

# folders = os.listdir("experiment")
# # print(folders)

# for folder in folders:
#     print(folder)


######################################################################

# We can also check the folders inside the folder

# os.mkdir(f"experiment/Tutorial 90/Legends")

# Now we print directories inside the directories

# folders = os.listdir("experiment")

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"experiment/{folder}"))



#################################################################

# os.getcwd() tell us current working directory in which we are working
# print(os.getcwd())


# We can also change the directory using this method



os.chdir("experiment")

print(os.getcwd())
print(os.listdir())


# We can also use ch util module



