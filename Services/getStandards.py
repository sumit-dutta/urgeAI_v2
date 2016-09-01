import venv.DatabaseLayer.converseWithStandards as cstd


def getColors():
    return cstd.getStandardValues("looksmash_standards","attributes", "Color")


def getTypes():
    return cstd.getStandardValues("looksmash_standards","attributes", "Type")


