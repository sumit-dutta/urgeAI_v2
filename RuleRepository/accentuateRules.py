import venv.RuleRepository.looksmashStandards as ls

####################################################Rules###################################

rules = {"accentuate":
            {
                "arms" : ["Sleeves","Neck","Sub_category"],
                "bust" : ["Neck","Sub_category"],
                "legs" : ["Sub_category", "Fit", "Length"],
                "waist" : ["Sub_category"]

            }
        }



####################################################Scores######################################


scores = {
          "arms":{},
          "bust":{},
          "legs": {},
          "waist": {}
          }



##############arms#####################
scores["arms"] ={
                    ls.Sleeves.Half_Sleeves.value: .4,
                    ls.Sleeves.Sleeveless.value: 1,
                    ls.Sleeves.Cap_Sleeves.value: .8,
                    ls.Sleeves.Puff_Sleeves.value: .8,
                    #ls.Sleeves.Flutter_Sleeves.value: .6,
                    ls.Sleeves.Short_Sleeves.value: .6,
                    ls.Sleeves.Three_Fourth_Sleeves.value: .2,
                    ls.Neck.Halter_Neck.value: .6,
                    ls.Sub_Category.Off_Shoulder_Dresses.value: .8,
                    ls.Sub_Category.Tank_Tops.value: 1,
                    ls.Sub_Category.Strappy_Tops.value: 1
                }


###############bust################

scores["bust"] = {
            ls.Neck.V_Neck.value: .8,
            ls.Neck.Spaghetti_Neck.value: 1,
            ls.Neck.Sweetheart_Neck.value: 1,
            ls.Sub_Category.Tube_Tops.value: .8,
            ls.Neck.Halter_Neck.value: .8,
            ls.Neck.Boat_Neck.value: .4,
            ls.Neck.Henley.value: .6,
            ls.Neck.Square_Neck.value: .6,
            ls.Sub_Category.Polo_T_shirts.value: .6,
            ls.Sub_Category.Bodycon_Dresses.value: .4

        }


####################legs#################

scores["legs"] =  {
            'Jeggings': .8,
            'Shorts': 1,
            'Skinny Fit': .3,
            'Slim Fit': .4,
            'Pencil': 1,
            'Mini': 1,
            ls.Sub_Category.Midis.value: .8,
            ls.Sub_Category.Asymmetric_Dresses.value: .6,
            ls.Sub_Category.Jumpsuit.value: 1,
            ls.Sub_Category.Shift_Dresses.value: .6,
            ls.Sub_Category.Bodycon_Dresses.value: .6,
            ls.Sub_Category.Peplum_Dresses.value: .6,
            ls.Sub_Category.Palazzos.value: .6,
            ls.Sub_Category.Leggings.value: .6,
            ls.Sub_Category.Beach_Shorts.value: 1,
            ls.Sub_Category.Three_Fourth_Shorts.value: .6

        }




############waist################

scores["waist"] = {
            ls.Sub_Category.Peplum_Dresses.value: 1,
            ls.Sub_Category.Bodycon_Dresses.value: .8,
            #'Empire Waist': .8,
            #'Wrap': .6,
            ls.Sub_Category.Maxis.value: .6,
            #'Fit and Flare': 1,
            #'Bandage': .8,
            ls.Sub_Category.Skater_Dresses.value: .8,
            ls.Sub_Category.Anarkali.value: 1,
            ls.Sub_Category.Jumpsuit.value: .6,
            ls.Sub_Category.Crop_Tops.value: 1,
            ls.Sub_Category.Anarkali_Gown.value: .6,
            ls.Sub_Category.Ethnic_Jackets.value: .4
        }

