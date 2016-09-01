import DatabaseLayer.converseWithDB as cdb
import RuleRepository.normalizationRules as nr
import json


getDict = {
    "Sub_category": nr.sub_categories_dict,
    "Pattern": nr.patterns_dict,
    "Neck": nr.necks_dict,
    "Sleeve": nr.sleeves_dict

}

def getLooksmashValues(category):
    print "==============================", category, "==================================="
    sub_categories = getDict[category]
    looksmash_categories = []
    for cat in sub_categories:
        looksmash_categories.extend(cat.values())

    return list(set(looksmash_categories))


def getDBValues(category, domain):
    dbValues = cdb.getColumnValues("looksmash_normalized", domain+"_normalized", category)
    return dbValues


def testNormalization(category, domain):
    dbValues = getDBValues(category, domain)
    looksmashValues = getLooksmashValues(category)
    print dbValues
    print looksmashValues

    print "Testing ",category," values in ",domain

    for value in dbValues:
        if value in looksmashValues:
            print "Success"
        else:
            print "Error Value ",value," not present in looksmash values"



def startTest(category):
    testNormalization(category, "flipkart")
    #testNormalization(category, "jabong")
    #testNormalization(category, "snapdeal")

startTest("Sub_category")
startTest("Neck")
startTest("Sleeve")
startTest("Pattern")
























sports_shoes = ["Sports Shoes", "Sports Shoes", "Sneakers", ]
mens_accessories = ["Necktie", ]
floaters = ["Floater Sandal", ]
bags = ["Hand Bags", "Womens Handbags", ]
casual_jackets = ["Jackets", ]
shirts_and_blouses = ["Shirts & Blouses", ]
suits = ["Suits", "Suits & Blazers", "Suits & Blazers", ]
loafers = ["Loafers", ]
boots = ["Boots", ]
trousers = ["Trousers", "Trousers", "Trousers", "Trousers", ]
earrings = ["Earrings", "Earrings", ]
chains = ["Chains", ]
dresses = ["Dresses", ]
clutches = ["Clutches", "Clutches", ]
sunglasses = ["Sunglasses", ]
shorts = ["Shorts", "Shorts & 3/4ths", ]
tops = ["Tops", "Tops", "Tops", ]
ballet_flats = ["Ballerinas", ]
bracelets = ["Bangles & Bracelets", "Bangles & Bracelets", ]
neck_pieces = ["Necklaces & Sets", "Necklaces & Necklace Sets", ]
scarves = ["Stoles & Scarves", ]
tees = ["Polo T Shirts", "Tees & Polos", "Polos & T-Shirts", "Polos & Tees", "Tees", ]
waistcoats = ["Waistcoats", ]
casual_shoes = ["Casual Shoes", "Casual Shoes", ]
dupattas = ["Dupattas", ]
formal_shirts = ["Formal Shirts", "Formal Shirts", ]
jeggings = ["Jeggings", ]
kurtas = ["Kurtis", "Kurtas", "Kurtas & Kurtis", ]
tunics = ["Tunics & More", ]
belts = ["Belts", "Belts", ]
sling_bag = ["Sling Bags", ]
formal_trousers = ["Formal Trousers", ]
flats = ["Flats", "Flat Slip-on & Sandal", ]
ethnic_wear = ["Ethnic Wear", ]
skirts = ["Skirts", ]
jeans = ["Jeans", "Denims & Jeggings", "Jeans", "Jeans", ]
watches = ["Watches", ]
formal_shoes = ["Formal Shoes", "Formal Shoes", ]
shirts = ["Shirts", "Shirts", "Shirts", ]
jackets = ["Blazers", "Winter Jackets", ]
sarees = ["Sarees", ]
ethnic_bottomwear = ["Salwars & Churidhars", "Salwars & Churidars", ]
casual_shirts = ["Casual Shirts", "Casual Shirts", ]


sub_categories_dict = dict.fromkeys(sports_shoes,"Sports Shoes")
sub_categories_dict.update(dict.fromkeys(mens_accessories,"Men Accessories"))
sub_categories_dict.update(dict.fromkeys(floaters, "Floaters"))
sub_categories_dict.update(dict.fromkeys(bags,"Bags"))
sub_categories_dict.update(dict.fromkeys(casual_jackets,"Casual Jackets"))
sub_categories_dict.update(dict.fromkeys(shirts_and_blouses,"Shirts And Blouses"))
sub_categories_dict.update(dict.fromkeys(suits,"Suits"))
sub_categories_dict.update(dict.fromkeys(loafers,"Loafers"))
sub_categories_dict.update(dict.fromkeys(boots,"Boots"))
sub_categories_dict.update(dict.fromkeys(trousers,"Trousers"))
sub_categories_dict.update(dict.fromkeys(earrings,"Earrings"))
sub_categories_dict.update(dict.fromkeys(chains,"Chains"))
sub_categories_dict.update(dict.fromkeys(dresses,"Dresses"))
sub_categories_dict.update(dict.fromkeys(clutches,"Clutches"))
sub_categories_dict.update(dict.fromkeys(sunglasses,"Sunglasses"))
sub_categories_dict.update(dict.fromkeys(shorts,"Shorts"))
sub_categories_dict.update(dict.fromkeys(tops,"Tops"))
sub_categories_dict.update(dict.fromkeys(ballet_flats,"Ballet Flats"))
sub_categories_dict.update(dict.fromkeys(bracelets,"Bracelets"))
sub_categories_dict.update(dict.fromkeys(neck_pieces,"Neck Pieces"))
sub_categories_dict.update(dict.fromkeys(scarves,"Scarves"))
sub_categories_dict.update(dict.fromkeys(tees,"Tees"))
sub_categories_dict.update(dict.fromkeys(waistcoats,"Waistcoats"))
sub_categories_dict.update(dict.fromkeys(casual_shoes,"Casual Shoes"))
sub_categories_dict.update(dict.fromkeys(dupattas,"Dupattas"))
sub_categories_dict.update(dict.fromkeys(formal_shirts,"Formal Shirts"))
sub_categories_dict.update(dict.fromkeys(jeggings,"Jeggings"))
sub_categories_dict.update(dict.fromkeys(kurtas,"Kurtas"))
sub_categories_dict.update(dict.fromkeys(tunics,"Tunics"))
sub_categories_dict.update(dict.fromkeys(belts,"Belts"))
sub_categories_dict.update(dict.fromkeys(sling_bag,"Sling Bags"))
sub_categories_dict.update(dict.fromkeys(formal_trousers,"Formal Trousers"))
sub_categories_dict.update(dict.fromkeys(flats,"Flats"))
sub_categories_dict.update(dict.fromkeys(ethnic_wear,"Ethnic Wear"))
sub_categories_dict.update(dict.fromkeys(skirts,"Skirts"))
sub_categories_dict.update(dict.fromkeys(jeans,"Jeans"))
sub_categories_dict.update(dict.fromkeys(watches,"Watches"))
sub_categories_dict.update(dict.fromkeys(formal_shoes,"Formal Shoes"))
sub_categories_dict.update(dict.fromkeys(shirts,"Shirts"))
sub_categories_dict.update(dict.fromkeys(jackets,"Jackets"))
sub_categories_dict.update(dict.fromkeys(sarees,"Sarees"))
sub_categories_dict.update(dict.fromkeys(ethnic_bottomwear,"Ethnic Bottomwear"))
sub_categories_dict.update(dict.fromkeys(casual_shirts,"Casual Shirts"))




#print sub_categories_dict

#
# data = cdb.getGenderData("looksmash_normalized", "jabong_normalized", "Women")
# normalized_data = []
#
# for doc in data:
#     print doc
#     print doc["Sub_category"], sub_categories_dict[doc["Sub_category"]]
#     cdb.updateDocument("looksmash_normalized", "jabong_normalized", doc["_id"], "Sub_category", sub_categories_dict[doc["Sub_category"]])
#



