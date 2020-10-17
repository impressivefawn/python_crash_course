# 9-11. Imported Admin:
from privileges import User, Admin, Privileges

stylish_fortnite = Admin('stylish', 'fortnite', '@stylishfortnite', 'stylishfortnite@gmail.com')
stylish_fortnite.privileges.show_privileges()