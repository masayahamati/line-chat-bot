import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file=open(r'C:\python\line\info.json','r')
info=json.load(file)
CHANNEL_ACCESS_TOKEN=info["CHANNEL_ACCESS_TOKEN"]#このチャンネルに贈ることの許可のこと
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID=info["USER_ID"]
    messages=TextSendMessage(text="おはよう")#送るメッセージを指定できる
    line_bot_api.push_message(USER_ID,messages=messages)#インスタンス化したline_bot_apiの関数をよびだしている。引数はどのユーザーに贈るかということとどのメッセージを送るかということ

if __name__=="__main__":
    main() 