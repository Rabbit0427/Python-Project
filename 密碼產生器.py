# -
產生一個包含大小寫字母、標點符號、數字至少各一的密碼產生器
[github密碼產生器.py](https://github.com/user-attachments/files/23850931/github.py)
import sys
import random
import string

def generate_strong_password(length=12):
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    punctuation = string.punctuation

    password_list = []
    password_list.append(random.choice(string.digits))
    password_list.append(random.choice(string.ascii_lowercase))
    password_list.append(random.choice(string.ascii_uppercase))
    password_list.append(random.choice(string.punctuation))

    all_characters = lowercase + uppercase + digits + punctuation

    if length > 4:
        for i in range(length - 4):
            random_char = random.choice(all_characters)
            password_list.append(random_char)

    random.shuffle(password_list)
    return "".join(password_list)


length_input = input("請輸入密碼長度:")
try:
    password = int(length_input)
    if password < 4:
        print(f"輸入的長度{password}太短了。至少需要 4 位才能保證包含所有類型字元。")
        sys.exit()
    elif password >=4:
        final_password = generate_strong_password(length=password)
        print(f"生成的強力密碼(長度:{password}) / 密碼為:{final_password}")

except ValueError:
    print("請輸入一個有效的數字。")
