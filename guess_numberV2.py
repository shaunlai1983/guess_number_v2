import random   #匯入標準的模組random
r = random.randint(1 , 100) #取用random模組內的randint功能.範圍1 -100
                            #random + int的意思為隨機的整數的意思
                            #從這邊就產生了一個r在這個世界上
count = 0
while True:                 #進入while 並且不斷重複
	num = input('猜猜看數字 1 - 100:')
	num = int(num)    #將input的字串型別轉換為整數
	if num == r:
		count = count + 1
		print('終於猜對了','這是你猜得第' ,count ,'次')	
		break          #印出後從這邊斷掉While迴圈
	elif num > r:
		count = count + 1
		print('你猜得比較大喔')
	elif num < r:
		count = count + 1
		print('你猜得比較小喔')
	print('這是你猜得第' ,count ,'次')  #放在elif架構之外,減少行數