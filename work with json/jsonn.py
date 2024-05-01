#https://sabzlearn.ir/lesson/25-26799/
import json


###############################################################################
#loads => str
#load => file

# with open(r"A:\Python\MY_projects\opencv\work with json\\test.json", "r") as jf:
#     data = json.load(jf)

# print(data["accounts"][2]["name"], data["accounts"][2]["id"])


###############################################################################


boli = False
def inpu():
    global x, y ,z , d
    x =input("you name: ")
    z = input("your id: ")
    y = int(input("cod mali cod"))
    
    d = {
        "name" : x,
        "id" : z,
        "mali" : y
    }
    print(d)
    
inpu()

# with open(r"A:\Python\MY_projects\opencv\work with json\\test2.json", "a") as jf:
#     json.dump({"account" : d}, jf)

# باز کردن فایل JSON و خواندن اطلاعات قبلی
with open(r"A:\Python\MY_projects\opencv\work with json\\test2.json", "r") as jf:
    data = json.load(jf)

# افزودن اطلاعات جدید به لیست اکانت‌ها
data["accounts"].append(d)

# ذخیره اطلاعات به فایل JSON
with open(r"A:\Python\MY_projects\opencv\work with json\\test2.json", "w") as jf:
    json.dump(data, jf, indent = 3)


### 
# دیفالت باید در جیسونت وجود داشته باشه
# {
#   "accounts": []
# }
#
############################################################################



























# import json

# # باز کردن فایل JSON
# with open(r"A:\Python\MY_projects\opencv\work with json\\test.json", "r") as jf:
#     data = json.load(jf)
#     accounts = data["accounts"]

# # نام دانش‌آموز را از کاربر دریافت کنید
# student_name = input("نام دانش‌آموز را وارد کنید: ")

# # جستجو در اطلاعات دانش‌آموزان
# found_student = None
# for student in accounts:
#     if student["name"] == student_name:
#         found_student = student
#         break

# # نمایش اطلاعات دانش‌آموز
# if found_student:
#     print(f"شناسه: {found_student['id']}")
#     print("نمرات:")
#     for subject, grade in found_student['grades'].items():
#         print(f"{subject}: {grade}")
# else:
#     print("دانش‌آموزی با این نام یافت نشد.")

