import shutil
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np


book_name_control = True 
Found = True

print("Dil seçiniz - Chose language")
print("1-Türkçe Tr")
print("2-English En")
lan = int(input("Seçtiğiniz dilin rakamını giriniz - Enter the number of the language you selected: "))
if lan == 1 or lan == 2:
    encode = {}
    for fnames in os.walk("./res"): #This function is going to /res file and read inside file
        for f in fnames: # It is read res file in side
            encode = f #This is convert to string if we didn't chance it  we use to list structure. 
    
    
    if book_name_control == True: #all books print to console
        if lan == 1:
            print("> Tüm kitaplar aşağıda listelenmiştir.")
        if lan == 2:
            print("All books are listed below.")
        for en in encode:
            print(en)
    
    
    print("------------------------------------")   
    print()
    if lan == 1:
        print("!! Alacağınız kitabı alkit klasörüne ve yüzünüzü facetake klasörüne atınız.")
    if lan == 2:
        print("!!Put the book you will take in the alkyd folder and your face in the face take folder.")
    no_book = True
    fnames = {}
    while book_name_control: # True
        
        if lan == 1:  
            book_name = input("Almak istediğiniz kitabın adını giriniz= ")+".jpg" # Take a book name value 
        if lan == 2:
            book_name = input("Enter the name of the book you want to take= ")+".jpg" # Take a book name value 
        book_name = book_name.lower()# convert to all text small charecter
        
       
        for fnames in os.walk("./alkit"): #This function is going to /res file and read inside file
            for f in fnames: # It is read res file in side
                alkit_in = f #This is convert to string if we didn't chance it  we use to list structure. 
           
        if alkit_in == []:
            if lan == 1:
                print("> Klasör içeriği boş lütfen fotograf yükleyiniz.")
            if lan == 2:
                print("> Folder contents are empty, please upload photos.")
           
        for i in alkit_in: #convert to string
            if book_name != i:
                shutil.copy2('./alkit/'+i, "./alkit/"+book_name)
                """
                It is make it copy file because we will remove to file the featcure if we can not do this.
                program will be cros the files  
                """
                os.path.exists("./alkit/"+i)
                os.remove("./alkit/"+i)
            
        os.chdir('C:/Users/Ege/Desktop/nesne') # go to the this file path 
                
        
        
                
        for e in encode: # this function is read in encode list
            
            if book_name == e: # encode in filename compate to book name 
                
                
                while True:
                    camera = cv2.VideoCapture("alkit/"+book_name)                    
                    ret,kare = camera.read()
                    try:
                        grey_square = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)#convert to grey color
                        obje = cv2.imread("res/"+book_name,0)    
                        res = cv2.matchTemplate(grey_square,obje,cv2.TM_CCOEFF_NORMED)#compare .jpg file
                        face_reco = True
                        old_value = 0.8
                        loc = np.where(res>old_value)
            
        
                
                        for n in zip(*loc[::-1]):
                            # compare is true
                            if lan == 1:
                                print("> Kitap Bulundu !!! :D.")
                            if lan == 2:
                                print("> Book Found !!! :D.")
                            book_name_control = False
                            Found = False
                            break
                        break
                    except:
                        if lan == 1:
                            print("> Kitap eşleştirme işleminde bir hata oldu lütfen tekrar deneyiniz.")
                        if lan == 2:
                            print("> There was an error in the book matching process, please try again.")
                        break
                            
                    
                        
                    if Found == False:
                        break
                    os.path.exists("./alkit/"+book_name)
                no_book = False
                book_name = book_name.split(".jpg")
                if lan == 1:                   
                    print(">",book_name[0],"Kütüphanede bulunmaktadır.")
                if lan == 2:
                    print(">",book_name[0],"Available in the library.")
            if encode[-1] == e:
                while_çık = True
                break
        
        if book_name_control == True:  
            break
    
    if no_book == True:
        if lan == 1:
            print("> Kitap yok.")
        if lan == 2:
            print("> No book.")
    else:     
        # close the windows
        camera.release()
        cv2.destroyAllWindows()
    
    
    # If program does not find the search book. it will be not continue
        
        
        
    def get_encoded_faces(ad):
        encoded = {}
        f = ad
        for dirpath, dnames, fnames in os.walk("./faces"):
            for esit in fnames:
                if ad == esit:
                    face = fr.load_image_file("faces/"+f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding
                    yüz_var = True
        
        return encoded
    
    
    def classify_face(im,kad):
        
        faces = get_encoded_faces(kad)
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())
        
        img = cv2.imread(im, 1)
     
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    
        face_names = []
        for face_encoding in unknown_face_encodings:
            # if program is not find user,make user name unknown
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"
    
    
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
        
        if name != "Unknown":
                
            for x in face_names:
                if lan == 1:
                    print(">>",x,"kullanıcısına kitap verildi.")
                if lan == 2:
                    print(">>",x,"user received a book.")
            face_count = len(face_names)
            
            if face_count != 1:
                if lan == 1:
                    print("> !!! Yüz tanıma işleminde birden çok yüz bulundu.")
                if lan == 2:
                    print("> !!! Multiple faces found in face recognition.")
            else:
                print()
                if lan == 1:
                    print(">>> İşlem başarıyla tamamlandı !")
                if lan == 2:
                    print(">>> The transaction was successfully completed !")
        else:
            if lan == 1:
                print("Kişi tanımlanmadı.")
            if lan == 2:
                print("No contact identified.")
            
        
    if book_name_control == False:
        
        if lan == 1:
            user_face = input("Adınızı giriniz= ")+".jpg"
        if lan == 2:
            user_face = input("Enter your name= ")+".jpg"
        user_face = user_face.lower()
        
        face_tut = {}
        for fnames in os.walk("./facetake"): 
            for f in fnames: 
                face_tut = f 
        if face_tut == []:
            if lan == 1:
                print("> Klasör içeriği boş lütfen fotoğraf yükleyiniz.")
            if lan == 2:
                print("> Folder content is empty, please upload photos.")
                
        for i in face_tut:
            if user_face != i:
                shutil.copy2('./facetake/'+i, "./facetake/"+user_face)
                #isim random olduğundan onu biz girilen değer de isimini veriyoruz
                os.path.exists("./facetake/"+i)
                os.remove("./facetake/"+i)
    
        
        
            if Found == False:    
                if face_reco == True:
                    print("")
                    if lan == 1:
                        print("-----------YÜZ TANIMA------------")  
                        print("Yüz tanıma işlemi sonucu")
                    if lan == 2:
                        print("-----------FACE RECOGNITION------------")  
                        print("Face recognition result")
                        
                    try:
                        classify_face("./facetake/"+user_face,user_face)
                    except:
                        if lan == 1:
                            print("> İsminiz sistemde bulunmamaktadır.")
                        if lan == 2:
                            print("> Your name is not in the system.")
                    
                    
                    
                    
    # Deletes the contents of the file "facetake"
    for fnames in os.walk("./facetake"): 
        for f in fnames: 
            alkit_in = f 
        for i in alkit_in:
            os.path.exists("./facetake/"+i)
            os.remove("./facetake/"+i)
                   
                    
    # Deletes the contents of the file "alkit"
    for fnames in os.walk("./alkit"): 
        for f in fnames: 
            alkit_in = f 
        for i in alkit_in:
            os.path.exists("./alkit/"+i)
            os.remove("./alkit/"+i)
    
                    
    

    
    
    
    
    
else:
    print("Dil seçiminde hata oluştu - Language selection error")
    
print()
print()
print()
print(">#/>#/>#/>#/>#/>#/>#  BİTTİ   />#/>#/>#/>#/>#/>#/>#/>#/>#/")

      
      
"""
    Norlar: faces ve res klasöründeki isimlendirmeler her zaman küçük harf olmalı(büyük harf kullanılmamalı) 
    
    Notes: Naming in the faces and pic folder must always be in lower case (no upper case)
    
"""
      
      
      
      
      
      

