from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image
from tkinter import messagebox
import pyttsx3
import pywhatkit
import datetime
import webbrowser



topp=Tk()
topp.geometry('975x720')
topp.title('Welcome')


load = Image.open("chatbotimage1.jpg")
render = ImageTk.PhotoImage(load)


img = Label(topp, image=render)
img.image = render
img.place(x=0, y=0)



def roooot():

            root = Tk()
            root.geometry('985x720')
            root.iconbitmap('Google-Noto-Emoji-Smileys-10103-robot-face.ico')



            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)




            def talk():
                     engine = pyttsx3.init()
                     engine.say(e.get())
                     engine.runAndWait()


            new = 1
            url = "https://www.mcehassan.ac.in/"
            url1 = "https://mceparents.contineo.in/"
            url2 = "https://en.wikipedia.org/wiki/Malnad_College_of_Engineering"
            url3 = "https://www.youtube.com/watch?v=LqruhGHQdF8"
            url4 = "https://www.mcealumni.in/"
            url5 = "http://mceresults.contineo.in/"
            url6 = "https://www.google.com/search?q=images+of+MCE+college&rlz=1C1CHBF_en&sxsrf=ALeKk02hVQo6UkXQgDJJjBcaaSs6ExQKbg:1624778035488&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiC-pLtobfxAhXc7HMBHVyICAEQ_AUoAXoECAEQAw&biw=1280&bih=616"


            def openwebmce():
                webbrowser.open(url,new=new)

            def openwebcontineo():
                webbrowser.open(url1, new=new)

            def openwenwikimce():
                webbrowser.open(url2, new=new)

            def openclgtour():
                webbrowser.open(url3, new=new)

            def openalumnimceofficial():
                webbrowser.open(url4, new=new)

            def openresultspage():
                webbrowser.open(url5, new=new)

            def mceimages():
                webbrowser.open(url6, new=new)

            def _quit():
               root.quit()
               root.destroy()
               exit()


            def rule():
                    messagebox.showinfo("RULES", "PLEASE FOLLOW THESE RULES WHILE INTERACTING WITH ME \n 1) Do not ask multiple questions at a time.\n 2) Use simple language while interacting.\n 3) Do not use shortforms while conversing.\n 4) Try not to use special characters except question mark.\n 5) Only queries about MCE is responded,so please ask queries only regarding MCE.")

            def talkk(text):
                engine.say(text)
                engine.runAndWait()


            def neww():
                top=Toplevel()
                top.geometry('975x650')

                load = Image.open("malnad.png")
                render = ImageTk.PhotoImage(load)


                img = Label(top, image=render)
                img.image = render
                img.place(x=0, y=0)
                send = Button(top,
                              text='MCE Image', bg='black', fg='white', activebackground='grey', width=18,
                             command=mceimages).grid(row=3, column=5)

                Btn = Button(top,
                             text="MCE WEBSITE", bg='black', fg='white', activebackground='grey', width=18,
                             command=openwebmce).grid(row=3, column=1)

                Btn = Button(top,
                             text="MCE CONTINEO", bg='black', fg='white', activebackground='grey', width=18,
                             command=openwebcontineo).grid(row=3, column=10)

                Btn = Button(top,
                             text="MCE WIKIPEDIA", bg='black', fg='white', activebackground='grey', width=18,
                             command=openwenwikimce).grid(row=3, column=15)

                Btn = Button(top,
                             text="MCE TOUR", bg='black', fg='white', activebackground='grey', width=18,
                             command=openclgtour).grid(row=3, column=20)

                Btn = Button(top,
                             text="MCE ALUMNI WEBSITE", bg='black', fg='white', activebackground='grey', width=18,
                             command=openalumnimceofficial).grid(row=4, column=1)

                Btn = Button(top,
                             text="MCE RESULT PAGE", bg='black', fg='white', activebackground='grey', width=18,
                             command=openresultspage).grid(row=4, column=5)


                top.title('websites')




            main_menu = Menu(root)

            file_menu=Menu(root)
            file_menu.add_command(label = 'Contineo',command=openwebcontineo)
            file_menu.add_command(label = 'About MCE',command=openwenwikimce)
            file_menu.add_command(label = 'MCE tour video',command=openclgtour)
            file_menu.add_command(label = 'Malnad Alumni Association',command=openalumnimceofficial)


            main_menu.add_cascade(label='Open', menu = file_menu)
            main_menu.add_command(label='Rules',command =rule)
            main_menu.add_command(label='Website',command =openwebmce)
            main_menu.add_command(label='Quit',command =_quit)


            root.config(menu=main_menu)





            text = Text(root,bg='light blue',fg='black')
            text.grid(row=0,column=0,columnspan=2)

            responce="Hello!\n I am Jarvis,\n welcome to M C E chatbot"
            talkk(responce)


            def send():


                send = "You:"+ e.get()
                text.insert(END,"\n" + send)
                if(e.get()=='hi'):

                    responce="hey,how can I assist you?"
                    #language = 'en'

                    text.insert(END, "\n"   +"Jarvis :"+ responce)

                    talkk(responce)

                    #output = gTTS(text=responce, lang=language, slow=False)

                    #output.save("output.mp3")

                    #os.system("start output.mp3")
                    #text.insert(END, "\n" + "Bot :" + responce)
                elif(e.get()=='hello'):

                    responce = "namaste,chanagi idira"
                    #language = 'en'

                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                    #output = gTTS(text=responce, lang=language, slow=False)

                    #output.save("output.mp3")

                    #os.system("start output.mp3")
                    #text.insert(END, "\n" + "Jarvis : " + responce)
                elif (e.get() == 'hu chanagi idivi'):

                    responce = "santhosha"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)


                elif (e.get() == 'how are you?'):

                    responce = "I am good,what about you?"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "i'm fine too"):

                     responce= "glad to hear"
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)
                elif (e.get() == "where is MCE"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is MCE?"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is mce"):

                     responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)


                elif (e.get() == "where is mce?"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is mce located?"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is mce located"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is MCE located?"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "where is MCE locateds"):

                    responce = "It is located near Salgame road,Rangoli halla,Hassan,Karnataka-573201"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "what are the branches available in MCE"):

                    responce = "Computer Science,Mechanical,Civil,Information Science,Electronics and Communication,Automobile,Electronics and Electrical"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)


                elif (e.get() == "what are the branches available in MCE?"):

                    responce = "Computer Science,Mechanical,Civil,Information Science,Electronics and Communication,Automobile,Electronics and Electrical"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the H O D of computer science branch"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of cse branch"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of cse branch?"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of CSE branch"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of CSE branch?"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of cse"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == "who is the HOD of cse?"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of CSE"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "who is the HOD of CSE?"):

                    responce = "Mrs.Geetha Kiran is the H O D of Computer Science branch"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is swimming pool present in mce"):

                    responce = "Yes,we do have a 25meters swimming pool inside our campus"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is swimming pool present in mce?"):

                    responce = "Yes,we do have a 25meters swimming pool inside our campus"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is swimming pool present"):

                    responce = "Yes,we do have a 25meters swimming pool inside our campus"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is swimming pool present?"):

                    responce = "Yes,we do have a 25meters swimming pool inside our campus"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is gym present in mce"):

                    responce = "Yes ofcourse"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is gym present in mce?"):

                    responce = "Yes ofcourse"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is gym present"):

                    responce = "Yes ofcourse"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "is gym present?"):

                    responce = "Yes ofcourse"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif(e.get() == "what the hell"):

                    responce = "you are being disrespectful"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == "bye"):

                    responce = "bye,have a great day"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'who is the current dean of MCE'):

                    responce = "The current students affair dean of MCE is K.P Ravikumar, academic dean is Dr.B Uma and exam dean is Dr.Pradeep S"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is current students affair dean of MCE'):

                    responce = "The current student affair dean of MCE is K.P Ravikumar"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is current academic dean of MCE'):

                    responce = "The current academic dean of MCE is Dr.B Uma"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)


                elif (e.get() == 'who is current exam dean of MCE'):

                    responce = "The current exam dean of MCE is Dr.Pradeep S"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is the current principal of MCE'):

                    responce = "The current principal of MCE is Dr.C.V Venkatesh"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'is canteen present in MCE'):

                    responce = "Yes the canteen is present in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'Is library present in MCE'):

                    responce = "Yes the library is present in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how big is the campus'):

                    responce = "The college is built on a campus of about 44 acres(180,000 square meters"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is there Wifi facility available in MCE'):

                    responce = "Yes the wifi facility is available in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'When was MCE established'):

                    responce = "It was established in 1960,during the second 5 year plan of India, as a joint venture between the Government of India,Government of Karnataka and the Malnad Technical Education Society,Hassan"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is MCE affiliated'):

                    responce = "Yes MCE is affiliated with the Visvesvaraya Technological University in Belgaum"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is the Motto of MCE'):

                    responce = "The Motto of MCE in english is 'Nothing is equal to knowledge"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is the Motto of MCE in english'):

                    responce = "The Motto of MCE in english is 'Nothing is equal to knowledge"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is the type of MCE'):

                    responce = "It is Government Aided Engineering College"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'what is the motto of MCE'):

                    responce = "The Motto of MCE is Nahi Jnanena Sadrusham"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is campus present in rural or urban area'):

                    responce = "The campus is present in urban area"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'in which year did MCE became autonomous'):

                    responce = "In the year 2007 MCE became autonomous"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'has MCE received any Awards'):

                    responce = "Yes MCE has received many awards along with ISTE Award as One of the Best Engineering Colleges in the Country,in 2007"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'in which position does MCE stand in Karnataka'):

                    responce = "MCE stands in 36th position in Karnataka"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is there Gym facility in MCE '):

                    responce = "Yes there is gym facility in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'is there Smart class in MCE'):

                    responce = "Yes smart class are present in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is badminton court present in MCE'):

                    responce = "Yes the badminton court is present in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is basketball  court present in MCE'):

                    responce = "Yes the basketball court is present in MCE"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is the infrastructure of the MCE'):

                    responce = "College have a well equipped campus along with basic considerations like library, advanced labs, hostel , playground etc.The faculties have highest qualifications and are well experienced in thier respective fields."
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'what are placements provided by the college?'):

                    responce = " College offers the students with their recruiting partners which are Accenture, Amazon, Mercedes- benz,Bharath eletronics and TCS and other notabel companies"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how does college train the students with placement?'):

                    responce = " Our college will train the students with the long term placement training and will also provide with various workshops and internship programs"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what are the cultural activities of the college?'):
                    responce = "Our college conducts the biggest festival every semester by the cultural clubs of our college (eg: Leo club, Lit club , Technical club, Rotract club"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is it like to be a first year student here?'):
                    responce = "The subjects and concepts of first year will give a great exposure towards the basics of all the branches. College has prioritise the importance of sports and focus communication skills ( like professional English, Kannada"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how is the food in the canteen?'):
                    responce = "Our canteen serves with the best food of most of the varieties and is highly hygienic. It serves the students with "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how accessible are administrator, resistors , financial aid officers etc?'):
                    responce = "Our college has a institutional unit called STUDENT AFFAIRS OFFICE ( SA OFFICE) where the students issues will be resolved and the students can contact through the information given in the official handbook"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'which is the most popular place in the campus? '):
                    responce = "It is the college canteen - favourite hangout places, filled with memories and is the most happening places in the campus"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'what is TEQUIP?'):
                    responce = "It is Technical Education Quality Improvement Programme of government of India. its main aim is to improve quality of technical education and enhance exsisting capacities of the institution."
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is there an alumni association or an organisation in the college ?'):
                    responce = "Yes, Our college have the greatest and strongest bonding with the alumni of the institution where the alumni always support the growth of the institution by offering scholarship to the students studying the college . They also provide students with laptop and basic equipments."
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'what are the courses offered in the MCE?'):
                    responce = "BE/ B Tech , ME/ M Tech"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'what are the hostel facilities?'):
                     responce = "The hostel is hygienic , ragging free and has an security network • Boys hostel within the campus •Girls hostel near college(provided with bus facility)"
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)
                elif (e.get() == 'what are the existing clubs in the college?'):
                     responce = "clubs in out college are LEO , LIT , ECO , TECH , ROTO , CULTURAL "
                     text.insert(END, "\n" + " Jarvis :" +responce)

                     talkk(responce)
                elif (e.get() == 'when will exams be conducted?'):
                     responce = "decisions are yet to be made"


                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)
                elif (e.get() == 'do they conduct sports activities in mce?'):
                    responce = "yes we conduct sports activities in Malnad fest and we also have sports for 1st year students"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif 'play malnad college of engineering video' in e.get():

                        song = e.get().replace('play', '')
                        pywhatkit.playonyt(song)
                        responce = "playing malnad college of engineering-MCE video in youtube"
                        text.insert(END, "\n" + "Jarvis :" + responce)

                        talkk(responce)
                elif (e.get() == 'who is HOD of Mechanical Engineering'):
                    responce = " is the H O D of Mechanical Engineering is "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Civil Engineering'):
                    responce = " Dr. A J Krishnaiah is the H O D of Civil Engineering "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Electrical and Electronics Engineering'):
                    responce = "N.S Jyothi is the H O D of Electrical Engineering "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Automobile Engineering'):
                    responce = "Y M Shashidhar is the H O D of Automobile Engineering "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Electrical and Communication Engineering'):
                    responce = " Sujatha B R is the H O D of Electrical and Communication Engineering is "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Industrial and Production Engineering'):
                    responce = " is the H O D of Industrial and Production Engineering is "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is HOD of Information Science Engineering'):
                    responce = " Uma B is the H O D of Information Science Engineering is "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'who is there Auditorium in MCE'):
                    responce = " Yes there is Auditorium in MCE "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how many entrance are there for MCE'):
                    responce = " There are 3 entrances in MCE "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'is cellphones allowed inside MCE'):
                    responce = " Yes cellphones are allowed inside the campus but not during class hours "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif (e.get() == 'is there any library cards available'):
                    responce = " There are General library cards and MIBB library cards available"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)

                elif (e.get() == 'how is lab facility in MCE'):
                     responce = "The labs in MCE are well equiped with advanced machinaries and well maintained "
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)

                elif (e.get() == 'how is parking facility in the college'):
                     responce = " The parking is separately alloted to both boys and girls inside the college premises"
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)

                elif (e.get() == 'is there any meditation hall in your college'):
                     responce = " Yes there is a place called Divya Chaitanya where you can meditate."
                     text.insert(END, "\n" + "Jarvis :" + responce)

                     talkk(responce)

                elif (e.get() == 'is there any stationary shop inside MCE'):
                    responce = " Yes there is stationary shop inside MCE "
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)
                elif 'time' in e.get():
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talkk('Current time is ' + time)
                    text.insert(END, "\n" + "Bot : Current time is" + time)

                elif (e.get() == 'open mce wikipedia'):
                    responce="opening M C E wikipedia"
                    text.insert(END, "\n" + " Jarvis :  opening MCE wikipedia")
                    talkk(responce)
                    messagebox.showinfo("Information", "redirecting you to mce wikipedia")
                    open.command=openwenwikimce()
                elif (e.get() == 'open mce contineo'):
                    responce="opening M C E contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    talkk(responce)
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    open.command = openwebcontineo()
                elif (e.get() == 'where can i find my internals marks?'):
                    responce = "you can find your internal marks in our contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    talkk(responce)
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    open.command=openwebcontineo()
                elif (e.get() == 'where can i find my internals marks'):
                    responce = "you can find your exam history in our contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                elif (e.get() == 'where can i find my exam history'):
                    responce = "you can find your exam history in our contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                    open.command = openwebcontineo()
                elif (e.get() == 'where can i find calender of events'):
                    responce = "you can find calender of events in our contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                    open.command = openwebcontineo()
                elif (e.get() == 'where can i view registered courses'):
                    responce = "you can find your registered courses in our contineo"
                    text.insert(END, "\n" + " Jarvis :  you can find your registered courses in our contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                    open.command = openwebcontineo()
                elif (e.get() == 'where can i view fee details'):
                    responce = "you can find fee details in our contineo"
                    text.insert(END, "\n" + " Jarvis :  you can find fee details in our contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                    open.command = openwebcontineo()
                elif (e.get() == 'where can i find my exam history?'):
                    responce = "you can find your exam history in our contineo"
                    text.insert(END, "\n" + " Jarvis :  opening MCE contineo")
                    messagebox.showinfo("Information", "redirecting you to mce contineo")
                    talkk(responce)
                    open.command = openwebcontineo()
                elif (e.get() == 'open mce website'):
                    responce="opening M C E website"
                    text.insert(END, "\n" + " Jarvis :  opening MCE website")
                    messagebox.showinfo("Information", "redirecting you to mce website")
                    talkk(responce)
                    open.command=openwebmce()
                elif (e.get() == 'open mce alumni website'):
                    responce="opening M C E alumni website"
                    text.insert(END, "\n" + " Jarvis :  opening MCE alumni website")
                    messagebox.showinfo("Information", "redirecting you to mce alumni website")
                    talkk(responce)
                    open.command=openalumnimceofficial()
                elif (e.get() == 'where can i find my results?'):
                    responce = "you can find your results here \n do check"
                    text.insert(END, "\n" + " Jarvis :  opening results page")
                    talkk(responce)
                    messagebox.showinfo("Information", "redirecting you to mce result page")
                    open.command = openresultspage()
                elif(e.get()=='okay'):
                    responce="okay\n,do you have any other queries?,please respond with \nyes \nor \nno"
                    #language = 'en'
                    text.insert(END, "\n" + "Jarvis : "+ responce)

                    talkk(responce)
                elif(e.get()=='yes'):
                    responce="go on! Ask me"
                    #language = 'en'
                    text.insert(END, "\n" + "Jarvis : "+ responce)

                    talkk(responce)
                elif(e.get()=='no'):
                    responce="okay,hope i answered to all your queries,thank you for reaching us"
                    #language = 'en'
                    text.insert(END, "\n" + "Jarvis : "+ responce)

                    talkk(responce)
                    messagebox.askquestion("feedback", "Was i helpful?")
                    e.delete(0, END)
                else:
                    responce = "Sorry I did not get it,\n or i may not have information about it"
                    text.insert(END, "\n" + "Jarvis :" + responce)

                    talkk(responce)


                e.delete(0,END)

            e = Entry(root,
                          width=80,cursor='mouse',bg='white',selectbackground='purple')
            send = Button(root,
                          text='Send',bg='black',fg='white',activebackground='grey',width=18,command=send).grid(row=1,column=1)
            send = Button(root,
                          text='speak',bg='light grey',fg='black',activebackground='grey',width=18,command=talk).grid(row=2,column=1)
            btn = Button(root,
                         text="MCE related \n websites",bg='black',fg='white',activebackground='grey',width=18,command=neww).grid(row=5,column=1)

            e.grid(row=1,column=0)



            root.title('CHATBOT')

myFont=font.Font(family='Times New Roman',size=18,weight='bold')
Btn = Button(topp, text="Open Chatbot", bg='light blue', fg='black', activebackground='grey', width=11,command=roooot)

Btn['font']=myFont
Btn.place(x=554,y=400)

topp.mainloop()
