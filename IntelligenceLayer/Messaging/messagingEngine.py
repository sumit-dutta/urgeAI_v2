
messages = dict.fromkeys(["AAABALAWCSK", "AAABALCSK", "AAABCSK", "ABALAWCSK", "ALAWCSK", "AAALAWCSK", "AAAWCSK", "AAABAWCSK", "ABAWCSK", "AAALCSK", "ABALC", "AAABALAWC", "AAABALC", "AAABC", "ABALAWC", "ALAWC", "AAALAWC", "AAAWC", "AAABAWC", "ABAWC", "AAALC", "ABALC"], ["Best match for your Personal Style"])
messages.update(dict.fromkeys(["AAABALAWSK", "AAABALSK", "AAABSK", "ABALAWSK", "ALAWSK", "AAALAWSK", "AAAWSK", "AAABAWSK", "ABAWSK", "AAALSK", "ABALSK"], ["Complements your skin tone & Physical Features"]))
messages.update(dict.fromkeys(["AACSK", "AAC"], ["Accentuates your Arms & Matches Your Color Choices"]))
messages.update(dict.fromkeys(["ABCSK", "ABC"], ["Accentuates Bust &  Matches Your Color Choices"]))
messages.update(dict.fromkeys(["ALCSK", "ALC"], ["Accentuates Legs & Matches Your Color Choices"]))
messages.update(dict.fromkeys(["AWCSK", "AWC"], ["Accentuates Arms & Complements Your Skin Tone"]))
messages.update(dict.fromkeys("AA", ["Shows off your Arms"]))
messages.update(dict.fromkeys("AB", ["Accentuates your Bust"]))
messages.update(dict.fromkeys("AL", ["Shows off your Legs"]))
messages.update(dict.fromkeys("AW", ["Shows off your Waist"]))
messages.update(dict.fromkeys(["C", "CSK"], ["Matches Your Color Preferences"]))
messages.update(dict.fromkeys("SK", ["Complements Your Skin Tone"]))

def getMsg(msgCode):
    return messages[msgCode]

print messages