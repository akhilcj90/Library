import os
import csv
class HeadClub:
    def __init__(self):
        self._username = 'Head'
        self._password = 'xyz'
    def welcome(self):
        print('\t\t\t\t\t WELCOME TO MASTER_PYTHON_CLUB!')
        rand = input("Press Enter_Key to continue.........")
    def Login(self):
        while(True):
            login_id = input('Enter the Login_Name: ')
            login_pswrd = input('Enter the password: ')
            if self._username == login_id and self._password == login_pswrd:
                print('Login Successfully!!!!!')
                break
            else:
                print('LoginName or password is wrong')
    def menu(self):
        while(True):
            print('1.Add Acccount'
                  '\n2.Delete Account'
                  '\n3.Update Account'
                  '\n4.exit')
            choose = input('Choose the items from the menu: ')
            RD = ReadHead()
            if choose == '1':
                RD.CreateAccount()
            elif choose == '2':
                RD.DeleteAccount()
            elif choose == '3':
                RD.UpdateAccount()
            elif choose == '4':
                exit()
class Member:
    def __init__(self):
        self._Clubid = ''
        self._Name = ''
        self._Adress = ''
        self._Gender = ''
        self._PhoneNumber = ''
        self._Mail_Id = ''
        self._AdharNo = ''
    def MainDetails(self):
        self._Clubid = int(input('Enter the club_id'))
        self._Name = input('Enter the name: ')
        self._Adress = input('Enter the Address: ')
        self._Gender = input('Enter the Gender: ')
        self._PhoneNumber  = int(input('Enter the Contact Number: '))
        self._Mail_Id = input('Enter the Mail_id: ')
        self._AdharNo = input('Enter the Adhar_Number: ')
    def Display(self):
        print('club_id',self._Clubid)
        print('Name: ',self._Name)
        print('Address ',self._Adress)
        print('Gender ',self._Gender)
        print('PhoneNumber: ',self._PhoneNumber)
        print('Mail_ID ',self._Mail_Id)
        print('Adhar_Number ',self._AdharNo)
    def WriteToFile(self):
        data = [self._Clubid,self._Name,self._Adress,self._Gender,self._PhoneNumber,
                self._Mail_Id,self._AdharNo]
        opencsv = open('Club.csv','a',newline='')
        writecsv = csv.writer(opencsv,delimiter = ',')
        writecsv.writerow(data)
        opencsv.close()
class ReadHead:
    def CreateAccount(self):
        m = Member()
        m.MainDetails()
        m.Display()
        m.WriteToFile()
    def DeleteAccount(self):
        mid = input('Enter the club_id to delete: ')
        opencsv = open('Club.csv')
        readercsv = csv.reader(opencsv,delimiter = ',')
        copy_opencsv = open('Club_1.csv','a',newline='')
        write_copy_opencsv = csv.writer(copy_opencsv,delimiter = ',')
        flag = 0
        for row in readercsv:
            if row[0] == mid:
                flag = 1
                continue
            write_copy_opencsv.writerow(row)
        if flag != 1:
            print('Club_Member id is invalid!!!!!!')
        else:
            opencsv.close()
            os.remove('Club.csv')
            copy_opencsv.close()
            os.rename('Club_1.csv','Club.csv')
    def UpdateAccount(self):
        print('Work in Progress.....Thank you for the patience')

model = HeadClub()
model.welcome()
model.Login()
model.menu()