import requests, os, sys
from sys import platform
from time import sleep

# ANSI màu
den = '\033[1;90m'
luc = '\033[1;32m'
trang = '\033[1;37m'
red = '\033[1;31m'
vang = '\033[1;33m'
tim = '\033[1;35m'
lamd = '\033[1;34m'
lam = '\033[1;36m'
hong = '\033[1;95m'
do = red
xnhac = lam

thanh_xau = trang + '~' + red + '[' + vang + 'C25' + red + '] ' + trang + '➩ ' + luc

# pystyle banner
try:
    from pystyle import Colorate, Colors
except:
    os.system("pip install pystyle")
    from pystyle import Colorate, Colors

banners = f"""
╔═════════════════════════════════════════════════════════════════           
 ██████╗██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝╚════██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║      █████╔╝███████╗       ██║   ██║   ██║██║   ██║██║     
██║     ██╔═══╝ ╚════██║       ██║   ██║   ██║██║   ██║██║     
╚██████╗███████╗███████║       ██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
╠═════════════════════════════════════════════════════════════════
║➢ Admin      : Vũ Văn Chiến                                   
║➢ Youtube    : https://www.youtube.com/@c25tool                  
║➣ Nhóm Bot Zalo :  https://zalo.me/g/elcygl942              
║➣ Website    :  c25tool.net            
╚═════════════════════════════════════════════════════════════════
"""
thongtin = """
Vượt Link Để lấy Key Free Hoặc Mua Key Vip Tại Web: C25TOOL.NET
Lưu ý :(key free đổi theo ip máy nên lần sau vào tool không thay wifi nhé)
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_green, banners))
    print(thongtin)

# Link github raw cho từng tool
link_map = {
    "1.1": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/1/1.1.py",
    "1.2": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/1/1.2.py",
    "1.3": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/1/1.3.py",
    "1.4": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/1/1.4.py",
    "1.5": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/1/1.5.py",
    "2.1": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.1.py",
    "2.2": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.2.py",
    "2.3": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.3.py",
    "2.4": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.4.py",
    "2.5": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.5.py",
    "2.6": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/2/2.6.py",
    "3.1": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.1.py",
    "3.2": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.2.py",
    "3.3": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.3.py",
    "3.4": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.4.py",
    "3.5": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.5.py",
    "3.6": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.6.py",
    "3.7": "https://raw.githubusercontent.com/Minhtien1234/C25Source/refs/heads/main/3/3.7.py",
}

# Giao diện menu
banner()
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Cày Cuốc  {vang}     ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛ """)
print(f'{thanh_xau}Nhập [1.1] Tool Cày Xu TDS Tiktok')
print(f'{thanh_xau}Nhập [1.2] Tool Cày Xu TDS Instagram')
print(f'{thanh_xau}Nhập [1.3] Tool Golike TikTok [ADR]')
print(f'{thanh_xau}Nhập [1.4] Tool Golike Instagram')
print(f'{thanh_xau}Nhập [1.5] Tool Cày Xu TDS Facebook')

print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃  {vang}Tool Profile         {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}Nhập [2.1] Tool Buff Share Ảo Cookie')
print(f'{thanh_xau}Nhập [2.2] Tool Get Token Facebook 16 Loại')
print(f'{thanh_xau}Nhập [2.3] Tool Lấy ID Bài Viết, ID Facebook')
print(f'{thanh_xau}Nhập [2.4] Tool CMT Bài Viết Dạo Facebook [bảo trì]')
print(f'{thanh_xau}Nhập [2.5] Tool Get Cookie Facebook Bằng TK MK')
print(f'{thanh_xau}Nhập [2.6] Tool Spam Tin Nhắn, War Messenger')

print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃   {vang}Tool Tiện Ích       {vang}┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}Nhập [3.1] Tool Doss Web + Doss IP')
print(f'{thanh_xau}Nhập [3.2] Tool Get Proxy')
print(f'{thanh_xau}Nhập [3.3] Tool Lọc Proxy')
print(f'{thanh_xau}Nhập [3.4] Tool Scan Mail Ảo Lấy Mã')
print(f'{thanh_xau}Nhập [3.5] Tool Spam SĐT')
print(f'{thanh_xau}Nhập [3.6] Tool Buff Tiktok [PC]')
print(f'{thanh_xau}Nhập [3.7] Tool Reg Nick FB')
print(f'{lam}────────────────────────────────────────────────────────')

chon = input(f'{thanh_xau}{do}Nhập Số: {vang}').strip()

# Chạy tool từ github mà không in link
if chon in link_map:
    try:
        code = requests.get(link_map[chon]).text
        exec(code, globals())
    except Exception as e:
        print(f"{do}Lỗi khi chạy tool {chon}: {e}")
else:
    print(f"{do}Lựa chọn không hợp lệ hoặc chưa hỗ trợ.")
