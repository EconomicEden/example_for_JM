import pyautogui
import time
import subprocess

# 1. 텔레그램 데스크탑 실행
telegram_path = "C:\\Path\\To\\Telegram\\Telegram.exe"  # 텔레그램 실행 파일 경로
subprocess.Popen(telegram_path)  # 텔레그램 실행
time.sleep(5)  # 앱 로딩 대기

# 2. 로그인 단계
# 2.1 전화번호 필드 탐지 및 입력
phone_field = pyautogui.locateOnScreen('phone_field.png', confidence=0.8)
if phone_field:
    pyautogui.click(phone_field)
    pyautogui.write('01012345678')  # 전화번호 입력
    pyautogui.press('enter')
    time.sleep(3)
else:
    print("전화번호 입력 필드를 찾을 수 없습니다!")

# 2.2 인증코드 필드 탐지 및 입력
code_field = pyautogui.locateOnScreen('code_field.png', confidence=0.8)
if code_field:
    pyautogui.click(code_field)
    pyautogui.write('123456')  # 인증코드 입력
    pyautogui.press('enter')
    time.sleep(3)
else:
    print("인증코드 입력 필드를 찾을 수 없습니다!")

# 3. 프리미엄 계정 신청 단계
# 3.1 "프리미엄" 버튼 클릭
premium_button = pyautogui.locateOnScreen('premium_button.png', confidence=0.8)
if premium_button:
    pyautogui.click(premium_button)
    time.sleep(3)
else:
    print("프리미엄 버튼을 찾을 수 없습니다!")

# 3.2 카드 정보 입력
# 카드번호 필드
card_number_field = pyautogui.locateOnScreen('card_field.png', confidence=0.8)
if card_number_field:
    pyautogui.click(card_number_field)
    pyautogui.write('4111111111111111')  # 카드번호 입력
else:
    print("카드번호 입력 필드를 찾을 수 없습니다!")

# 유효기간 필드
expiry_date_field = pyautogui.locateOnScreen('expiry_field.png', confidence=0.8)
if expiry_date_field:
    pyautogui.click(expiry_date_field)
    pyautogui.write('12/30')  # 유효기간 입력
else:
    print("유효기간 입력 필드를 찾을 수 없습니다!")

# 보안코드 필드
cvv_field = pyautogui.locateOnScreen('cvv_field.png', confidence=0.8)
if cvv_field:
    pyautogui.click(cvv_field)
    pyautogui.write('123')  # 보안코드 입력
else:
    print("보안코드 입력 필드를 찾을 수 없습니다!")

# 3.3 결제 버튼 클릭
pay_button = pyautogui.locateOnScreen('pay_button.png', confidence=0.8)
if pay_button:
    pyautogui.click(pay_button)
    print("프리미엄 신청 완료!")
else:
    print("결제 버튼을 찾을 수 없습니다!")
