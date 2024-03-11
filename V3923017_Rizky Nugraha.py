#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd= ""
)

#prepering a cursor object
cursorObject = database.cursor()

#creating database
cursorObject.execute("CREATE DATABASE D3_TeknikInformatika_2024")


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="D3_TeknikInformatika_2024"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA VARCHAR(30) NOT NULL,
                    ALAMAT VARCHAR(255),
                    MATKUL_DIIKUTI VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

database.close()


# In[3]:


import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TeknikInformatika_2024"
)

#preparing cursor
cursorObject = database.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAMA, ALAMAT, MATKUL_DIIKUTI) VALUES (%s, %s, %s, %s)"
val = [("V3922011",  "ARVIN", "MADIUN", "PBO"),
       ("V3922012",  "DEVINA", "CARUBAN", "BASIS DATA"),
       ("V3922013",  "HABIB", "WONOASRI", "STATISTIKA"),
       ("V3922014",  "PUPUT", "MEJAYAN", "MIKROKONTROLER"),
       ("V3922015",  "RIZKY", "KEBONSARI", "PEMWEB")
      ]

cursorObject.executemany(sql, val)
database.commit()

#Disconnect
database.close()


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="D3_TeknikInformatika_2024"
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE Dosen (
                    NIP VARCHAR(20) NOT NULL PRIMARY KEY,
                    NAMA_DOSEN VARCHAR(50) NOT NULL,
                    MATKUL_DIAJAR VARCHAR(50)
                    )"""

cursorObject.execute(studentRecord)

dataBase.close()


# In[5]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TeknikInformatika_2024"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, NAMA_DOSEN, MATKUL_DIAJAR) VALUES (%s, %s, %s)"
val = [("19089756",  "PAK DARMAWAN", "PBO"),
       ("19806748",  "BU MASBAHAH", "BASIS DATA"),
       ("16759839",  "BU TRISNA", "STATISTIKA"),
       ("28479021",  "PAK YUSUF", "MIKROKONTROLER"),
       ("19492470",  "BU ZULMI", "PSO")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()


# In[6]:


import mysql.connector

database = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database ="D3_TeknikInformatika_2024"
)

cursorObject = database.cursor()

studentRecord = """CREATE TABLE Mata_Kuliah (
                    KODE_MATKUL VARCHAR(10) NOT NULL PRIMARY KEY,
                    NAMA_MATKUL VARCHAR(50) NOT NULL,
                    NAMA_DOSEN VARCHAR(20),
                    WAKTU DATE,
                    RUANGAN VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)

database.close()


# In[7]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TeknikInformatika_2024"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Mata_kuliah (KODE_MATKUL, NAMA_MATKUL, NAMA_DOSEN, WAKTU, RUANGAN) VALUES (%s, %s, %s, %s, %s)"
val = [("12121212",  "PBO", "PAK DARMAWAN", "2023-1-1", "Lab 1"),
       ("23232323",  "BASIS DATA", "BU MASBAHAH", "2023-1-1", "Lab 2"),
       ("34343434",  "STATISTIKA", "BU TRISNA", "2023-1-1", "Lab 1"),
       ("45454545",  "MIKROKONTROLER", "PAK YUSUF", "2023-1-1", "R. Mikro"),
       ("56565656",  "PEMWEB", "BU ZULMI", "2023-1-2", "Lab 2")
      ]

cursorObject.executemany(sql, val)
dataBase.commit()


# In[8]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "D3_TeknikInformatika_2024"
)

cursorObject = dataBase.cursor()

query = "SELECT NAMA_MATKUL, NAMA_DOSEN FROM Mata_Kuliah"
cursorObject.execute (query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    
dataBase.close()


# In[ ]:




