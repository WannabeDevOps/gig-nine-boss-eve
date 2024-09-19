#น้องโต๋ย
import random

def get_random_boyfriend():
    menu = [
        "อลัน", 
        "มาร์คคริส", 
        "ขุนพล", 
        "ฮาร์ท", 
        "โก๋ยโต๋ย", 
        "ไทย", 
        "คอปเปอร์", 
        "ภีม", 
        "จินจุค", 
        "จั๋ง",
        "เอเอ",
        "nex"

    ]
    
    return random.choice(menu)

# เรียกใช้ฟังก์ชันเพื่อสุ่มเมนูอาหาร
today_menu = get_random_boyfriend()
print(f"วันนี้มีแฟนชื่ออะไรดี: {today_menu}")
