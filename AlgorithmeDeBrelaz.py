
def MatBool(n): #Beaucoups de verification car cette fonction sera utilisé par l'utilisateur

        n=int(n)
        print("vous allez devoir saisir les ",n," lignes de votre matrice une par une comme cela 1,0,1,0,1,1 par exemple.\n")
        matrice=[]
        for i in range(n):      #saisie de la matrice
                print("saisir la ligne n ",i+1)
                ligne=input(" : ")
                matrice.append(ligne.split(","))
                if(len(matrice[i])>n):  #verification de la taille de la ligne
                        print("la longeur de la ligne que vous avez saisie est trop longue elle va être reduite en supprimant les derniers nombres saisie")
                        matrice[i]=matrice[i][:n]
                        print("ligne après reduction : ",matrice[i],"\n")
                elif(len(matrice[i])<n):
                        print("la longeur de la ligne que vous avez saisie n'est pas assez longue elle va être rallongée en ajoutant des 0")
                        while (len(matrice[i])<n):
                                matrice[i].append(0)
                        print("ligne après allongement : ",matrice[i],"\n\n")
                for j in range(n):      #cast en int et correction de mauvaise saisie
                        if (matrice[i][j]==""or j==i):
                                matrice[i][j]="0"
                        try:    #verification que c'est bien un nombre   
                                matrice[i][j]=int(matrice[i][j])
                        except ValueError:
                                print("un caractère incunnue a été detecté il va etre remplacé par un 0\n")
                                matrice[i][j]=int(0)
                        if (matrice[i][j]>1):   #verifier que ce n'est pas superrieur à 1
                                matrice[i][j]=1
                                print("un nombre supérieur à 1 a été detecté il va être remplacé par un 1\n")
                print("ligne après correction primaire :",matrice[i],"\n\n")
        for i in range(n):      #correction mathematique pour avoir une matrice booléenne non orienté
                for j in range(n):
                        if (matrice[i][j]!=matrice[j][i]):
                                if (matrice[i][j]==1):
                                        matrice[j][i]=int(1)
                                else:
                                        matrice[i][j]=int(1)
        print("votre matrice de dimentions ",n," est la suivante :\n\n")
        for i in matrice:
                print(i,"\n")
        print("\n\n\n\n")
        return matrice


def Deg(mat):   #peu de verification car l'utilisateur n'aura pas accès à cette fonction

        degres=[]
        n=int(0)
        for i in mat:#voyager dans les lignes
                degres.append(0)
                for j in i:#voyager dans les collones
                        if (j==1):
                                degres[n]+=1
                n+=1
        return degres

def InitBrelaz(mat) :   #peu de verification car l'utilisateur n'aura pas accès à cette fonction
	
        sommetd=[]
        degres=Deg(mat)
        for i in range(len(degres)):
                position=0
                for j in range(len(degres)):
                        if(j not in sommetd and degres[position]==degres[j] and position>j):
                                position = j
                        elif(j not in sommetd and degres[position]<degres[j]):
                                position=j
                        elif(j not in sommetd and degres[position]==degres[j] and len(sommetd)==len(degres)-1):
                                position=j
                        elif(position in sommetd and position < len(degres)):
                                position+=1
                sommetd.append(position)
        
        return sommetd      
def InitBrelaz2(mat):    #peu de verification car l'utilisateur n'aura pas accès à cette fonction

        degres=Deg(mat)[:]
        degresIndex=[]
        for i in range(len(degres)):
                degresIndex.append([degres[i],i])
        for i in range(len(degres)):
                for j in range(i,len(degresIndex)):
                        if (degresIndex[i][0]<degresIndex[j][0]):
                                a=degresIndex[i]
                                degresIndex[i]=degresIndex[j]
                                degresIndex[j]=a
        for i in range(len(degres)):
                degres[i]=degresIndex[i][1]
        return(degres)


def lien(mat,index):          #peu de verification car l'utilisateur n'aura pas accès à cette fonction

        if (index < len(mat) and index >=0):
                lien=[]
                for i in range (len(mat)):
                        if (mat[index][i]==1):
                                lien.append(i)
                return lien
        else:
                print ("ERREUR : l'index entré est invalide")


def colorier(mat,index,sommetcol,coul,brelaz):
        memecoul=False
        colMax=0
        liee=lien(mat,index)
        for i in coul:
                if (i>colMax):
                        colMax=i 
        for i in sommetcol:
                memecoul=False
                if (i not in liee):
                        for j in liee:
                                if(coul[brelaz[0].index(i)]==coul[brelaz[0].index(j)]) :
                                        memecoul=True
                        if(not memecoul):
                                return coul[brelaz[0].index(i)]
        return colMax+1
                


def Brelaz(mat):       #peu de verification car l'utilisateur n'aura pas accès à cette fonction

        degres=Deg(mat)
        sommetDec=InitBrelaz(mat)
        brelaz=[]
        X={}
        coul=[]
        sommetcol=[]
        for i in range(len(mat)):
                coul.append(int(0))
        brelaz.append(sommetDec)
        brelaz.append([])
        for i in range(len(sommetDec)):
                brelaz[1].append(degres[sommetDec[i]])
        
        for i in range(1,len(sommetDec)):
                gDegres=0
                brelaz.append(brelaz[i][:])
                for j in range(1,len(sommetDec)):
                        try:
                                int(brelaz[i][gDegres])
                                if (j not in sommetcol and brelaz[i][gDegres]<brelaz[i][j] ):
                                        gDegres=j
                                        
                        except TypeError:
                                if (brelaz[i][gDegres]=="*"):
                                        gDegres+=1
                        except ValueError:
                                gDegres+=1
                        
                                        
                coul[gDegres]=colorier(mat,brelaz[0][gDegres],sommetcol,coul,brelaz)
                sommetcol.append(brelaz[0][gDegres])
                liee=lien(mat,brelaz[0][gDegres])
                for j in range(len(sommetDec)):
                        if (j != gDegres and brelaz[0][j] in liee and brelaz[0][j] not in sommetcol):
                                try:
                                        if (brelaz[i+1][j]==brelaz[1][j]):
                                                brelaz[i+1][j]=1
                                        else:
                                                brelaz[i+1][j]+=1
                                except TypeError:
                                        print (brelaz[i+1][j])
                        elif(j==gDegres):
                                brelaz[i+1][gDegres]="*"
        for i in coul:
                if (i==0):
                        j=coul.index(i)
                        coul[j]=colorier(mat,brelaz[0][j],sommetcol,coul,brelaz)
                        sommetcol.append(j)
        X["tab"]=brelaz
        X["coul"]=coul
        return X

def AffBrelaz(X):       #peu de verification car l'utilisateur n'aura pas accès à cette fonction

        print ("voici le tabelau resultant de l'algorithme de Brelaz \"*\" signifie que le sommet a été colorié la derniere ligne correspond aux couleurs : \n\n\n")
        for i in range(len(X.get("tab"))):
                if (i==0):
                        print("sommets   :\t",X["tab"][i])
                else:
                        print("DSAT(x)",i,":\t",X["tab"][i])
        print("couleurs  :\t",X["coul"])
                




#main

n=input("saisir la taille de la matrice : ")
erreur = False
try:
        n = int(n)
except ValueError :
        erreur = True

while erreur == True or n < 2 :
        if (erreur == False and n < 2) :
                n=input("ERREUR : la taille de la matrice saisie n'est pas assez grande veuillez saisir la taille de nouveau :")
                        
        try :
                erreur = False
                n=int(n)
        except ValueError :
                erreur = True
                n=input("ERREUR : la valeur saisie n'est pas numerique veuillez saisir la taille de nouveau :")
                
mat=MatBool(n)              
AffBrelaz(Brelaz(mat))
