# modules
import webbrowser
from win10toast_click import ToastNotifier 

# 웹사이트 만든곳으로 이동
page_url = 'http://example.com/' 

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')
        
def d_alert():
    # initialize 
    toaster = ToastNotifier()

    # showcase
    toaster.show_toast(
        "현재 사이트에서 악성 스크립트가 탐지됨", # title
        "(자세한 내용)클릭 >>", # message 
        icon_path=None, # 아이콘 경로 
        duration=5, # 위치
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
        callback_on_click=open_url # click notification to run function 
        )