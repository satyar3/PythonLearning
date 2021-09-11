import os

print(dir(os))
print(os.getcwd())
print(os.name)
# os.chdir("C:\\")
# print(os.getcwd())
print(os.listdir(os.getcwd()))
# os.mkdir("Some_name")
# os.makedirs("some_folder/inside_some_folder")
# os.rename("old_name.txt","new_name.txt")
print(os.environ.get('Path'))
print(os.path.join("C:\\\\","//Txt.txt"))

print(os.path.exists("C://"))
print(os.path.isdir("C://"))
print(os.path.isfile("C://"))