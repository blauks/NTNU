from pymongo import MongoClient
import urllib.parse
#uname = urllib.parse.quote_plus('admin')
#pwd = urllib.parse.quote_plus('password')
client = MongoClient('mongodb://admin:123@it2810-15.idi.ntnu.no:27017/bomstasjoner')
db = client['bomstasjoner']
collection = db['bomstasjoner']
with open("bomstasjon.csv") as data_file:
    for index,line in enumerate(data_file):
        #print(line.split(","))
        line_data = line.split(";")
        #print(line_data)

        litenTakst = 0
        storTakst = 0

        if line_data[25] != "":
            litenTakst = int(line_data[25].split(".")[0])
        
        if line_data[26] != "":
            storTakst = int(line_data[26].split(".")[0])


        post = {
            "VEGOBJEKT-ID": line_data[0],
            "TYPE-ID": line_data[1],
            "VERSJON": line_data[2],
            "STARTDATO": line_data[3],
            "SLUTTDATO": line_data[4],
            "SIST MODIFISERT": line_data[5],
            "BOMPENGEANLEGG_ID": line_data[6],
            "BOMSTASJONSTYPE": line_data[7],
            "BOMSTASJON_ID": line_data[8],
            "EIER": line_data[9],
            "ETABLERINGSÅR": line_data[10],
            "GEOMETRI_PUNKT": line_data[11],
            "GRATIS_GJENNOMKJØRING_VED_HC-BRIKKE": line_data[12],
            "INNKREVNINGSRETNING": line_data[13],
            "LINK_TIL_BOMSTASJON": line_data[14],
            "NAVN_BOMPENGEANLEGG_FRA_CS": line_data[15],
            "NAVN_BOMSTASJON": line_data[16],
            "OPERATØR_ID": line_data[17],
            "PROSJEKTREFERANSE": line_data[18],
            "RUSHTID_ETTERMIDDAG_FRA": line_data[19],
            "RUSHTID_ETTERMIDDAG_TIL": line_data[20],
            "RUSHTID_MORGEN_FRA": line_data[21],
            "RUSHTID_MORGEN_TIL": line_data[22],
            "RUSHTIDSTAKST_LITEN_BIL": line_data[23],
            "RUSHTIDSTAKST_STOR_BIL": line_data[24],
            "TAKST_LITEN_BIL": litenTakst,
            "TAKST_STOR_BIL": storTakst,
            "TIDSDIFFERENSIERT_TAKST": line_data[27],
            "TILLEGGSINFORMASJON": line_data[28],
            "TIMESREGEL": line_data[29],
            "TIMESREGEL_PASSERINGSGRUPPE": line_data[30],
            "TIMESREGEL_VARIGHET": line_data[31],
            "VEDLIKEHOLDSANSVARLIG": line_data[32],
            "VEDTATT_TIL_ÅR": line_data[33],
            "KOMMUNE": line_data[34],
            "KOMMUNENUMMER": line_data[35],
            "FYLKE": line_data[36],
            "FYLKESNUMMER": line_data[37],
            "RIKSVEGRUTE": line_data[38],
            "KONTRAKTSOMRÅDE": line_data[39],
            "VEGSYSTEMREFERANSE": line_data[40],
            "VEGKATEGORI": line_data[41],
            "FASE": line_data[42],
            "VEGNUMMER": line_data[43],
            "STREKNING": line_data[44],
            "DELSTREKNING": line_data[45],
            "FRA_METER": line_data[46],
            "TIL_METER": line_data[47],
            "VEGLENKESEKVENSID": line_data[48],
            "STARTPOSISJON": line_data[49],
            "SLUTTPOSISJON": line_data[50],
            "RETNING": line_data[51],
            "SIDEPOSISJON": line_data[52],
            "GEOMETRI": line_data[53]
        }
        plane_id = collection.insert_one(post).inserted_id
        print(str(str(index) + ": " + str(plane_id)))