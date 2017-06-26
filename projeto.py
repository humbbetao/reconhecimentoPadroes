from sklearn import tree
import numpy as np 
import itertools

def voto(dictionary):
	oMaior = 0.0
	for key, val in dictionary.items():

		if val > oMaior :
			oMaior = key

	return oMaior


if __name__ == "__main__": 
	
	zoo=np.genfromtxt('zoo.csv', delimiter=',' ,
 		 dtype={
 		 'names':['animalName','hair','feathers','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venomous','fins','legs','tail','domestic','catsize','classType'],
 		 'formats': [ '|S15',np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float,np.float ]})


	# print(zoo)

	# feature = zoo[0:15]
	# target = zoo[0:102]

	# print(zoo[0])
	feature=[]
	for i in range(0,102):
		if i>0:
			feature.append([])
			for j in range(0,17):
				if j>0:
					feature[i-1].append(zoo[i][j])

	# print("Feature")
	# for i in range(0,101):
		# print(feature[i])
	
	target =[]
	for i in range(0,102) :
		if i>0:
			target.append(zoo[i][17])




	# teste
	# target = zoo[0:102][17]
	# print("Target")
	# print(target)

	# print(len(feature))
	# print(len(target))

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(feature,target)

	predict = clf.predict(feature)
	
	# predict_proba = clf.predict_proba(target)

	acuracia = clf.score(feature, target) *100
	print("acuracia: ", acuracia)






	# # print(feature)
	# print(zoo[0,1])


	# for linha in zoo.readlines():      # percorre cada linha do arquivo
	# 	dados = linha.split(",")
	# 	zooMatriz.append(dados)	    
	# zoo.close()

	# print(zooMatriz)

	# classification = open("class.csv","r")

	# classificationMatriz=[]
	# for linha in classification.readlines():      # percorre cada linha do arquivo
	# 	dados = linha.split(",")
	# 	classificationMatriz.append(dados)	    
	# classification.close()

	# print(classificationMatriz)

	# # linhasMatriz = len(zooMatriz)
	# # colunasMatriz = len(zooMatriz[0])


	# # # print(linhasMatriz)
	# # # print(colunasMatriz)


	# feature = zooMatriz[:,1:19]
	# target = zooMatriz[:,19]


	# # clf = tree.DecisionTreeClassifier()

	# # clf = clf.fit(feature,target)

	# # predict = clf.predict(feature)
	# # predict_proba = clf.predict_proba(target)

	# # k =0.0
	# # # print(predict)

	# # acuracia = clf.score(base3[:,0:58], base3[:,59]) *100


	# # # for i in range(1,colunasMatriz) :
	# # # 	for j in range(1,linhasMatriz) :
	# # # 		print(list(itertools.permutations(zooMatriz[j], i)))
