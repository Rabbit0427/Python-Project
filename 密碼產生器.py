# -
產生一個包含大小寫字母、標點符號、數字至少各一的密碼產生器
[github密碼產生器.py](https://github.com/user-attachments/files/23850931/github.py)
import string
import random

def generate_strong_password(length=12):

    lowercase = string.ascii_lowercase

    uppercase = string.ascii_uppercase

    digits = string.digits

    punctuation = string.punctuation

    password_list = []

    password_list.append(random.choice(lowercase))

    password_list.append(random.choice(uppercase))

    password_list.append(random.choice(digits))

    password_list.append(random.choice(punctuation))

    all_characters = lowercase + uppercase + digits + punctuation

    if length > 4:
        for i in range(length):
            random_char = random.choice(all_characters)
            password_list.append(random_char)
    
    random.shuffle(password_list)

    return "".join(password_list)

pw1 = generate_strong_password(length=16)
print(f"密碼 1: {pw1}")
pw2 = generate_strong_password(length=8)
print(f"密碼 2: {pw2}")
pw3 = generate_strong_password(length=4)
print(f"密碼 3: {pw3}")
