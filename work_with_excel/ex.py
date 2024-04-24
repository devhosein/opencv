import pandas as pd
import os
from datetime import datetime

dirname = os.path.dirname(__file__)


# تابعی برای دریافت ورودی از کاربر و ذخیره آن در فایل اکسل
def save_input_to_excel(file_path):
    
    # دریافت ورودی از کاربر
    user_input = input("لطفا مقدار را وارد کنید: ")
    
    # دریافت تاریخ و زمان فعلی
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # تلاش برای خواندن فایل اکسل موجود
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        # اگر فایل وجود ندارد، یک DataFrame جدید ایجاد کنید
        df = pd.DataFrame(columns=["--------TIME--------","Input"])
    
    # ایجاد یک DataFrame جدید با ورودی کاربر
    new_data = pd.DataFrame([{"--------TIME--------": current_time ,"Input": user_input}])
    
    # اضافه کردن ورودی جدید به DataFrame با استفاده از concat
    df = pd.concat([df, new_data], ignore_index=True)
    
    # ذخیره DataFrame به‌روز شده در فایل اکسل
    df.to_excel(file_path, index=False)
    
filename = os.path.join(dirname, "ex.xlsx")
# فراخوانی تابع برای ذخیره ورودی در "user_inputs.xlsx"
save_input_to_excel(filename)

# پیام موفقیت
print("ورودی شما با موفقیت در user_inputs.xlsx ذخیره شد")
