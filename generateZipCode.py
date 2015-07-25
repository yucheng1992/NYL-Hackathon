from pyzipcode import ZipCodeDatabase
import pandas as pd
import random

def generateLatitudeLongitude(zipCode):
    '''
    Generate the longitude and latitude according to the zipcode.
    '''
    zcdb = ZipCodeDatabase()
    try :
        zipCodeInfo = zcdb[int(zipCode)]
        latitude = zipCodeInfo.latitude
        longitude = zipCodeInfo.longitude
        return (longitude, latitude)
    except:
        pass 

def readDataFromExcel(fileName):
    """Read data from excel file."""
    user_data = pd.read_excel(fileName)
    user_data_zip = user_data[["ZIP"]]
    return  user_data_zip

def assignRandomZipCode(df):
    random.seed(2)
    geo_info = map(generateLatitudeLongitude, df["ZIP"])
    geo_unique = list(set(geo_info))
    geo_unique.remove(None)
    length = len(geo_unique)
    new_geo_info = []
    for item in geo_info:
        if item == None:
            random_number = random.randint(0, length - 1)
            new_geo_info.append(geo_unique[random_number])
        else:
            new_geo_info.append(item)
    return new_geo_info

def addColumnsToDataFrame(df, geo_info):
    longitude = [pair[0] for pair in geo_info]
    latitude = [pair[1] for pair in geo_info]
    df["LONGITUDE"] = longitude
    df["LATITUDE"] = latitude
    return df[["ZIP", "LONGITUDE", "LATITUDE"]]

if __name__ == '__main__':
    df = readDataFromExcel("data/Software_Requirment_Brief_Heat.xls")
    geo_info = assignRandomZipCode(df)
    print addColumnsToDataFrame(df, geo_info)
