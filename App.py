import cv2
import numpy as np
import os
from PIL import Image
from os import listdir
from os.path import isfile, join
from pathlib import Path
import subprocess
from subprocess import call
from subprocess import Popen
import sys
import tkinter as tk
from tkinter import messagebox
import pyAesCrypt
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
# import mysql.connectori
import sqlite3
# from recogv2 import recog

connectiondb = sqlite3.connect('passdb.db')
cursordb = connectiondb.cursor()


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

#==========================================================================================================================================================================================

def createtraining():
    # Load HAAR face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load functions
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if faces is ():
            return None
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = "datasets/User." + str(count) + ".jpg"
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            result = messagebox.askquestion("Wajah tidak ditemukan", "Pastikan menghadap kamera dan tidak ada cahaya terang dibelakang karena dapat mengganggu deteksi, Apakah ingin melanjutkan?", icon='warning')
            if result == 'yes':
                pass
            else:
                break  

        if cv2.waitKey(10) & 0xFF == ord('q') or count == 100:
            break
            
    cap.release()
    cv2.destroyAllWindows()            
        
def createtrainingp1():
    # Load HAAR face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load functions
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if faces is ():
            return None
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 101

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = "datasets/User." + str(count) + ".jpg"
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            result = messagebox.askquestion("Wajah tidak ditemukan", "Pastikan menghadap kamera dan tidak ada cahaya terang dibelakang karena dapat mengganggu deteksi, Apakah ingin melanjutkan?", icon='warning')
            if result == 'yes':
                pass
            else:
                break  

        if cv2.waitKey(1) == 13 or count == 200: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()      

def createtrainingp2():
    # Load HAAR face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load functions
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if faces is ():
            return None
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 201

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = "datasets/User." + str(count) + ".jpg"
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            result = messagebox.askquestion("Wajah tidak ditemukan", "Pastikan menghadap kamera dan tidak ada cahaya terang dibelakang karena dapat mengganggu deteksi, Apakah ingin melanjutkan?", icon='warning')
            if result == 'yes':
                pass
            else:
                break  

        if cv2.waitKey(1) == 13 or count == 300: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()      

def createtrainingp3():
    # Load HAAR face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load functions
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if faces is ():
            return None
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 301

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = "datasets/User." + str(count) + ".jpg"
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            result = messagebox.askquestion("Wajah tidak ditemukan", "Pastikan menghadap kamera dan tidak ada cahaya terang dibelakang karena dapat mengganggu deteksi, Apakah ingin melanjutkan?", icon='warning')
            if result == 'yes':
                pass
            else:
                break  

        if cv2.waitKey(1) == 13 or count == 400: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()      

def createtrainingp4():
    # Load HAAR face classifier
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Load functions
    def face_extractor(img):
        # Function detects faces and returns the cropped face
        # If no face detected, it returns the input image
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if faces is ():
            return None
        
        # Crop all faces found
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h, x:x+w]

        return cropped_face

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 401

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = "datasets/User." + str(count) + ".jpg"
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            result = messagebox.askquestion("Wajah tidak ditemukan", "Pastikan menghadap kamera dan tidak ada cahaya terang dibelakang karena dapat mengganggu deteksi, Apakah ingin melanjutkan?", icon='warning')
            if result == 'yes':
                pass
            else:
                break  

        if cv2.waitKey(1) == 13 or count == 500: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()      
#========================================================================================================================================================================================
def cektrai():
    # os.path.exists('.trainer/trainer.yml') 
    my_file = Path("trainer/trainer.yml")
    if my_file.is_file():
        print ('ada')
    else:
        messagebox.showerror("Error", "Data train belum ada!") 

def recog():
    cektrai()
    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    assure_path_exists("trainer/")

    # Load the trained mode
    recognizer.read('trainer/trainer.yml')

    # Load prebuilt model for Frontal Face
    cascadePath = "haarcascade_frontalface_default.xml"

    # Create classifier from prebuilt model
    faceCascade = cv2.CascadeClassifier(cascadePath);

    # Set the font style
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,500)
    fontScale              = 1
    color                  = (255,255,255)
    lineType               = 2
    org                    = (50, 50)
    thickness              = 2


    # Initialize and start the video frame capture
    cam = cv2.VideoCapture(0)

    # Loop
    while True:

        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.5,5)

        cv2.putText(im, 'Tekan Q untuk keluar', org, font, fontScale, color, thickness, cv2.LINE_AA) 

        # For each face in faces
        for(x,y,w,h) in faces:
            
            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)


            # Recognize the face belongs to which ID
            Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            hasil = round(140 - confidence)
            
            # Check the ID if exist 
            if hasil > 90:
                Id = "Terbuka".format(hasil)
                lockRaiseFrame()
                cv2.destroyAllWindows() 
                return
                                            
            else:
                Id = "Tidak Dikenali".format(hasil)
                    # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
            
                    
        # Display the video frame with the bounded rectangle
        cv2.imshow('Pengenalan Wajah',im)
          
        # If 'q' is pressed, close program
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    # Stop the camera
    cam.release()
    # Close all windows
    cv2.destroyAllWindows() 

def training():
    import cv2, os
    import numpy as np
    from PIL import Image
    import os

    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
    # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Using prebuilt frontal face training model, for face detection
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    # Create method to get the images and label data
    def getImagesAndLabels(path):

        # Get all file path
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        
        # Initialize empty face sample
        faceSamples=[]
        
        # Initialize empty id
        ids = []

        # Loop all the file path
        for imagePath in imagePaths:

            # Get the image and convert it to grayscale
            PIL_img = Image.open(imagePath).convert('L')

            # PIL image to numpy array
            img_numpy = np.array(PIL_img,'uint8')

            # Get the image id
            id = int(os.path.split(imagePath)[-1].split(".")[1])

            # Get the face from the training images
            faces = detector.detectMultiScale(img_numpy)

            # Loop for each face, append to their respective ID
            for (x,y,w,h) in faces:

                # Add the image to face samples
                faceSamples.append(img_numpy[y:y+h,x:x+w])

                # Add the ID to IDs
                ids.append(id)

        # Pass the face array and IDs array
        return faceSamples,ids

    # Get the faces and IDs
    faces,ids = getImagesAndLabels('datasets')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    assure_path_exists('trainer/')
    recognizer.save('trainer/trainer.yml')
    messagebox.showinfo("Berhasil", "Data selesai di Train!")

def buka_file():
    global letak
    fileName = askopenfilename(parent=root, title='Pilih File')
    file = Label(root, text=fileName)
    file.place(x=150, y=50)
    letak = file.cget("text")

def pancingandb():
    cursordb.execute('CREATE TABLE IF NOT EXISTS password (id INTEGER, passw TEXT)')
    cursordb.execute('SELECT * FROM password WHERE (id=?)', ('1'))  
    entry = cursordb.fetchone()
    if entry is None:
        cursordb.execute("INSERT INTO password (id, passw) VALUES (1, 123)")
        print ('New entry added')
    else:
        print ('Entry found')
#===========================================================================================
def login_verification():
    pass_verification = password_verification.get()
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    if cursordb.fetchone() is not None:
        messagebox.showinfo("Bersiap", "Foto akan diambil 100x mohon untuk menghadap kamera dan melepas semua aksesoris di wajah, tatap beberapa saat lalu putar perlahan searah jarum jam, tekan OK untuk mulai!")
        createtraining() 
    else:
        messagebox.showerror("Error", "Password salah!") 

def login_verificationp1():
    pass_verification = password_verification.get()
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    if cursordb.fetchone() is not None:
        messagebox.showinfo("Bersiap", "Foto akan diambil 100x mohon untuk menghadap kamera dan melepas semua aksesoris di wajah, tatap beberapa saat lalu putar perlahan searah jarum jam, tekan OK untuk mulai!")
        createtrainingp1() 
    else:
        messagebox.showerror("Error", "Password salah!") 

def login_verificationp2():
    pass_verification = password_verification.get()
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    if cursordb.fetchone() is not None:
        messagebox.showinfo("Bersiap", "Foto akan diambil 100x mohon untuk menghadap kamera dan melepas semua aksesoris di wajah, tatap beberapa saat lalu putar perlahan searah jarum jam, tekan OK untuk mulai!")
        createtrainingp2() 
    else:
        messagebox.showerror("Error", "Password salah!") 

def login_verificationp3():
    pass_verification = password_verification.get()
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    if cursordb.fetchone() is not None:
        messagebox.showinfo("Bersiap", "Foto akan diambil 100x mohon untuk menghadap kamera dan melepas semua aksesoris di wajah, tatap beberapa saat lalu putar perlahan searah jarum jam, tekan OK untuk mulai!")
        createtrainingp3() 
    else:
        messagebox.showerror("Error", "Password salah!") 

def login_verificationp4():
    pass_verification = password_verification.get()
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    if cursordb.fetchone() is not None:
        messagebox.showinfo("Bersiap", "Foto akan diambil 100x mohon untuk menghadap kamera dan melepas semua aksesoris di wajah, tatap beberapa saat lalu putar perlahan searah jarum jam, tekan OK untuk mulai!")
        createtrainingp4() 
    else:
        messagebox.showerror("Error", "Password salah!") 

def hapusentry():
    passEntry.delete(0, END)
    pwbaruentry.delete(0, END)
    pwlamaentry.delete(0, END)

def stoptrain():
    cv2.destroyAllWindows()

def gantipassw():
    pass_verification = password_verification.get() 
    cursordb.execute('select * from password where passw ="%s"' % (pass_verification))
    
    if len(password_verification1.get()) == 0:
        messagebox.showerror("Error", "Password baru tidak boleh kosong!") 
    
    elif cursordb.fetchone() is not None:
        pass_verification = password_verification.get()
        pass_verification1 = password_verification1.get()
        cursordb.execute('UPDATE password SET passw = "%s" WHERE passw = "%s"' % (pass_verification1, pass_verification))
        messagebox.showinfo("Berhasil", "Password telah diganti!")
        hapusentry()

    else:
        messagebox.showerror("Error", "Password lama salah!") 
              
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


root = tk.Tk()
root.title("Aplikasi pengamanan data")
root.geometry("865x300")

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/4 - windowWidth/3)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))


#Frames
loginFrame = tk.Frame(root)
regFrame = tk.Frame(root)
userMenuFrame = tk.Frame(root)
gantipass = tk.Frame(root)
root1 = tk.Frame(root)

#Define Frame List
frameList=[loginFrame,regFrame,userMenuFrame,gantipass,root1]
#Configure all Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='white',width='865', height='300')
	
def raiseFrame(frame):
	frame.tkraise()

def regFrameRaiseFrame():
	raiseFrame(regFrame)
def logFrameRaiseFrame():
	raiseFrame(loginFrame)
def gantipassRaiseFrame():
	raiseFrame(gantipass)
def lockRaiseFrame():
	raiseFrame(root1)
#Tkinter Vars
#Stores user's name when registering
name = tk.StringVar()
#Stores user's name when they have logged in
loggedInUser = tk.StringVar()

# def test():
# 	command = "python Recog.py"
# 	subprocess.Popen(command)
	
global password_verification
global password_verification1
password_verification = StringVar()
password_verification1 = StringVar()


banner = tk.Label(loginFrame, background='black', text="Data Encryp", width=35, font=('Futura', 32), fg='white')
banner.place(x=0, y=0)

loginButton = tk.Button(loginFrame,text="Login", width=45, command=recog, bg="bisque",font=('Futura', 20))
loginButton.place(x=70, y=80)

regButton = tk.Button(loginFrame,text="Train Wajah",width=45 ,command=combine_funcs(regFrameRaiseFrame, pancingandb), bg="gainsboro",font=('Futura', 20))
regButton.place(x=70, y=155)

# =====================================================================================================================================================

bannertrain = tk.Label(regFrame,text="Trainer", font=("Futura",33),fg='white',width=35, bg="black")
bannertrain.place(x=0, y=0)

labelpass = tk.Label(regFrame,text="Password",font=("Futura",20),bg="white")
labelpass.place(x=10, y=80)

passEntry=tk.Entry(regFrame,textvariable=password_verification, bg="gray90", show= "*", font=("Futura",20))
passEntry.place(x=150, y=80)

registerButton = tk.Button(regFrame,text="Daftar P0",command=login_verification,width=10, bg="white",font=("Futura", 10))
registerButton.place(x=150, y=140)

registerButton = tk.Button(regFrame,text="P1",command=login_verificationp1,width=4, bg="white",font=("Futura", 10))
registerButton.place(x=250, y=140)

registerButton = tk.Button(regFrame,text="P2",command=login_verificationp2,width=4, bg="white",font=("Futura", 10))
registerButton.place(x=300, y=140)

registerButton = tk.Button(regFrame,text="P3",command=login_verificationp3,width=4, bg="white",font=("Futura", 10))
registerButton.place(x=350, y=140)

registerButton = tk.Button(regFrame,text="P4",command=login_verificationp4,width=4, bg="white",font=("Futura", 10))
registerButton.place(x=400, y=140)


backButton = tk.Button(regFrame,text="Kembali",command=combine_funcs(logFrameRaiseFrame,hapusentry), bg="gray25",font=("Futura", 15), fg="white")
backButton.place(x=740, y=9)

gantiButton = tk.Button(regFrame,text="Ganti Password",command=combine_funcs(gantipassRaiseFrame, hapusentry),bg="white",font=("Futura", 15))
gantiButton.place(x=10, y=240)

trainButton = tk.Button(regFrame,text="Train",command=training,width=15, bg="bisque",font=("Futura", 10))
trainButton.place(x=470, y=140)

infodaftar=tk.Label(regFrame, text="Catatan : Profil tersebut di isi sesuai intensitas cahaya apabila dirasa akurasi mulai menurun di tempat atau ruangan tertentu bisa ditambah untuk meningkatkan akurasi di antara P0 sampai dengan P5", wraplength=250, justify=LEFT)
infodaftar.place(x=600, y=200)

# ===password===============================================================================================================

bannergantipass = tk.Label(gantipass,text="Ganti Password ",bg="black", width=35,font=("Futura",33), fg="white")
bannergantipass.place(x=0, y=0)

pwlama = tk.Label(gantipass,text="Password Lama",font=("Futura",20),bg="white")
pwlama.place(x=10, y=80)

pwbaru = tk.Label(gantipass,text="Password Baru",font=("Futura",20),bg="white")
pwbaru.place(x=10, y=125)

pwlamaentry = passEntry=tk.Entry(gantipass,textvariable=password_verification,show= "*", bg="gray90", font=("Futura",20))
pwlamaentry.place(x=220, y=81)

pwbaruentry = passEntry=tk.Entry(gantipass, textvariable=password_verification1,show= "*", bg="gray90", font=("Futura",20))
pwbaruentry.place(x=220, y=126)

submitButton = tk.Button(gantipass,text="Submit",command=combine_funcs(gantipassw, hapusentry), width=10, bg="white",font=("Futura", 10))
submitButton.place(x=220, y=180)

submitButton = tk.Button(gantipass,text="Kembali",command=regFrameRaiseFrame,bg="gray25",font=("Futura", 15), fg="white")
submitButton.place(x=740, y=9)

# ==========================================================================================================================
mylabel3=Label(root1, text="Pilih file yang akan dilakukan encrypt atau decrypt", wraplength=250,width=300,bg="black",fg="white", justify=LEFT)
mylabel3.place(x=-930, y=0)
browse = Button(root1, text="Pilih File", command=buka_file)
browse.place(x=25, y=50)

mylabel2=Label(root1, text="Nama File Baru", justify=LEFT, bg='#dbdbdb')
mylabel2.place(x=25, y=90)

f = Entry(root1, width=30, bg='#dbdbdb')
f.place(x=175, y=90)

mylabel=Label(root, text="Password", bg='#dbdbdb')
mylabel.place(x=25, y=100)

e = Entry(root, width=30, bg='#dbdbdb')
e.place(x=175, y=95)

try:
    letak
except NameError:
    letak = None

def popup_enkripsi():
    messagebox.showinfo("Enkripsi status", "Enkripsi berhasil")

def popup_enkripsi_error():
    messagebox.showwarning("Enkripsi status", "File belum dipilih")

def popup_dekrip():
    messagebox.showinfo("Dekrip status", "Dekrip sukses")

def popup_dekrip_error():
    messagebox.showwarning("Dekrip status", "File belum dipilih")

def myDecrypt():

    bufferSize = 256 * 1024
    password=e.get()
    
    pyAesCrypt.decryptFile(letak, f.get(), password, bufferSize)

def myEncrypt():
    bufferSize = 256 * 1024
    password=e.get()
    pyAesCrypt.encryptFile(letak, f.get(), password, bufferSize)
    
def enkripsi():
    if letak is None:
        popup_enkripsi_error()
    else:
        myEncrypt()
        popup_enkripsi()

def dekrip():
    if letak is None:
        popup_dekrip_error()
    else:
        myDecrypt()
        popup_dekrip()


myButton = Button(root1, text="Encrypt", width=10, command=enkripsi)
myButton.place(x=45, y=150)



myButton2 = Button(root1, text="Decrypt", width=10, command=dekrip)
myButton2.place(x=150, y=150)

mylabel4=Label(root1, text="Catatan : Pastikan anda mengingat format file yang di encrypt atau decrypt atau anda dapat menyertakan format file pada nama file", wraplength=250, justify=LEFT)
mylabel4.place(x=25, y=200)

    

#Load Faces
raiseFrame(loginFrame)
root.iconbitmap('.\ico.ico')
root.mainloop()
connectiondb.commit()
connectiondb.close()