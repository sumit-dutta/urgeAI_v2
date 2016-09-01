import venv.IntelligenceLayer.RuleEngine.ruleEngine as re
import venv.Utilities.RulesUtils.ruleUtils as ru
import venv.DatabaseLayer.dataNormalization as dn
import venv.DatabaseLayer.converseWithDB as cdb
import venv.RuleRepository.looksmashStandards as ls
import venv.IntelligenceLayer.Messaging.messagingEngine as me
import json
from operator import itemgetter
import itertools
import urllib, cStringIO
import random
import json





#print re.computeAccentuateScores(data, userPrefs)




# with open('../DataFiles/jabong_data.json', 'rb') as f:
#     data = f.readlines()
#
# data = map(lambda x: x.rstrip(), data)
# data_json_str = "[" + ','.join(data) + "]"
#
# data = json.loads(data_json_str)





# for doc in data:
#
#     score =  re.computeAccentuateScores(dn.normalize_data(doc), userPrefs)
#     if score>0:
#         print doc
#         print score


def getCategoryValueIndex(value, grouped_data, category):
    ind = -1
    if len(grouped_data[value][category])>0 and float(value) > 0:
        ind = random.randint(0,len(grouped_data[value][category])-1)
    return ind


def testFeed(userprefs):
    print userprefs

    accentuateWeight = .7
    colorWeight = .5
    skinToneWeight = .1
    scores = cdb.getFullData("looksmash_rules", "rules")[0]





    bodyPrefs = {
        "accentuate": {
            "arms": False,
            "bust": False,
            "waist": False,
            "legs" : False
        }
    }

    for bodyPart in userprefs["accentuate"]:
        bodyPrefs["accentuate"][bodyPart] = True

    colors = userprefs['colors']
    types = userprefs['types']
    skinTone = userprefs['skinTone']




    jabong_data =  cdb.getFullDataWithColorsAndTypesFromDomain("looksmash_db", "looksmash_women", "Jabong", ru.getColorList(colors,skinTone), types)
    scored_data = []
    grouped_data = {}
    for doc in jabong_data:
        doc = dn.normalize_data(doc)
        accentuateScore, accentuateMsg = re.computeAccentuateScores(doc, bodyPrefs, scores)
        colorScore, colorMsg = re.computeColorScores(doc, colors)
        skinToneScore, skinToneMsg = re.computeSkinToneScores(doc,skinTone,colors)
        doc['score'] = accentuateWeight*accentuateScore + colorWeight*colorScore + skinToneWeight*skinToneScore
        doc['msg'] = me.getMsg(accentuateMsg + colorMsg + skinToneMsg)
        #print doc
        if doc['score'] not in grouped_data.keys():
            grouped_data[doc['score']] = {
                ls.Category.Topwear.value : [],
                ls.Category.Bottomwear.value : [],
                ls.Category.Footwear.value : []
            }

        del doc['_id']
        grouped_data[doc['score']][doc['Category']].append(doc)
        scored_data.append(doc)


    feed = []

    json.dump(grouped_data, open("grouped.txt",'w'))
    sorted_keys = grouped_data.keys()
    sorted_keys.sort(reverse=True)

    if 0.5 in sorted_keys:
        limInd = sorted_keys.index(0.5)
    else:
        limInd = len(sorted_keys)/2

    for i in range(0,100):
        for index, value in enumerate(sorted_keys):
            #print value, index
            if index > limInd:
                #print "breaking..!"
                break;
            ind = getCategoryValueIndex(value, grouped_data, ls.Category.Topwear.value)
            if ind >= 0:
                feed.append(grouped_data[value][ls.Category.Topwear.value][ind])
                #print grouped_data[value][ls.Category.Topwear.value][ind]
                del grouped_data[value][ls.Category.Topwear.value][ind]

            ind = getCategoryValueIndex(value, grouped_data, ls.Category.Bottomwear.value)
            if ind >= 0:
                feed.append(grouped_data[value][ls.Category.Bottomwear.value][ind])
                #print grouped_data[value][ls.Category.Bottomwear.value][ind]
                del grouped_data[value][ls.Category.Bottomwear.value][ind]

            ind = getCategoryValueIndex(value, grouped_data, ls.Category.Footwear.value)
            if ind >= 0:
                feed.append(grouped_data[value][ls.Category.Footwear.value][ind])
                #print grouped_data[value][ls.Category.Footwear.value][ind]
                del grouped_data[value][ls.Category.Footwear.value][ind]


        if limInd > len(sorted_keys):
            limInd = 0
        else:
            limInd = limInd + 1

    print sorted_keys

    print feed

    images = {}
    i=0
    for product in feed:
        images[i]={"image" :product["Image"],
                   "msg" : product["msg"],
                   "url" : product["Url"]
                   }
        i = i+1

    return {"result": json.dumps(images)}




def normalizeDB():
    women_data =  cdb.getFullData("looksmash_db", "looksmash_women")

    for doc in women_data:
        dn.normalize_data(doc)


    men_data =  cdb.getFullData("looksmash_db", "looksmash_men")
    for doc in men_data:
        dn.normalize_data(doc)

    return "done"


    #cdb.printColVals("Sub_category")

#
#
# with open('../DataFiles/snapdeal_data.json', 'rb') as f:
#     data = f.readlines()
#
# data = map(lambda x: x.rstrip(), data)
# data_json_str = "[" + ','.join(data) + "]"
#
# data = json.loads(data_json_str)
#
#
#
#
#
# scored_data = []
# for curDoc in data:
#
#         if curDoc['Sex'] != "Men":
#             doc = dn.normalize_data(curDoc)
#
#             doc['score'] = re.computeAccentuateScores(doc, userPrefs) + re.computeSkinToneScores(doc, "fair") + re.computeColorScores(doc, colors)
#             #print doc
#             scored_data.append(doc)
#
# sorted_data = sorted(scored_data, key=itemgetter('score'), reverse=True)
#
#
# top10 = itertools.islice(sorted_data, 10)
#
# print "Result"
#
# for doc in top10:
#     print doc
#     file = cStringIO.StringIO(urllib.urlopen(doc["Image"]).read())
#     img = Image.open(file)
#     img.show()