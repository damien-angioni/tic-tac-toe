H1=" "
H2=" "
H3=" "
M1=" "
M2=" "
M3=" "
B1=" "
B2=" "
B3=" "
Player1="X"
Player2="O"
Game_Over=0
process=0
parité=0
placement=0
print("Pour placer votre marque, vous suivrez cette logique là pour la grille:")
print("7|8|9")
print("4|5|6")
print("1|2|3")
print("Le joueur 1 commence et est remrésenté par une X tandis que le joueur 2 est second et représenté par un O:")
while(Game_Over<1):
    if(H1==H2==H3==Player1)or(H1==M2==B3==Player1)or(H1==M1==B1==Player1)or(H2==M2==B2==Player1)or(H3==M2==B1==Player1)or(H3==M3==B3==Player1)or(M1==M2==M3==Player1)or(B1==B2==B3==Player1):
        print("Joueur 1 a gagné! du coup t'es nul joueur 2!")
        Game_Over=1
    elif(H1==H2==H3==Player2)or(H1==M2==B3==Player2)or(H1==M1==B1==Player2)or(H2==M2==B2==Player2)or(H3==M2==B1==Player2)or(H3==M3==B3==Player2)or(M1==M2==M3==Player2)or(B1==B2==B3==Player2):
        print("Joueur 2 a gagné! du coup t'es nul joueur 1!")
        Game_Over=1
    elif(H1!=" ")and(H2!=" ")and(H3!=" ")and(M1!=" ")and(M2!=" ")and(M3!=" ")and(B1!=" ")and(B2!=" ")and(B3!=" "):
        print("Draw!")
        Game_Over=1
    else:
        while(process==0):
            if(parité==0):
                print("tour du joueur 1:")
                placement=input("Choisissez votre emplacement:")
                if(placement=="1"):
                    if(B1==" "):
                        B1=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="2"):
                    if(B2==" "):
                        B2=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="3"):
                    if(B3==" "):
                        B3=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")                
                elif(placement=="4"):
                    if(M1==" "):
                        M1=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="5"):
                    if(M2==" "):
                        M2=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="6"):
                    if(M3==" "):
                        M3=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="7"):
                    if(H1==" "):
                        H1=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="8"):
                    if(H2==" "):
                        H2=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="9"):
                    if(H3==" "):
                        H3=Player1
                        parité=1
                        process=1
                    else:
                        print("Emplacement occupé")
                else:
                    print("emplacement invalide")
            elif(parité==1):
                print("tour du joueur 2:")
                placement=input("Choisissez votre emplacement:")
                if(placement==1):
                    if(B1==" "):
                        B1=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="2"):
                    if(B2==" "):
                        B2=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="3"):
                    if(B3==" "):
                        B3=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")                
                elif(placement=="4"):
                    if(M1==" "):
                        M1=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="5"):
                    if(M2==" "):
                        M2=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="6"):
                    if(M3==" "):
                        M3=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="7"):
                    if(H1==" "):
                        H1=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="8"):
                    if(H2==" "):
                        H2=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                elif(placement=="9"):
                    if(H3==" "):
                        H3=Player2
                        parité=0
                        process=1
                    else:
                        print("Emplacement occupé")
                else:
                    print("emplacement invalide")
        process=0
        print(H1+"|"+H2+"|"+H3)
        print(M1+"|"+M2+"|"+M3)
        print(B1+"|"+B2+"|"+B3)