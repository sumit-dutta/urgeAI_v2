import pymongo

from pymongo import MongoClient


client = MongoClient('52.220.13.79', 27017)



def getColumnValues(dbName, collectionName, columnName):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({}, {columnName:1, "_id":0})
    values = []
    for doc in result:
        if columnName in doc.keys():
            values.append(doc[columnName])
    return list(set(values))


def getColumnValuesForDomain(dbName, collectionName, columnName, domain):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    result =  collection.find({"Domain":domain}, {columnName:1, "_id":0})
    values = []
    for doc in result:
        if columnName in doc.keys():
            values.append(doc[columnName])
    return list(set(values))


def getSchemaDetails(dbName, collectionName):
    print dbName, collectionName
    db = client[dbName]
    collection = db[collectionName]
    schematodo = collection.find_one()
    for key in schematodo:
        print key,type(key)




def printColVals(columnName):
    print columnName
    print "flipkart",getColumnValues("looksmash_normalized", "flipkart_normalized", columnName)
    print "jabong",getColumnValues("looksmash_normalized", "jabong_normalized", columnName)
    print "snapdeal",getColumnValues("looksmash_normalized", "snapdeal_normalized", columnName)




def getFullData(dbName, collectionName):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find()
    return result


def getGenderData(dbName, collectionName, gender):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Sex": gender})
    return result

def getFullDataFromDomain(dbName, collectionName, domain):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Domain": domain})
    return result


def getGenderDataFromDomain(dbName, collectionName, gender, domain):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Sex": gender, "Domain": domain})
    return result



def getCategoryData(dbName, collectionName, category):
    db = client[dbName]
    collection = db[collectionName]
    result = collection.find({"Category": category})
    return result

def getCategoryDataFromDomain(dbName, collectionName, domain, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for cat in category:
        condition = {"Category": cat}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList, "Domain": domain}
    result = collection.find(finalQuery)
    return result

def getSubCategoryDataFromDomain(dbName, collectionName, domain, *subCategory):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for cat in subCategory:
        condition = {"Sub_category": cat}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList, "Domain": domain}
    result = collection.find(finalQuery)
    return result



def getFullDataWithColors(dbName, collectionName, *colors):
    db = client[dbName]
    collection = db[collectionName]
    conditionList = []
    for color in colors:
        condition = {"Color": color}
        conditionList.append(condition)

    finalQuery = {"$or": conditionList}
    result = collection.find(finalQuery)
    return result


def getFullDataWithColorsAndCategory(dbName, collectionName, colors, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForCategory = []
    for color in colors:
        condition = {"Color": color}
        conditionListForColor.append(condition)

    for cat in category:
        condition = {"Category": cat}
        conditionListForCategory.append(condition)

    finalQuery = {"$or": conditionListForColor, "$or": conditionListForCategory}
    result = collection.find(finalQuery)
    return result


def getFullDataWithColorsAndCategoryFromDomain(dbName, collectionName, domain, colors, *category):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForCategory = []
    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for cat in category:
        condition = {"Category": cat}
        conditionListForCategory.append(condition)
    print conditionListForColor
    finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForCategory}, {"Domain": domain}]}
    print finalQuery
    result = collection.find(finalQuery)
    return result

def getFullDataWithColorsAndTypesFromDomain(dbName, collectionName, domain, colors, types):
    db = client[dbName]
    collection = db[collectionName]
    conditionListForColor = []
    conditionListForType = []
    for color in colors:
        condition = {"Color": {"$elemMatch":{"$eq":color}}}
        conditionListForColor.append(condition)

    for type in types:
        condition = {"Type": type}
        conditionListForType.append(condition)
    finalQuery = {"$and":[{"$or": conditionListForColor}, {"$or": conditionListForType}, {"Domain": domain}]}
    print finalQuery
    result = collection.find(finalQuery)
    return result



def updateDocument(dbName, collectionName, id, attribute, value):
    db = client[dbName]
    collection = db[collectionName]
    collection.update({"_id": id},
                      {
                        "$set" : {attribute:value}
                      }
                      )



def renameFieldInDocument(dbName, collectionName, field, newVal):
    db = client[dbName]
    collection = db[collectionName]
    collection.update({}, {"$rename":{field:newVal}}, False, True);





def replaceDocument(dbName, collectionName, document):
    print "Replacing Doc ->", document
    db = client[dbName]
    collection = db[collectionName]
    id = document["_id"]
    collection.replace_one({"_id": id}, document)





