<<<<<<< HEAD
# wintoast 쓰니깐 되다가 안되다가 넘 심해서 그냥 웹여는걸로 함
import webbrowser

# 웹사이트 만든곳으로 이동
page_url = 'http://example.com/' 

def open_url():
    try:
        webbrowser.open_new(page_url)
    except:
        print('Failed to open URL. Unsupported variable type.')
        
def d_alert():
    open_url()

=======
# wintoast 쓰니깐 되다가 안되다가 넘 심해서 그냥 웹여는걸로 함
import webbrowser

# 웹사이트 만든곳으로 이동
page_url = 'http://example.com/' 

def open_url():
    try: 
        webbrowser.open_new(page_url)
    except: 
        print('Failed to open URL. Unsupported variable type.')
        
def d_alert():
    open_url()

>>>>>>> 802554d90f9aa68f63f58425fc10c040e174b89e
    