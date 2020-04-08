import requests
import configparser
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from fugle_realtime import intraday

config = configparser.ConfigParser()
config.read('config.ini')
access_token = config['TELEGRAM']['ACCESS_TOKEN']
webhook_url = config['TELEGRAM']['WEBHOOK_URL']
api_token = config['TELEGRAM']['api_token']

requests.post('https://api.telegram.org/bot'+'1072022422:AAFwoUUbuTNN3LeHI2tgLvOCPuxgpJHTFTk'
+'/deleteWebhook').text

requests.post('https://api.telegram.org/bot'+access_token+'/setWebhook?url='+webhook_url+'/hook').text


# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=config['TELEGRAM']['ACCESS_TOKEN'])

@app.route('/hook', methods=['POST'])    
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'
    
def start(bot, update):
    bot.send_message(update.message.chat.id, '{} 您好，請輸入欲查詢的股票代碼：'.format(update.message.from_user.first_name))
    
def info(bot, update):
    global num
    num = update.message.text
    data = intraday.meta(apiToken=api_token , symbolId=num ,output='raw')
    
    if 'error' in data:
        update.message.reply_text('請輸入正確的股票代碼：')
        return
    if 'industryZhTw' in data:
        text = ('產業別：'+data['industryZhTw']+'\n'+'交易幣別：'+data['currency']+'\n'+'股票中文簡稱：'+data['nameZhTw']+'\n'+'開盤參考價：'+ str(data['priceReference'])+'\n'+
            '漲停價：'+str(data[ 'priceHighLimit'])+'\n'+'跌停價：'+str(data["priceLowLimit"])+'\n'+'股票類別：'+data['typeZhTw'])
    else:
        text = ('交易幣別：'+data['currency']+'\n'+'股票中文簡稱：'+data['nameZhTw']+'\n'+'開盤參考價：'+ str(data['priceReference'])+'\n'+
            '漲停價：'+str(data[ 'priceHighLimit'])+'\n'+'跌停價：'+str(data["priceLowLimit"])+'\n'+'股票類別：'+data['typeZhTw'])
    global reply_markup
    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('即時股價', callback_data='now_price'),
        InlineKeyboardButton('最新一筆交易', callback_data='trade'),InlineKeyboardButton('最佳五檔', callback_data='five')]])
    
    update.message.reply_text(text)

    if update.message:
         bot.send_message(update.message.chat.id, '{} 您好，有什麼我可以幫忙的？'.format(update.message.from_user.first_name) 
                     , reply_to_message_id = update.message.message_id,reply_markup = reply_markup)
            
            


def getClickButtonData(bot, update):

    if update.callback_query.data == 'now_price':
        df1 = intraday.chart(apiToken=api_token , symbolId=num)
        df1 = df1.iloc[-1]
        text = ('●股票代碼：'+num+'\n'+'此分鐘開盤價：'+str(df1["open"])+'\n'+'此分鐘最高價：'+str(df1['high'])+'\n'+'此分鐘最低價：'+str(df1['low'])+'\n'+'此分鐘收盤價：'
                +str(df1['close'])+'\n'+'此分鐘交易張數：'+str(df1['unit'])+'\n'+'此分鐘交易量：'+str(df1['volume']))
       
        update.callback_query.message.reply_text(text,reply_markup = reply_markup)
       

        

    if update.callback_query.data == 'trade':
        df2 = intraday.quote(apiToken=api_token,symbolId=num,output='raw')
        df3 = df2['trade']
        text = ('●'+num+'最新一筆交易：'+'\n'+'成交價：'+str(df3['price'])+'\n'+'成交張數：'+str(df3['unit'])+'\n'+'成交量：'+str(df3['volume'])+'\n'+
                                                                                                     '成交序號：'+str(df3['serial']))
        update.callback_query.message.reply_text(text,reply_markup = reply_markup)
        
    if update.callback_query.data == 'five':
        df4 = intraday.quote(apiToken=api_token,symbolId=num,output='raw')
        df4 = df4['order']
        text1 = ('●'+num+'最佳五檔買價：'+'\n'
                +'價格：'+str(df4['bestBids'][0]['price'])+'\n'+'張數：'+str(df4['bestBids'][0]['unit'])+'\n'+'交易量：'+str(df4['bestBids'][0]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestBids'][1]['price'])+'\n'+'張數：'+str(df4['bestBids'][1]['unit'])+'\n'+'交易量：'+str(df4['bestBids'][1]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestBids'][2]['price'])+'\n'+'張數：'+str(df4['bestBids'][2]['unit'])+'\n'+'交易量：'+str(df4['bestBids'][2]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestBids'][3]['price'])+'\n'+'張數：'+str(df4['bestBids'][3]['unit'])+'\n'+'交易量：'+str(df4['bestBids'][3]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestBids'][4]['price'])+'\n'+'張數：'+str(df4['bestBids'][4]['unit'])+'\n'+'交易量：'+str(df4['bestBids'][4]['volume']))
        text2 = ('●'+num+'最佳五檔賣價：'+'\n'
                +'價格：'+str(df4['bestAsks'][0]['price'])+'\n'+'張數：'+str(df4['bestAsks'][0]['unit'])+'\n'+'交易量：'+str(df4['bestAsks'][0]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestAsks'][1]['price'])+'\n'+'張數：'+str(df4['bestAsks'][1]['unit'])+'\n'+'交易量：'+str(df4['bestAsks'][1]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestAsks'][2]['price'])+'\n'+'張數：'+str(df4['bestAsks'][2]['unit'])+'\n'+'交易量：'+str(df4['bestAsks'][2]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestAsks'][3]['price'])+'\n'+'張數：'+str(df4['bestAsks'][3]['unit'])+'\n'+'交易量：'+str(df4['bestAsks'][3]['volume'])+'\n'+'\n'
                +'價格：'+str(df4['bestAsks'][4]['price'])+'\n'+'張數：'+str(df4['bestAsks'][4]['unit'])+'\n'+'交易量：'+str(df4['bestAsks'][4]['volume']))
  
        update.callback_query.message.reply_text(text1)
        update.callback_query.message.reply_text(text2,reply_markup = reply_markup)




dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, info))
dispatcher.add_handler(CallbackQueryHandler(getClickButtonData))

if __name__ == '__main__':
    app.run()