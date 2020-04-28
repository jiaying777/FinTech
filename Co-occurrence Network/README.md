# Co-occurrence Network

資料來源：[Fugle](https://www.fugle.tw)\
資料名稱：[0410~0416客戶瀏覽卡片資料](https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/data.zip)
（因資料使用權限問題，在此僅附上已經處理過的資料）

## 觀察資料
* 拿到資料後發現**同一個用戶**瀏覽不同股票所觀看的卡片皆相同，由於卡片版面為使用者自行設定，因此可能會因人而異，但同一個人觀看的卡片卻沒什麼差異，所以卡片只能代表這個使用者習慣看哪些資訊，因此把此卡片放在版面中，但我們無法從此資料中得知使用者到底有沒有看這張卡片。
<br>

* 所以無法從觀看哪種類型的卡片下手做分析，因此決定分析使用者看了Ａ也會看什麼？

  👉  意即有一群人看了Ａ股票後，也會看Ｂ股票。\
  📌  找出各股之間的共現關係。
  
## 整理資料＆建立共現矩陣

只顯示共現矩陣前5列：

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/共現矩陣1.png'>

得到的共現矩陣為稀疏矩陣。

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/co_sym.png'>

👆畫出股票間的熱點圖，發現彼此之間的共現頻率不高❗️

  
  🧐可能原因：
  
    資料量不足造成稀疏矩陣，因此畫出來的熱點圖共現頻率也很低。
  
  💡解決辦法：
  
    增加資料量(瀏覽資料的時間區間加長)，資料變多可以使各股共現次次數提高，藉此可以更準確地分析。
  
