import os

import pickle

import time

id=0

x=0

m=0

class Customer:

    

    def __init__(self):

        self.name=None

        self.mobile_no=None

        self.email=None

        self.username=None

        self.password=None

        self.pass_t_id=[]

        self.b_no=[]

        self.t_bill=[]

        self.t_ref=[]

        self.security_ques=None

        self.security_pas=None

       

    def storedata(self):

        print()

        self.name=input('Enter Name- ')

        stat=0

        self.mobile_no=input('Enter Mobile Number- ')

        while stat==0:

            if len(self.mobile_no)!=10:

                print ('Invalid Mobile Number')

                self.mobile_no=input('Please Enter Valid Mobile Number- ')

            else:

                stat=1

        self.email=input('Enter Email ID- ')

        pos=0

        while pos==0:

            if '@' in self.email and '.' in self.email:

                pos=1

            else:

                print ('Invalid Email ID')

                self.email=input('Please Enter Valid Email ID- ')

               



    def display_pas(self):

        print( '----------------------------------------CustomerDetails----------------------------------------')

        print()

        print ('Customer Name : ',self.name)

        print ('Customer Mobile : ',self.mobile_no)

        print ('Customer Email : ',self.email)

        print()

        print ('------------------------------------------------------------------------------------------------------')



def forgot_password():



    status=0

    while status==0:        

        username=input('Enter Username- ')

        f=open("customer.dat","rb")

        p=Customer()

        st=1

        try:            

            while True:

                

                p=pickle.load(f)
                if p.username==username:

                    status=1

                    st=0

                    print()

                    ans=input(p.security_ques+'- ')

                    print()

                    password=p.security_pas

                    if ans.lower()==password.lower():

                        print('Password : ',p.password)

                        print()

                    else:

                        print ('Wrong Answer')

                        print()                        

                    break

                       

        except EOFError:

            f.close()

            

        if status==0 and st==1:

            os.system('clear')

            print('\nIncorrect Username')

            print('--------------------Choose The Following--------------------')

            print('1)Retry Username')

            print ('2)Exit To Main Menu')

            print()

            c=input('Enter Your Choice (Number)- ')
            if(c.isnumeric()):
                c = int(c)
  
            if c==1:

                pass

            elif c==2:

                break

            else:

                print('Invalid Entry')

  

                

def security():

    global security_pas, security_ques

    status=0

    while status==0:

        print('Pick Your Security Question')

        print()

        print( '--------------------------------------Security Questions--------------------------------------')

        print( '1)What is the last name of the teacher who gave you your first failing grade?')

        print( '2)What is the name of your first pet?')

        print( '3)What is the name of the first beach you visited?')

        print('4)What was your favorite place to visit as a child?')

        print( '5)What was the make and model of your first car?')

        print('6)What was your maternal grandfathers first name?')

        print( '7)In what city or town does your nearest sibling live?')

        print('8)Any Other (Custom)')

        print()

        c=input('Enter Your Choice (Number)- ')
        if(c.isnumeric):
            c = int(c)

        os.system('clear')

        if c==1:

            security_ques='What is the last name of the teacher who gave you your first failing grade?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==2:

            security_ques='What is the name of your first pet?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==3:

            security_ques='What is the name of the first beach you visited?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==4:

            security_ques='What was your favorite place to visit as a child?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==5:

            security_ques='What was the make and model of your first car?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==6:

            security_ques='What was your maternal grandfather\'s first name?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==7:

            security_ques='In what city or town does your nearest sibling live?'

            print()

            security_pas=input('Enter Answer For The Security Question- ')

            status=1

        elif c==8:

            security_ques=input('Enter A Question Of Your Choice (Without \'?\')- ')

            print()

            security_ques=security_ques+'?'

            security_pas=input('Enter The Answer For The Security Question- ')

            status=1

        else:

            print ('Invalid Entry')

        print()

    return ([security_ques,security_pas])  

    

def change_password(user,pas):



    global new_pass

    stat=0

    

    while stat==0:

        print()

        password=input('Enter Old Password- ')                

        if password==pas:

            stat=1

            new_pass=input('Enter New Password- ')

            sta=0

            while sta==0:

                confirm_pass=input('Re-Enter (Confirm) Your New Password- ')                

                if confirm_pass==new_pass:

                    sta=1

                    print( '\nYour New Password Is Confirmed\n')



                else:

                    print( '\nYour New Password Is Not Confirmed\n')

                    sta=0

            

        else:

            print( '\nThe Password You Gave Was Incorrect')

            stat=0

    

    f1=open("customer.dat","rb")

    f2=open("newfile.dat","wb")

    s=Customer()



    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                s.password=new_pass

            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")

    

def edit_pas(user):

    

    f1=open("customer.dat","rb")

    f2=open("newfile.dat","wb")

    s=Customer()



    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                print( '-----------------------------------Edit Details-----------------------------------')

                print( '1)Customer Name\n2)Customer Mobile\n3)Customer Email\n4)All Details')

                print ()

                ch=input('Enter Your Choice (Number)- ')

                if(ch.isnumeric()):
                    ch = int(ch)

                os.system('clear')

                if ch==1:

                    s.name=input('Enter New Name- ')

                elif ch==2:

                    stat=0

                    s.mobile_no=input('Enter New Mobile Number- ')

                    while stat==0:

                        if len(s.mobile_no)!=10:

                            print( 'Inavlid Mobile Number')

                            s.mobile_no=input('Enter New Mobile Number- ')

                        else:

                            stat=1

                elif ch==3:

                    s.email=input('Enter New Email- ')

              

                elif ch==4:

                    s.storedata()

                    

                else:

                    print ('Invalid Entry')

                    

            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")

    

def disp_pas():

    f=open('customer.dat','rb')

    s=Customer()

    try:

        i=1

        while True:

            s= pickle.load(f)

            print( 'Customer '+str(i))

            s.display_pas()

            i=i+1

            

    except EOFError:

        f.close()  



def del_pass():

    

    f=open('customer.dat','rb+')

    i=1

    try:

        while True:

            s= pickle.load(f)

            print('Customer '+str(i))

            s.display_pas()

            i=i+1

            

    except EOFError:

        f.close()        

    print()

    f=open('customer.dat','wb+')

    c=input('Enter Your Choice (Number)- ')
    if(c.isnumeric()):
        c= int(c)

    i=1

    while i<c:

        s=pickle.load(f)

        i=i+1        

    s=pickle.load(f)

    user=s.username

    f.close()

    

    f1=open("customer.dat","ab+")

    f2=open("newfile.dat","wb")

    

    try:

        while True:

            s= pickle.load(f1)

            if s.username!=user:

                pickle.dump(s,f2)

      

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","v.dat")

    print()

    print('User Account Deleted\n')



def disp_pass(user):



    f=open('customer.dat','ab+')  

    status=0

    while status==0:

        s=pickle.load(f)

        if s.username==user:

            s.display_pas()

            status=1



    f.close()        

      

def sign_in():

    print( '----------------------------------------Login----------------------------------------')

    x=0

    username='sfdag'

    password='sdg'

    pos=0

    status=0

    while status==0:

        

        username=input('Enter Username- ')

        f=open("customer.dat","rb")

        p=Customer()

        st=1

        try:            

            while True:

                p= pickle.load(f)

                if p.username==username:

                    status=1

                    stat=0

                    while stat==0:

                        password=input('Enter Password- ')

                        if p.password==password:

                            os.system('clear')

                            print()

                            print( 'You Are Signed In- ')

                            print (p.name)

                            print()

                            stat=1

                            st=0

                            status=1                                                    

                        else:

                            stat=0

                            os.system('clear')

                            print ('\nIncorrect Password')

                            print ('--------------------Choose The Following--------------------')

                            print ('1)Change Username')

                            print ('2)Retry Password')

                            print ('3)Exit And Return To Main Menu')

                            print()

                            c=input('Enter Your Choice (Number)- ')
                            if(c.isnumeric()):
                                c = int(c)

                            if c==1:

                                stat=1

                                status=0

                                st=0

                            elif c==2:

                                stat=0

                            elif c==3:

                                stat=1

                                status=0

                                st=0

                                x=1                           

                            else:

                                print( 'Invalid Entry')

                    if stat==1:

                        break

                else:

                    status=0

                        

        except EOFError:

            f.close()

        if x==1:

            pos=1

            break

        if status==0 and st==1:

            os.system('clear')

            print ('\nIncorrect Username')

            print('--------------------Choose The Following--------------------')

            print( '1)Retry Username')

            print ('2)Exit To Main Menu')

            print()

            c=input('Enter Your Choice (Number)- ')
            if(c.isnumeric()):
                c = int(c)

            if c==1:

                pass

            elif c==2:

                pos=1

                break

            else:

                print( 'Invalid Entry')



    return([username,password,pos])





def sign_up():

    



    

    username=input('Create A Username- ')

    p=Customer()

        

    password=input('Create (Enter) A Password- ')

    stat=0

    

    while stat==0:

        confirm_pass=input('Re-Enter (Confirm) Your Password- ')                

        if confirm_pass==password:

            os.system('clear')

            stat=1

            print ('\nYour Password Is Confirmed')

            print ('Account Created')

            print ('Username : ',username)

            print ('Password : ',password)

            print()

            

        else:

            stat=0

            print( '\nPassword Not Confirmed\n')



    return([username,password])



def add_member(user,pas):

    

    f=open("customer.dat","ab+")    

    p=Customer()

    secure=list(security())

    p.security_ques=secure[0]

    p.security_pas=secure[1]

    p.storedata()

    p.username=user

    p.password=pas

    pickle.dump(p,f)

    f.close()

    

class movie_details:



    def __init__(self):

        self.admin_user='Jason'

        self.admin_pass='abcd'

        self.date=None

        self.movie_id=None

        self.movie_name=None

        self.from_l=None

        self.to_l=None

        self.genre=[]

        self.len_cruise=0

        self.t_std_seat=80

        self.t_vip_seat=50

        self.t_sui_seat=30

        self.a_std_seat=80

        self.a_vip_seat=50

        self.a_sui_seat=30

        self.f_cus=0

        self.f_std=0

        self.f_vip=0

        self.f_sui=0



    def input_data(self):

        self.movie_name=input('Enter Movie Name- ')

        self.date=input('Enter Date Of Movie (DD\MM\YY)- ')

        self.genre=input('Enter Genre 1- ')

        self.len_cruise=input('Enter Time Of Movie In Minutes- ')

        self.t_std_seat=input('Enter Number Of Standard Seats- ')

        self.t_seats_seat=input('Enter Number Of VIP Seats- ')

        self.t_sui_seat=input('Enter Number Of Suite Seats- ')

        self.f_cus=input('Enter Admission Fee Per Person- ')

        self.f_std=input('Enter Cost Per Standard Seat- ')

        self.f_vip=input('Enter Cost Per VIP Seat- ')

        self.f_sui=input('Enter Cost Per Suite Seat- ')

        self.movie_id=self.date[0]+self.date[1]+self.date[3]+self.movie_name+self.date[4]+self.date[6]+self.date[7]

        self.a_std_seat=self.t_std_seat

        self.a_vip_seat=self.t_vip_seat

        self.a_sui_seat=self.t_sui_seat

       



    def display(self):

        

        print ('--------------------------------------------Movie Details--------------------------------------------')

        print()

        print( 'ID :',self.movie_id)

        print ('Movie Name :',self.movie_name)

        print ('Date Of Movie :',self.date)

        print ('Genres :',self.genre)

        print ('Duration Of Movie In Minutes :',self.len_cruise)

        print ('Total Number Of Standard Seats :',self.t_std_seat)

        print ('Total Number Of VIP Seats :',self.t_vip_seat)

        print ('Total Number Of Suite Seats:',self.t_sui_seat)

        print ('Number Of Available Standard Seats :',self.a_std_seat)

        print ('Number Of Available VIP Seats :',self.a_vip_seat)

        print ('Number Of Available Suite Seats :',self.a_sui_seat)

        print ('Admission Fee Per Person : '+'$'+str(self.f_cus))

        print ('Cost Per Standard Seat : '+'$'+str(self.f_std))

        print ('Cost Per VIP Seat : '+'$'+str(self.f_vip))

        print ('Cost Per Suite Seat : '+'$'+str(self.f_sui))

        print()

        print('--------------------------------------------------------------------------------------------------------')



def create_movie():

    

    f=open("movie_details.dat","wb+")    

    n=input("Enter Number Of Movies (To Be Entered or Screened )- ")

    s=movie_details()

    for i in range(n):

        s.input_data()

        pickle.dump(s,f)

    f.close()





def add_movie():

    

    f=open("movie_details.dat","ab+")    

    n=input("Enter Number Of Movies (To Be Entered or Screened)- ")
    if(n.isnumeric()):
        n = int(n)

    s=movie_details()

    for i in range(n):

        print ('Movie '+str(i+1))

        print ('-------------------------------------------------------------------------------------')

        s.input_data()

        pickle.dump(s,f)

    f.close()

    print ('\n')



def display_movie():
    f=open('movie_details.dat','rb')

    i=1

    try:

        while True:

            s= pickle.load(f)

            print ('movie '+str(i))

            s.display()

            i=i+1

            

    except EOFError:
        f.close()



    

def del_movie():

    global id 



    display_movie() 

    id=input('enter movie id to be deleted: ')

    f1=open("movie_details.dat","rb")

    f2=open("newfile.dat","wb")

    

    try:

        while True:

            s= pickle.load(f1)

            if s.movie_id!=id:

                pickle.dump(s,f2)

            else:pass

      

    except EOFError:

        f1.close()

        f2.close()

    print ('Movie id deleted')

    f1.close()

    f2.close()

    os.remove("movie_details.dat")

    os.rename("newfile.dat","movie_details.dat")





def book_seat(user):

    global id

    

    no_people=input('Enter Number Of People (Children < 3 :Free Admission)- ')
    if(no_people.isnumeric()):
        no_people = int(no_people)

    b_std=input('Enter Number Of Standard Seats To Be Booked- ')

    if b_std=='0' or b_std=='':

        b_std=0

    else:

        b_std=int(b_std)

    b_vip=input('Enter Number Of VIP Seats To Be Booked- ')

    if b_vip=='0' or b_vip=='':

        b_vip=0

    else:

        b_vip=int(b_vip)

    b_sui=input('Enter Number Of Suite Seats To Be Booked- ')

    if b_sui=='0' or b_sui=='':

        b_sui=0

    else:

        b_sui=int(b_sui)

    receipt(b_std,b_vip,b_sui,no_people,user)

    ch = input('Do You Want To Confirm Booking (y/n)- ')

    os.system('clear')    

    if ch.lower()=='y':

        t_bil=t_bill(b_std,b_vip,b_sui,no_people,user)

        t_reff=t_ref(b_std,b_vip,b_sui,user)

        #  TODO: Check what this if was for. If ch is y then it can't be 0 or 1 so just made this an if else. Confirm if I'm missing something cause the first if will never run
        if ch==0:

            print ('\nInsufficient Amount')

            print ('\nBooking Not Confirmed\n')

        else:

            update_seat(b_std,b_vip,b_sui)

            update_b_no(b_std,b_vip,b_sui,user)

            update_t_bill(t_bil,t_reff,user)

            #  TODO: This function doesn't exist so not sure what it's for
            # update_cus_t_id(user)

            print ('\nBooking Confirmed\n')

            

    else:

        print ('\nBooking Not Confirmed\n')



def t_bill(b_std,b_vip,b_sui,no_people,user):

    global id 

    f=open('customer.dat','rb')

    s=Customer()

    status=0

    while status==0:

        s=pickle.load(f)

        if s.username==user:

            f1=open('movie_details.dat','rb')

            try:

                while True:

                    sh= pickle.load(f1)

                    if sh.movie_id==id:

                        t_bill=sh.f_cus*no_people+b_std*sh.f_std+b_vip*sh.f_vip+b_sui*sh.f_sui

                        return (t_bill)

            except EOFError:

                    f1.close()        

            status=1



        else:

            status=0

    f.close()

    

def t_ref(b_std,b_vip,b_sui,user):

    global id 

    f=open('customer.dat','rb')

    s=Customer()

    status=0

    while status==0:

        s=pickle.load(f)

        if s.username==user:

            f1=open('movie_details.dat','rb')

            try:

                while True:

                    sh= pickle.load(f1)

                    if sh.movie_id==id:

                        t_ref=b_std*int(sh.f_std)+b_vip*int(sh.f_vip)+b_sui*int(sh.f_sui)

                        return (t_ref)

            except EOFError:

                    f1.close()        

            status=1



        else:

            status=0

    f.close()

    

def receipt(b_std,b_vip,b_sui,no_people,user):

    os.system('clear')

    lcltime = time.asctime( time.localtime(time.time()) )

    global id 

    f=open('customer.dat','rb')

    s=Customer()

    status=0

    while status==0:

        s=pickle.load(f)

        if s.username==user:

            f1=open('movie_details.dat','rb')

            try:

                while True:

                    sh= pickle.load(f1)

                    if sh.movie_id==id:

                        t_bill=int(sh.f_cus)*no_people+b_std*int(sh.f_std)+b_vip*int(sh.f_vip)+b_sui*int(sh.f_sui)

                        print ('\n                                               Cinema Enterprises LTD')

                        print ('----------------------------------------------------------RECEIPT----------------------------------------------------------')

                        print ('\t   Customer Name: '+s.name+'\t                                  '+lcltime)

                        print ('\t   Movie Name : '+sh.movie_name)

                        print ('\t   Date Of Movie : '+sh.date)

                        print ('\t   Number Of Standard Seats : '+str(b_std))

                        print ('\t   Number Of VIP Seats : '+str(b_vip))

                        print ('\t   Number Of Suite Seats : '+str(b_sui))

                        print ('\t   '+str(no_people)+'x'+str(sh.f_cus)+'='+'$'+str(int(sh.f_cus)*no_people))

                        print ('\t   '+str(b_std)+'x'+str(sh.f_std)+'='+'$'+str(b_std*int(sh.f_std)))

                        print ('\t   '+str(b_vip)+'x'+str(sh.f_vip)+'='+'$'+str(b_vip*int(sh.f_vip)))

                        print ('\t   '+str(b_sui)+'x'+str(sh.f_sui)+'='+'$'+str(b_sui*int(sh.f_sui)))

                        print ('--------------------------------------------------------------------------------------------------------------------------------')

                        print ('\t   TOTAL : '+str(t_bill)+'$')

                        print ('--------------------------------------------------------------------------------------------------------------------------------' )                       

            

            except EOFError:

                    f1.close()        

            status=1                 



        else:

            status=0

    f.close()



def update_seat(b_std,b_vip,b_sui):

    global id    

    f1=open("movie_details.dat","rb+")

    f2=open("newfile.dat","wb")

    s=movie_details()



    try:

        while True:

            s= pickle.load(f1)

            if s.movie_id==id:

                s.a_std_seat=int(s.t_std_seat)-b_std 

                s.a_vip_seat=int(s.t_vip_seat)-b_vip

                s.a_sui_seat=int(s.t_sui_seat)-b_sui  

            pickle.dump(s,f2)

    except EOFError:

        f1.close()

        f2.close()

    os.remove("movie_details.dat")

    os.rename("newfile.dat","movie_details.dat")



def update_b_no(b_std,b_vip,b_sui,user):

    f1=open("customer.dat","rb+")

    f2=open("newfile.dat","wb")

    s=Customer()

    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                s.b_no=s.b_no+list([[b_std,b_vip,b_sui]])



            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")



def update_t_bill(t_bill,t_reff,user):

    f1=open("customer.dat","rb+")

    f2=open("newfile.dat","wb")

    s=Customer()

    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                s.t_bill=s.t_bill+list([t_bill])

                s.t_ref=s.t_ref+list([t_reff])

            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")



def update_pass_t_id(user):

    global id



    f1=open("customer.dat","rb")

    f2=open("newfile.dat","wb")

    s=Customer()



    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                s.pass_t_id=s.pass_t_id+list([id])

            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")

def find_movie_genre():

    global id



    f=open("Movie_details.dat","rb")

    print ('------------------------Genre------------------------')

    try:

        i=1

        while True:

            s= pickle.load(f)

            print (str(i)+')'+s.genre[0]+','+s.genre[1])

            i=i+1

                

    except EOFError:

        f.close()



    f=open("movie_details.dat","rb")

    print ()

    c=input('Enter Your Choice (Number)- ')
    if(c.isnumeric()):
        c = int(c)

    os.system('clear')

    i=1

    while i<c:

        s=pickle.load(f)

        i=i+1

    s=pickle.load(f)

    print    ()

    print ('Your Movie Is '+s.movie_name)

    id=s.movie_id

    s.display()

    f.close()



def find_movie_date():

    global id



    f=open("movie_details.dat","rb")

    print ('---------------------------Dates---------------------------')

    try:

        i=1

        while True:

            s= pickle.load(f)

            print (str(i)+')'+s.date)

            i=i+1

                

    except EOFError:

        f.close()

        

    f=open("movie_details.dat","rb")

    print ()

    c=input('Enter Your Choice (Number)- ')
    if(c.isnumeric()):
        c = int(c)

    os.system('clear')

    i=1

    while i<c:

        s=pickle.load(f)

        i=i+1

    s=pickle.load(f)

    print    ()

    print ('Your Movie Is '+s.movie_name)

    id=s.movie_id

    s.display()

    f.close()



def find_movie_len():

    global id



    f=open("movie_details.dat","rb")

    print ('------------------------Length Of Movie------------------------')

    try:

        i=1

        while True:

            s= pickle.load(f)

            print (str(i)+')'+str(s.len_cruise)+' Minutes')

            i=i+1

                

    except EOFError:

        f.close()

        

    f=open("movie_details.dat","rb")

    print()

    c=input('Enter Your Choice (Number)- ')
    if(c.isnumeric()):
        c = int(c)

    os.system('clear')

    i=1

    while i<c:

        s=pickle.load(f)

        i=i+1

    s=pickle.load(f)

    print    ()

    print ('Your Movie Is '+s.movie_name)

    id=s.movie_id

    s.display()

    f.close()







def find_movie(user):

    global m

    global id

    print ('--------------------------------Find Your Movie--------------------------------')

    print ('1)Genre\n2)Dates\n3)Length Of Movie')

    print ()

    ch=input('Enter Your Choice (Number)- ')
    if(ch.isnumeric()):
        ch = int(ch)

    os.system('clear')

    m=0

    if  ch==1:

        find_movie_genre()

    elif ch==2:

        find_movie_date()

    elif ch==3:

        find_movie_len()

    else:

        print ('Invalid Entry')

        m=1

    



def reset_movie():

    print ('---------------------------------------Reset Movie---------------------------------------')

    print ('1)Reset Any One Movie')

    print ('2)Reset All Movie')

    print()

    ch=input('Enter Your Choice (Number)- ')
    if(ch.isnumeric()):
        ch = int(ch)

    os.system('clear')

    if ch==1:

        display_movie()

        

        id=input('Enter movie id to reset - ')

        

        f1=open("movie_details.dat","rb")

        f2=open("newfile.dat","wb")

        s=movie_details()

        try:

            while True:

                s= pickle.load(f1)

                if s.movie_id==id:

                    s.a_std_seat=s.t_std_seat

                    s.a_vip_seat=s.t_vip_seat

                    s.a_sui_seat=s.t_sui_seat

                pickle.dump(s,f2)

            

        except EOFError:

            f1.close()

            f2.close()

        os.remove("movie_details.dat")

        os.rename("newfile.dat","movie_details.dat")

        print ('\nMovie'+str(id)+' Has Been Reset\n')

    elif ch==2:

        f1=open("movie_details.dat","rb")

        f2=open("newfile.dat","wb")

        s=movie_details()

        try:

            while True:

                s= pickle.load(f1)

                s.a_std_seat=s.t_std_seat

                s.a_vip_seat=s.t_vip_seat

                s.a_sui_seat=s.t_sui_seat

                pickle.dump(s,f2)

            

        except EOFError:

            f1.close()

            f2.close()

        os.remove("movie_details.dat")

        os.rename("newfile.dat","movie_details.dat")

        print ('\nAll Movies Have Been Reseted\n')

def check_movie(user):

    global id

    f1=open("customer.dat","rb")

    f2=open("newfile.dat","wb")

    s=Customer()



    try:

        while True:

            s= pickle.load(f1)

            if s.username==user:

                if id in s.pass_t_id:

                    return(1)

                else:

                    return(0)

            pickle.dump(s,f2)

            

    except EOFError:

        f1.close()

        f2.close()

    os.remove("customer.dat")

    os.rename("newfile.dat","customer.dat")





def main():

    global m, sta



    t='y'

    while t.lower()=='y':

        

        print ('---------------------------------Welcome To S and L Enterprises LTD---------------------------------')

        print ('1) Administrative login')

        print ('2) Customer Login')

        print ('3) Exit')

        print()

        choice = input ('Enter Your Choice (Number) - ')
        if(choice.isnumeric()):
            choice = int(choice)
        os.system('clear')

        if choice == 1:

            print ('---------------------------------Admin Login---------------------------------')

            status=0

            x=0

            while status==0:

                user=input('Enter Admin Username- ')

                if user=='admin':

                    status=1

                    stat=0                    

                    while stat==0:

                        pas=input('Enter Admin Password- ')

                        if pas=='abcd':

                            os.system('clear')

                            print ('\nWelcome Administrator\n')

                            stat=1

                        else:

                            os.system('clear')

                            print ('\nIncorrect Password')

                            print ('--------------------Choose The Following--------------------')

                            print ('1)Retry Password')

                            print ('2)Exit And Return To Main Menu')

                            print ()

                            c=input('Enter Your Choice (Number)- ')
                            if(c.isnumeric()):
                                c = int(c)

                            if c==1:

                                stat=0

                            elif c==2:

                                stat=1

                                status=0

                                x=1                           

                            else:

                                print ('Invalid Entry')



                else:

                    status=0

                    os.system('clear')

                    print ('\nIncorrect Username')

                    print ('--------------------Choose The Following--------------------')

                    print ('1)Retry Username')

                    print ('2)Exit To Main Menu')

                    print ()

                    c=input('Enter Your Choice (Number)- ')
                    if(c.isnumeric()):
                        c = int(c)

            

                    if c==1:

                        pass

                    elif c==2:

                        break

                    else:

                        print ('Invalid Entry')

                if x==1:

                    break



            if status==1:

                statu=1

                while statu==1:

                    print ('----------------------------------------Administrative Features----------------------------------------')

                    print ('1)Display Movie\n2)Create Movie\n3)Delete Movie\n4)Reset Movie Seats\n5)Display User Accounts\n6)Delete All User Accounts\n7)Logout And Return To Main Menu')

                    print ()

                    c=input('Enter Your Choice (Number)- ')
                    if(c.isnumeric()):
                        c = int(c)

                    os.system('clear')

                    if c==1:

                        print ('--------------------------------------------------------------------------------------------------------')

                        display_movie()

                    elif c==2:

                        add_movie()

                    elif c==3:

                        del_movie()

                    elif c==4:

                        reset_movie()

                    elif c==5:

                        disp_pas()

                    elif c==6:

                        del_pass()

                    elif c==7:

                        statu=0

        elif choice==2:

            print ('1)Login (Existing Account)')

            print ('2)Create New Account')

            print ('3)Forgot Password?')

            we=input('enter choice (number):')
            if(we.isnumeric()):
                we = int(we)

            if we==1:

                account=list(sign_in())

                if account[2]==0:

                    stat=0

                    user=account[0]

                    pas=account[1]

                    while stat==0:

                        print ('--------------------------------User Account--------------------------------')

                        print ('1)Find Movie and Book Seat')

                        print ('2)Cancel Customer Bookings')

                        print ('3)Edit Customer Details')

                        print ('4)Change Password')

                        print ('5)Change Security Question')

                        print ('6)Logout and Return To Main Menu')

                        stat=1

                        print()

                        ch=input('Enter Your Choice (Number)- ')
                        if(ch.isnumeric()):
                            ch = int(ch)

                        os.system('clear')

                        if ch==1:

                            find_movie(user)

                            m=check_movie(user)

                            if m==1:

                                print ('\nThis Movie Is Already Booked\n')

                                stat=0

                            

                            else:

                                if m==0:                    

                                    book_seat(user)

                                    stat=0

                        elif ch==2:

                            print ('all your bookings have been cancelled')

                            print ('your money will be refunded')

                        elif ch==3:

                            edit_pas(user)

                            stat=0

                        elif ch==4:

                            change_password(user,pas)

                            sta=1

                        elif ch==5:

                            f1=open("customer.dat","rb")

                            f2=open("newfile.dat","wb")

                            s=Customer()

                            secure=list(security())

                            try:

                                while True:

                                    s= pickle.load(f1)

                                    if s.username==user:

                                        s.security_ques=secure[0]

                                        s.security_pas=secure[1]

                                    pickle.dump(s,f2)

                

                            except EOFError:

                                f1.close()

                                f2.close()

                            os.remove("customer.dat")

                            os.rename("newfile.dat","customer.dat")

                            stat=0



                        elif ch==6:

                            sta=1

                        else:

                            print ('Invalid Entry')

                            stat=0

            elif we==2: 



                    account=sign_up()

                    user=account[0]

                    pas=account[1]

                    os.system('clear')

                    add_member(user,pas)



            elif we==3:        

                    forgot_password()

            else:

                print ('choice entered in invalid:')

            

        elif choice==3:

            exit()

    if sta==1:

         t='y'

main()

