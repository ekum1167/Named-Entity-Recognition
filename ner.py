import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import json
import sys
import codecs


inp = sys.argv[1]
i = open (inp, 'r', encoding= 'utf-8')
SAMPLE_TEXT = i.read()

LOCATIONS = []
    
opened_file = open( 'locations.txt', "r", encoding="utf8")

for line in opened_file:
    line = line.strip().title()
    LOCATIONS.append(line)

#print(LOCATIONS)

org = open("organizations.txt" , "r", encoding="utf8")
ORGANIZATIONS = org.readlines()
for i,line in enumerate(ORGANIZATIONS):
    ORGANIZATIONS[i] = line.strip().title()
#print(ORGANIZATIONS)
org.close()

#print(ORGANIZATIONS)
p = open("person.txt" , "r", encoding = "utf-8")
PERSON = p.readlines()
for j,line in enumerate(PERSON):
    PERSON[j] = line.rstrip().title()
#print(PERSON)
p.close()
# https://simplemaps.com/data/tr-cities for locations in turkey
# https://simplemaps.com/data/world-cities for locations in world
# https://gist.github.com/emrekgn/b4049851c88e328c065a for names

#ORGANIZATIONS
#https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27deki_bankalar_listesi 
#https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27deki_%C3%BCniversiteler_listesi
#https://en.wikipedia.org/wiki/List_of_companies_of_Turkey  
#https://fortune.com/global500/2020/search/
#https://www.forbes.com/global2000/#148296f4335d


#SAMPLE_TEXT = """Sabancı Üniversitesi 1999 yılında Prof. Dr. Tosun Terzioğlu kurucu rektörlüğünde İstanbul, Tuzla ilçesinde kurulmuştur.\nŞimdiki rektörü Prof. Dr. Yusuf Leblebici’dir."""

#sent = preprocess(SAMPLE_TEXT)
#print(sent)



#Decided to keep list of words that are printed in order to prevent double printing the same value.
DATE_VAL = []
LOC_VAL = []
ORG_VAL =[]
PERSON_VAL = []



SAMPLE_TEXT = SAMPLE_TEXT.split('\n')
#print(SAMPLE_TEXT)
for iter,line in enumerate(SAMPLE_TEXT):

    #if 'okulu' in SAMPLE_TEXT[iter] or 'Okulu' in SAMPLE_TEXT[iter]:
    words = re.finditer(r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )*(([İi]lk|[Oo]rta|[Yy]üksek|[Oo]kulu?)|[Ll]ise)[a-zçğıöşü\']*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in ORG_VAL and word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "ORGANIZATION "+ word[0])
            ORG_VAL.append(word)
   
    if 'yıl' in SAMPLE_TEXT[iter]:
        words =  re.finditer(r'\d{4}(?=\s+yıl\w+)',SAMPLE_TEXT[iter])
        for word in words:
            if word not in DATE_VAL and word[0] != ' ': 
                print(("Line "+ str(iter+1) + ": " + "DATE "+word[0]))
                DATE_VAL.append(word)

    if 'Dr.' in SAMPLE_TEXT[iter]:
        words = re.finditer(r'(?<=Dr. )([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in PERSON_VAL and word[0] != '': 
                print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
                PERSON_VAL.append(word)
    
  
    #Başkanımız can also find Cumhurbaşkanımız
    #if 'Belediye Başkanı' in SAMPLE_TEXT[iter] or 'belediye başkanı' in SAMPLE_TEXT[iter] or 'Belediye başkanı' in SAMPLE_TEXT[iter] or 'belediye Başkanı' in SAMPLE_TEXT[iter]:
    words = re.finditer(r'([A-ZÇĞİÖŞÜa-zçğıöşü]*[bB]aşkanı)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != ' ': 
            print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
            PERSON_VAL.append(word)
    
    words = re.finditer(r'([A-ZÇĞİÖŞÜa-zçğıöşü]*[Bb]akanı)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != ' ': 
            print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
            PERSON_VAL.append(word)

    
    words = re.finditer(r'([Vv]ali)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != '': 
            print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
        PERSON_VAL.append(word)
    #if 'Kaymakam' in SAMPLE_TEXT[iter] or 'kaymakam ' in SAMPLE_TEXT[iter] :
    words = re.finditer(r'([kK]aymakam)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != '': 
            print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
            PERSON_VAL.append(word)

    words = re.finditer(r'([Mm]üdür)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != '': 
            print(("Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
            PERSON_VAL.append(word)

    words = re.finditer(r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )+([Üü]niversitesi|[Kk]ulübü|[tT]akımı|[dD]erneği|[Hh]oldingi?|[Vv]akfı|[Ee]nstitüsü|[kK]urumu|[bB]anka?(sı)?|[Şş]irketi?)[a-zçğıöşü\']*' , SAMPLE_TEXT[iter])
    for word in words:
        if word not in ORG_VAL and word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "ORGANIZATION "+ word[0] )
            ORG_VAL.append(word)

    #if 'Bey' in SAMPLE_TEXT[iter] or 'bey' in SAMPLE_TEXT[iter] or 'Hanım' in SAMPLE_TEXT[iter]  or 'hanım' in SAMPLE_TEXT[iter] or 'hoca' in SAMPLE_TEXT[iter] or 'Hoca' in SAMPLE_TEXT[iter] or 'Abi' in SAMPLE_TEXT[iter] or 'abi' in SAMPLE_TEXT[iter] or 'Ağabey' in SAMPLE_TEXT[iter] or 'ağabey' in SAMPLE_TEXT[iter] :
    words= re.finditer (r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )+([Bb]ey|[Hh]anım|[Hh]oca|[Aa]bi|[Aa]ğabey|[aA]bla)[a-zçğıöşü\']*', SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "PERSON "+ word[0])
            PERSON_VAL.append(word)
    #Köyü Dağı Mahallesi Sokak
    words= re.finditer (r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )+([Kk]öyü?|[Mm]ahalles?i?|[Dd]ağı?|[Ss]oka[k|(ğı)]|[Cc]adde(si)?|[Ss]ite(si)?|[Kk]öprü(sü)?|[Ss]arayı?|[Mm]ezarlı[k(ğı)])[a-zçğıöşü\']*', SAMPLE_TEXT[iter])
    for word in words:
        if word not in PERSON_VAL and word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "LOCATION "+ word[0])
            PERSON_VAL.append(word)

    if 'Sayın' in SAMPLE_TEXT[iter] or 'sayın' in SAMPLE_TEXT[iter] or 'Sevgili' in SAMPLE_TEXT[iter] or 'sevgili' in SAMPLE_TEXT[iter]:
        words = re.finditer(r'(?<=[Ss]ayın )([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in PERSON_VAL and word[0] != ' ':
                print("Line "+ str(iter+1) + ": "  +  "PERSON "+ word[0][:-1])
                PERSON_VAL.append(word)
    if 'AŞ' in SAMPLE_TEXT[iter] or 'L.T.D.' in SAMPLE_TEXT[iter] or 'A.Ş.' in SAMPLE_TEXT[iter] or 'A.Ş' in SAMPLE_TEXT[iter ] or 'LTD' in SAMPLE_TEXT[iter ] or 'LTD.' in SAMPLE_TEXT[iter ] or 'ŞTİ.' in SAMPLE_TEXT[iter ] or 'ŞTİ' in SAMPLE_TEXT[iter ] or 'Ş.T.İ.' in SAMPLE_TEXT[iter]:
        words = re.finditer(r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]* )+(LTD.?|ŞTİ.?|A.Ş.?)[a-zçğıöşü\']*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in ORG_VAL and word[0] != ' ':
                print("Line "+ str(iter+1) + ": "  +  "ORGANIZATION "+ word[0])
                ORG_VAL.append(word)
    #date-1
    words = re.finditer(r'([0-3]?[0-9])? ?([Oo]cak|[Şş]ubat|[Mm]art|[Nn]isan|[Mm]ayıs|[Hh]aziran|[Tt]emmuz|[Aa]ğustos|[Ee]ylül|[Ee]kim|[Kk]asım|[Aa]ralık) [12][0-9][0-9][0-9][a-zçğıöşü\']*',SAMPLE_TEXT[iter])
    for word in words:
        if word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "DATE "+ word[0])
    
    for uppercaseWord in re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT[iter]):
        uppercaseWord = SAMPLE_TEXT[iter][uppercaseWord.start():uppercaseWord.end()]
        #print("uppercase word is :", uppercaseWord)
        if uppercaseWord in PERSON and uppercaseWord not in PERSON_VAL:
            print(("Line "+ str(iter+1) + ": "+"PERSON "+  uppercaseWord ))
            PERSON_VAL.append(uppercaseWord)
        elif uppercaseWord in LOCATIONS and uppercaseWord not in LOC_VAL:
            print(("Line "+ str(iter+1) + ": "+"LOCATION "+ uppercaseWord ))
            LOC_VAL.append(uppercaseWord)
        elif uppercaseWord in ORGANIZATIONS and uppercaseWord not in ORG_VAL:
            print(("Line "+ str(iter+1) + ": "+"ORGANIZATION "+  uppercaseWord))
            ORG_VAL.append(uppercaseWord)
    

    #if 'ilçe' in SAMPLE_TEXT[iter]:
    words = re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+[İi]lçe[a-zçğıöşü\']*)',SAMPLE_TEXT[iter])
    for word in words:
        if word not in LOC_VAL and word[0] != ' ':
            print(("Line "  + str(iter+1) + ": "+"LOCATION "+ word[0]))
            LOC_VAL.append(word)
    #if 'belde' in SAMPLE_TEXT[iter]:
    words = re.finditer(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+[Bb]elde[a-zçğıöşü\']*)',SAMPLE_TEXT[iter])
    for word in words:
        if word not in LOC_VAL and word[0] != ' ':
            print(("Line "  + str(iter+1) + ": "+"LOCATION "+ word[0]))
            LOC_VAL.append(word)

    #date-2
    words = re.finditer(r'[0-9]{1,2}(/|-|.)[0-9]{1,2}(/|-|.)[0-9]{4}', SAMPLE_TEXT[iter])
    for word in words:
        if word[0] != ' ':
            print(("Line "  + str(iter+1) + ": "+"DATE "+ word[0]))
    #date-3
    words = re.finditer(r'/^([0-9]|0[0-9]|1[0-9]|2[0-3])(:|.)[0-5][0-9]$/',SAMPLE_TEXT[iter]) # HOUR FORMAT https://digitalfortress.tech/tricks/top-15-commonly-used-regex/
    for word in words:
        if word[0] != ' ':
            print("Line "  + str(iter+1) + ": "+"DATE "+ word[0])


    #Ocak ayı, ocak ayında #date-4
    words = re.finditer(r'([Oo]cak|[Şş]ubat|[Mm]art|[Nn]isan|[Mm]ayıs|[Hh]aziran|[Tt]emmuz|[Aa]ğustos|[Ee]ylül|[Ee]kim|[Kk]asım|[Aa]ralık)(\')*[a-zçğıöşü]* (ayı[a-zçğıöşü\']*)?',SAMPLE_TEXT[iter])
    for word in words:
        if word[0] != ' ':
            print("Line "  + str(iter+1) + ": "+"DATE "+ word[0])
    #date-5
    #pazartesi,salı, ... günü
    words = re.finditer(r'([Pp]azartesi|[Ss]alı|[Çç]arşamba|[Pp]erşembe|[Cc]uma|[Cc]umartesi|[Pp]azar)(\')*[a-zçğıöşü]* (günü[a-zçğıöşü\']*)?',SAMPLE_TEXT[iter])
    for word in words:
        if word[0] != ' ':
            print("Line "  + str(iter+1) + ": "+"DATE "+ word[0])
    
    #date-6
    #2000'de
    words = re.finditer(r'\d{4}(?=\')[(A-Z)ÇĞİÖŞÜ(a-z)çğıöşü]*?',SAMPLE_TEXT[iter])
    for word in words:
        if word[0] != ' ':
            print("Line "  + str(iter+1) + ": "+"DATE "+ word[0])





"""
if 'Dr.' in SAMPLE_TEXT[iter]:
        words = re.findall(r'(?<=Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in PERSON_VAL: 
                print(("Line "+ str(iter+1) + ": "+"PERSON "+ word))
                PERSON_VAL.append(word)
"""

"""
# RULE_EXAMPLE 3
    if 'Prof. Dr.' in SAMPLE_TEXT[iter] or 'Dr. ' in SAMPLE_TEXT[iter] or 'Sn.' in SAMPLE_TEXT[iter] or ('SN. ') in SAMPLE_TEXT[iter] :
        words = re.findall(r'(?<=Dr.S[Nn]. [A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in PERSON_VAL: 
                print(("Line "+ str(iter+1) + ": "+"PERSON "+ word))
                PERSON_VAL.append(word)

"""

"""
#if 'Cumhurbaşkanı' in SAMPLE_TEXT[iter] or 'cumhurbaşkanı' in SAMPLE_TEXT[iter]:
words = re.finditer(r'(?<=[Cc]umhurbaşkanı)[a-zçğıöşü\']*\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
for word in words:
    if word not in PERSON_VAL and word[0] != ' ': 
        print(("4Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
        PERSON_VAL.append(word)
"""
"""           
    if 'Prof. Dr. ' in SAMPLE_TEXT[iter]:
        words = re.finditer(r'(?<=Prof. Dr. )([A-ZÇĞİÖŞÜ][a-zçğıöşü]* ?)*',SAMPLE_TEXT[iter])
        for word in words:
            if word not in PERSON_VAL and word[0] != '': 
                print(("3,1Line "+ str(iter+1) + ": "+"PERSON "+ word[0][:-1]))
                PERSON_VAL.append(word)
"""

"""
#We already wrote university below. No need to double check
if 'Üniversite' in SAMPLE_TEXT[iter]:
    words = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Üniversite\w+',SAMPLE_TEXT[iter])
    for word in words:
        if word not in ORG_VAL and word[0] != ' ':
            print("Line "+ str(iter+1) + ": "  +  "ORGANIZATION "+ word)
            ORG_VAL.append(word)
"""
