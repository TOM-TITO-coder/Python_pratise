# f = open("D:\\DATA Science\\funny.txt", "r")
# f_out = open("D:\\DATA Science\\funny_wc.txt", "w")

# # r: opens file for reading oly. Throws error if file does not exist.
# # w: opens file for writing only. If file doesn't exist the it eill create new one. If it exist the it will overwrite it.
# # a: Opens a file in append mode. Whatever you write to file will get appended and original content will not be overwritten

# # f.write("I love you.")
# #print(f.read())

# # for line in f:
# #     print(line)

# for line in f:
#     tokens = line.split(" ")
#     f_out.write("Wordcount: " + str(len(tokens)) + line)
#     #print(str(tokens))
#     #print(len(tokens))
    
# f.close()
# f_out.close()

with open("D:\\DATA Science\\funny.txt", "r") as f:
    print(f.read())

print(f.closed)