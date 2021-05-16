import random   #匯入標準的模組random
start = input('輸入開始值')
end = input('輸入結束值')
start = int(start)
end = int(end)
r = random.randint(start, end) #取用start,end變數.用在randint的定義範圍內
count = 0                   #變數來計算輸入次數
while True:                 #進入while 並且不斷重複
	num = input('猜猜看數字:')
	num = int(num)    #將input的字串型別轉換為整數
	if num == r:
		count += 1  #count = count + 1 的快寫法
		print('終於猜對了', '這是你猜得第', count, '次')	
		break          #印出後從這邊斷掉While迴圈
	elif num > r:
		count = count + 1
		print('你猜得比較大喔')
	elif num < r:
		count = count + 1
		print('你猜得比較小喔')
	print('這是你猜得第', count, '次')  #放在elif架構之外,減少行數