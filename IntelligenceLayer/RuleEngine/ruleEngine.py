import RuleRepository.accentuateRules as rp
import RuleRepository.skinToneRules as sk
#import RuleRepository.productPairingRules as pp


def computeScore(record, rules, scores, preference, bodyPart):
    score = 0
    count = 0
    for attr in rules[preference][bodyPart]:
        if attr in record.keys() and record[attr] in scores[bodyPart].keys():
            print scores[bodyPart][record[attr]]
            score = score + float(scores[bodyPart][record[attr]])
            count = count + 1
            #print attr, score
    if count==0:
        count = count + 1
    return score/count




def computeAccentuateScores(record, userPrefs, scores = rp.scores, rules = rp.rules,):

    score  = 0
    msg = ''
    if userPrefs["accentuate"]["arms"]:
         curScore =  computeScore(record, rules, scores, "accentuate", "arms")
         if curScore > 0:
            score = score + computeScore(record, rules, scores, "accentuate", "arms")
            msg = msg + 'AA'
    if userPrefs["accentuate"]["bust"]:
         curScore =  computeScore(record, rules, scores, "accentuate", "bust")
         if curScore > 0:
            score = score + computeScore(record, rules, scores, "accentuate", "bust")
            msg = msg + 'AB'
    if userPrefs["accentuate"]["legs"]:
         curScore =  computeScore(record, rules, scores, "accentuate", "legs")
         if curScore > 0:
            score = score + computeScore(record, rules, scores, "accentuate", "legs")
            msg = msg + 'AL'
    if userPrefs["accentuate"]["waist"]:
         curScore = computeScore(record, rules, scores, "accentuate", "waist")
         if curScore > 0:
            score = score + computeScore(record, rules, scores, "accentuate", "waist")
            msg = msg + 'AW'

    return score, msg


def computeSkinToneScores(record, skinTone, colors, scores = sk.scores):
    score = 0
    count = 0
    for color in record["Color"]:
        if color in diff(scores[skinTone].keys(), colors):
            score = 1
    return score,"SK"


#old logic
# score = score + scores[skinTone][color]
# count = count + 1
#
# if count==0:
#     count = count + 1
# return score/count



def computeColorScores(record, colors):
    score = 0
    count = 0
    for color in colors:
        if color in record["Color"]:
            score = 1

    return score,"C"

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

# def computeProductPairingColorScore(record1, record2):
#     return pp.scores['Color'][record1['Category']][record2['Category']][record1['Color']][record2['Color']]
#
# def computeProductPairingTypeScore(record1, record2):
#     print pp.scores['Type'][record1['Sex']]
#     print pp.scores['Type'][record1['Sex']][record1['Category']][record2['Category']]
#     return pp.scores['Type'][record1['Sex']][record1['Category']][record2['Category']][record1['Sub_category']][record2['Sub_category']]
#
# def computeProductPairingPatternScore(record1, record2):
#     return pp.scores['Pattern'][record1['Category']][record2['Category']][record1['Pattern']][record2['Pattern']]
#
#
#
# def computeProductPairingScores(record1, record2):
#     if record2['Category'] in pp.pairingCycle[record1['Category']]:
#         return computeProductPairingColorScore(record1, record2) + computeProductPairingTypeScore(record1, record2) + computeProductPairingPatternScore(record1, record2)
#
#
# record1 = {"_id":{"$oid":"570f30d704079a789d8b2d7c"},"Category":"Topwear","Pattern":"Checks","Neck":"COLLAR","Fit":"Slim","Url":"http://www.jabong.com/Wills-Lifestyle-Green-Casual-Shirt-770832.html?pos=2101","Type":"","Sub_category":"Casual Shirts","Color":"Green","Image":"http://static4.jassets.com/p/Wills-Lifestyle-Green-Casual-Shirt-5523-238077-1-pdp_slider_l.jpg","Sex":"Men","Cost":"1689","Sleeves":"Full Sleeves","Product Name":"Green Casual Shirt","Brand":"Wills Lifestyle","Size":["39","40","42","44"]}
# record2 = {"_id":{"$oid":"570f30d704079a789d8b2d7c"},"Category":"Bottomwear","Pattern":"Solids","Neck":"COLLAR","Fit":"Slim","Url":"http://www.jabong.com/Wills-Lifestyle-Green-Casual-Shirt-770832.html?pos=2101","Type":"","Sub_category":"Jeans","Color":"Black","Image":"http://static4.jassets.com/p/Wills-Lifestyle-Green-Casual-Shirt-5523-238077-1-pdp_slider_l.jpg","Sex":"Men","Cost":"1689","Sleeves":"Full Sleeves","Product Name":"Green Casual Shirt","Brand":"Wills Lifestyle","Size":["39","40","42","44"]}
#
#
# print computeProductPairingScores(record1, record2)



