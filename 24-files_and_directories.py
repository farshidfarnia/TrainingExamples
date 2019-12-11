from pathlib import Path


# Absolute path
# for windows => c:\Program Files\Microsoft
# for mac => /user/local/bin

# Relative path
# for example "ecommerce" directory

# path = Path("ecommerce")
# print(path.exists())
# path = Path("emails")
# Create new directory called "emails" by "mkdir"
# print(path.mkdir())
# Delete directory called "emails" by "rmdir"
# print(path.rmdir())

path = Path()
for file in path.glob("*"):
    print(file)