import venv.RuleRepository.skinToneRules as sk


def getColorList(userPrefs, skintone, skinToneRules=sk.scores):
    print userPrefs+skinToneRules[skintone].keys()
    return userPrefs+skinToneRules[skintone].keys()