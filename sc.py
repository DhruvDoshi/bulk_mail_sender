lst = []
# open file in read mode
with open("abc.txt", 'r') as file_handle:
    # read file content into list
    lines = file_handle.readlines()
# print list content
    lst.append(lines)

print(lst)
# with open("abc.txt", 'r') as file_handles:
#     file_handles.write(lst)
with open('your_file.txt', 'w') as f:
    for item in lst:
        f.write("%s\n" % item)