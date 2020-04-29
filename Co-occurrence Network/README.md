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

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/co_sym.png' width=80%>

👆畫出股票間的熱點圖，發現彼此之間的共現頻率不高❗️

  
  🧐可能原因：
  
    資料量不足造成稀疏矩陣，因此畫出來的熱點圖共現頻率也很低。
  
  💡解決辦法：
  
    增加資料量(瀏覽資料的時間區間加長)，資料變多可以使各股共現次次數提高，藉此可以更準確地分析。
    
## 共現圖
<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/Co-occurrence%20map.png' width=80%>
<br>

👆 資料量過多，因此需要篩選資料，不然從圖看不出什麼資訊。
<br>

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/統計次數.png' width=50%>

由統計圖看出，0410~0416這段期間2330台積電為最多人瀏覽的股票，因此選擇2330台積電來做進一步的分析。🚗
<br>

### 2330台積電與所有共現股票之共線圖

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/2330_Co-occurrence%20map.png'>

📌距離為共現機率，節點大小為被瀏覽的總人次。
👉 由於很多股票跟2330台積電的共現次數都不高，所以篩選共現頻率較高的再畫一次共現圖

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/2330_Co_map.png'>

📌距離為共現機率，節點大小為被瀏覽的總人次。<br>
👉 由上圖可以看出看2330台積電的人也有機率會看0050、0056、2884、2317、2337等等股票。<br>
👉 其中0050、0056為ETF，而2884玉山金為Fugle合作夥伴，因此玉山金的瀏覽次數與共現頻率可能不是那麼準確。
<br>

## 抓取股票特徵再分析

📌抓取特定指標，找出看完2330台積電後可能會瀏覽的股票之間的關係（沒有ETF的部分，因為ETF沒有本益比。指標選擇根據專題小組共同決定而來。）

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/共現矩陣2.png'>
<br>

#### 建立共現矩陣
<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/共現矩陣3.png'>
<br>

### 熱點圖
<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/0416_2330_co_sym.png'>
👆 從熱點圖可以看出各特徵之間共現的關係
<br>

### 共現圖
<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/0416_2330_Co_map.png'>
👆由上圖可知瀏覽2330台積電的這群用戶可能會瀏覽的股票之特徵為：(只標共現次數其實都很相近，同指標取其高且相近者)

   * 股價位於0~50
   * 殖利率1~5
   * 股價淨值比>1
   * 本益比12~20
   * Beta係數>1
<br>

## 回去找出這群使用者 👫
<br>

🔍 找出“使用者瀏覽股票清單”和“看2330台積電後可能會看的股票清單”相似程度**高達8成**的使用者

<img src='https://github.com/jiaying777/FinTech/blob/master/Co-occurrence%20Network/相似使用者.png' width=80%>
<br>

#### 將使用者分群再推播

📍 找出這些相似的使用者，將使用者做分群，就能夠更準確地進行推播。<br>
🚗 再來我們可以將相似**高達8成**的使用者也觀看或追蹤的股票推薦給其他相似的使用者。








