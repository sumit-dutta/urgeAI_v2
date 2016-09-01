import venv.DatabaseLayer.converseWithDB as cdb
import venv.DatabaseLayer.converseWithStandards as cstd
import venv.RuleRepository.looksmashStandards as ls
import venv.RuleRepository.skinToneRules as sk
import venv.DatabaseLayer.dataNormalization as dn
import random




#print cdb.getColumnValuesForDomain("looksmash_db", "looksmash_women","Type", "Jabong")
#
# cdb.renameFieldInDocument("looksmash_rules", "rules", "arms.3/4 sleeves", "arms.3/4th Sleeves")
#
test = cstd.getStandardValues("looksmash_standards","attributes", "Type")
print test

# print random.randint(0,0)
#
# test = [1,1,3,44,5,6,7,5,3,2,1,2,3,4,5,6,7,4,3]
#
# group = {}
#
# for value in test:
#     if value not in group.keys():
#         group[value] = {
#             "test":[]
#         }
#
#     group[value]["test"].append(value)
#
#
# print group.keys()
#
# sub_categories_dict = dict.fromkeys(['a', 'b'], ls.Sub_Category.Sport_Shoes.value)
# print sub_categories_dict
# del group[1][1]
# print group
#
# cdb.getSchemaDetails("looksmash_db", "looksmash_women")

# shorts_data = cdb.getSubCategoryDataFromDomain("looksmash_db", "looksmash_women", "Jabong",ls.Sub_Category.Shorts.value, ls.Sub_Category.Beach_Shorts.value, ls.Sub_Category.Chino_Shorts.value, ls.Sub_Category.Three_Fourth_Shorts.value)
#
# for doc in shorts_data:
#     doc = dn.normalize_data(doc)
#     cdb.replaceDocument("looksmash_db", "looksmash_women", doc)