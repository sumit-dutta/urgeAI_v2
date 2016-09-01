# from looksmashStandards import Colors
# from looksmashStandards import Gender
# from looksmashStandards import Category
# from looksmashStandards import Type
# from looksmashStandards import Pattern
#
#
# pairingCycle = {
#                 Category.Topwear.value: [Category.Bottomwear.value],
#                 Category.Bottomwear.value: [Category.Footwear.value, Category.Topwear.value],
#                 Category.Footwear.value: [Category.Bottomwear.value]
#
# }
#
# scores = {
#             "Color": {},
#             "Type" : {},
#             "Pattern": {}
# }
#
#
#
# scores["Color"] = {
#                     Category.Topwear.value: {
#                                     Category.Bottomwear.value:{
#                                                     Colors.Blue.value: {
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Navy_Blue.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Red.value: .5
#
#                                                     },
#                                                     Colors.Grey.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Peach.value: .5,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Indigo.value: .5,
#                                                                 Colors.Yellow.value: .5,
#                                                                 Colors.Mauve.value: .5
#                                                     },
#                                                     Colors.Black.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Khaki.value: .5
#
#                                                     },
#                                                     Colors.Navy_Blue.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Emerald_Green.value: .5,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Yellow.value: .5
#
#                                                     },
#                                                     Colors.White.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Mauve.value: .5
#                                                     },
#                                                     Colors.Red.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Blue.value: .5
#                                                     },
#                                                     Colors.Green.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Khaki.value: .5,
#                                                                 Colors.White.value: .5
#                                                     },
#                                                     Colors.Yellow.value: {
#                                                                 Colors.Blue.value:1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Black.value: .5,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Olive.value: .5
#
#                                                     },
#                                                     Colors.Brown.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Black.value: .5,
#                                                                 Colors.Navy_Blue.value: .5
#                                                     },
#                                                     Colors.Maroon.value: {
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Navy_Blue.value: .5,
#                                                                 Colors.Blue.value: .5
#                                                     },
#                                                     Colors.Pink.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Khaki.value: 1
#
#                                                     },
#                                                     Colors.Purple.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Tan.value: .5
#
#                                                     },
#                                                     Colors.Beige.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Orange.value: .5
#                                                     },
#                                                     Colors.Orange.value: {
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Navy_Blue.value: 1
#                                                     },
#                                                     Colors.Cream.value: {
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Peach.value: .5,
#                                                                 Colors.Khaki.value: .5,
#                                                                 Colors.Olive.value: .5
#                                                     },
#                                                     Colors.Olive.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Cream.value: .5,
#                                                                 Colors.White.value: .5
#                                                     },
#                                                     Colors.Khaki.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Grey.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Tan.value: .5
#                                                     },
#                                                     Colors.Peach.value: {
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Navy_Blue.value: .5,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Black.value: .5
#                                                     },
#                                                     Colors.Silver.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1
#                                                     },
#                                                     Colors.Golden.value: {
#                                                                 Colors.Black.value: 1
#                                                     },
#                                                     Colors.Tan.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1
#                                                     },
#                                                     Colors.Magenta.value: {
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Blue.value: .5
#                                                     },
#                                                     Colors.Turquoise.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1
#
#                                                     },
#                                                     Colors.Copper.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Green.value: .5,
#                                                                 Colors.Mustard.value: .5
#
#                                                     },
#                                                     Colors.Mauve.value: {
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: .5,
#                                                                 Colors.Green.value: .5,
#                                                                 Colors.Emerald_Green.value: .5
#                                                     },
#                                                     Colors.Mustard.value: {
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Black.value: .5
#                                                     },
#                                                     Colors.Nude.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Olive.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Khaki.value: .5
#                                                     },
#                                                     Colors.Scarlet.value: {
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Brown.value: 1
#
#                                                     },
#                                                     Colors.Plum.value: {
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Grey.value: .5,
#                                                                 Colors.White.value: .5,
#                                                                 Colors.Cream.value: .5
#                                                     },
#                                                     Colors.Emerald_Green.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Peach.value: .5
#                                                     },
#                                                     Colors.Lime_Green.value: {
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Grey.value: .5,
#                                                                 Colors.Brown.value: .5
#                                                     },
#                                                     Colors.Indigo.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Peach.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Yellow.value: .5
#                                                     }
#
#
#
#                                     }
#                     },
#                     "Bottomwear": {
#                                     "Topwear": {
#                                                     Colors.Blue.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Yellow.value: .5,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Turquoise.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Scarlet.value: .5
#
#
#                                                     },
#                                                     Colors.Grey.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Scarlet.value: .5,
#                                                                 Colors.Plum.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Orange.value: .5
#
#
#                                                     },
#                                                     Colors.Black.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#
#
#                                                     },
#                                                     Colors.Navy_Blue.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Mauve.value : 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Green.value: .5,
#                                                                 Colors.Navy_Blue.value: .5,
#                                                                 Colors.Turquoise.value: .5,
#                                                                 Colors.Khaki.value: .5,
#                                                                 Colors.Brown.value: .5
#                                                     },
#                                                     Colors.White.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Red.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Peach.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Indigo.value: .5
#                                                     },
#                                                     Colors.Green.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Blue.value: .5,
#                                                                 Colors.Olive.value: .5
#                                                     },
#                                                     Colors.Yellow.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: .5
#
#                                                     },
#                                                     Colors.Brown.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Indigo.value: .5,
#                                                                 Colors.Mauve.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Yellow.value: .5,
#                                                                 Colors.Black.value: .5,
#                                                                 Colors.Blue.value: .5,
#                                                                 Colors.Navy_Blue.value: .5
#
#                                                     },
#                                                     Colors.Maroon.value: {
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Emerald_Green.value: .5,
#                                                                 Colors.Indigo.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Olive.value: .5,
#                                                                 Colors.Khaki.value: .5
#                                                     },
#                                                     Colors.Pink.value: {
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Maroon.value: .5,
#                                                                 Colors.Scarlet.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Red.value: .5,
#
#
#
#                                                     },
#                                                     Colors.Purple.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Yellow.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Olive.value: .5
#
#                                                     },
#                                                     Colors.Beige.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Orange.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Turquoise.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Khaki.value: .5,
#                                                                 Colors.Copper.value: .5
#
#                                                     },
#                                                     Colors.Cream.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Olive.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Red.value:.5,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Indigo.value: .5,
#                                                                 Colors.Orange.value: .5
#
#                                                     },
#                                                     Colors.Khaki.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Scarlet.value: .5,
#                                                                 Colors.Plum.value: .5,
#                                                                 Colors.Black.value: .5,
#                                                                 Colors.Emerald_Green.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Purple.value: .5
#                                                     },
#                                                     Colors.Peach.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Olive.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Scarlet.value: .5,
#                                                                 Colors.Nude.value: .5
#                                                     },
#                                                     Colors.Silver.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Golden.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Tan.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Orange.value: 1
#
#
#                                                     },
#                                                     Colors.Magenta.value: {
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Maroon.value: .5,
#                                                                 Colors.Scarlet.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Tan.value: .5
#                                                     },
#                                                     Colors.Turquoise.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Tan.value: .5
#
#                                                     },
#                                                     Colors.Copper.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#
#                                                     },
#                                                     Colors.Mauve.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Yellow.value: .5,
#                                                                 Colors.Emerald_Green.value: .5
#                                                     },
#                                                     Colors.Mustard.value: {
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Nude.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5
#                                                     },
#                                                     Colors.Nude.value: {
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#                                                     },
#                                                     Colors.Scarlet.value: {
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Red.value: .5,
#                                                                 Colors.Pink.value: .5,
#                                                                 Colors.Magenta.value: .5
#
#                                                     },
#                                                     Colors.Plum.value: {
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Magenta.value: .5,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Plum.value: .5,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Copper.value: .5,
#                                                                 Colors.Golden.value: .5
#
#
#                                                     },
#                                                     Colors.Emerald_Green.value: {
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Blue.value: .5,
#                                                                 Colors.Orange.value: .5,
#                                                                 Colors.Mustard.value: .5,
#                                                                 Colors.Yellow.value: .5
#
#
#                                                     },
#                                                     Colors.Lime_Green.value: {
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value:1,
#                                                                 Colors.Beige.value: .5,
#                                                                 Colors.Brown.value: .5,
#                                                                 Colors.Tan.value: .5,
#                                                                 Colors.Maroon.value: .5
#
#                                                     },
#                                                     Colors.Indigo.value: {
#
#                                                                 Colors.Blue.value: 1,
#                                                                 Colors.Grey.value: 1,
#                                                                 Colors.Black.value: 1,
#                                                                 Colors.Navy_Blue.value: 1,
#                                                                 Colors.White.value: 1,
#                                                                 Colors.Red.value: 1,
#                                                                 Colors.Green.value: 1,
#                                                                 Colors.Yellow.value: 1,
#                                                                 Colors.Brown.value: 1,
#                                                                 Colors.Maroon.value: 1,
#                                                                 Colors.Pink.value: 1,
#                                                                 Colors.Purple.value: 1,
#                                                                 Colors.Beige.value: 1,
#                                                                 Colors.Orange.value: 1,
#                                                                 Colors.Cream.value: 1,
#                                                                 Colors.Olive.value: 1,
#                                                                 Colors.Khaki.value: 1,
#                                                                 Colors.Peach.value: 1,
#                                                                 Colors.Silver.value: 1,
#                                                                 Colors.Golden.value: 1,
#                                                                 Colors.Tan.value: 1,
#                                                                 Colors.Magenta.value: 1,
#                                                                 Colors.Turquoise.value: 1,
#                                                                 Colors.Copper.value: 1,
#                                                                 Colors.Mauve.value: 1,
#                                                                 Colors.Mustard.value: 1,
#                                                                 Colors.Nude.value: 1,
#                                                                 Colors.Scarlet.value: 1,
#                                                                 Colors.Plum.value: 1,
#                                                                 Colors.Emerald_Green.value: 1,
#                                                                 Colors.Lime_Green.value: 1,
#                                                                 Colors.Indigo.value: 1,
#                                                                 Colors.Coffee.value: 1,
#                                                                 Colors.Multicolor.value: 1
#
#
#                                                     }
#
#                                     }
#                     }
# }
#
#
# scores["Type"] = {
#                     Gender.Men.value: {
#                                         Category.Topwear.value: {
#                                                                 Category.Bottomwear.value: {
#                                                                                         Type.Casual_Shirts.value: {
#                                                                                                 Type.Jeans.value: 1,
#
#                                                                                          },
#                                                                                         Type.Shirts.value: {
#                                                                                                 Type.Trousers.value:1,
#                                                                                                 Type.Formal_Trousers.value:1
#                                                                                         },
#                                                                                         Type.Formal_Shirts.value: {
#                                                                                                 Type.Trousers.value:1,
#                                                                                                 Type.Formal_Trousers.value:1
#                                                                                         },
#                                                                                         Type.Tees.value:{
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Shorts.value:1
#                                                                                         }
#
#                                                                 }
#                                         }
#
#
#
#                     },
#                     Gender.Women.value: {
#                                         Category.Topwear.value: {
#                                                                 Category.Bottomwear.value: {
#                                                                                         Type.Casual_Shirts.value: {
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Jeggings.value:1
#                                                                                         },
#                                                                                         Type.Shirts.value: {
#                                                                                                 Type.Formal_Trousers.value:1,
#                                                                                                 Type.Skirts.value:1,
#                                                                                                 Type.Trousers.value:1
#                                                                                         },
#                                                                                         Type.Tops.value: {
#                                                                                                 Type.Skirts.value:1,
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Jeggings.value:1
#                                                                                         },
#                                                                                         Type.Tees.value: {
#                                                                                                 Type.Jeggings.value:1,
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Shorts.value:1
#
#                                                                                         },
#                                                                                         Type.Shirts_And_Blouses.value: {
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Jeggings.value:1,
#                                                                                                 Type.Skirts.value:1
#                                                                                         },
#                                                                                         Type.Kurtas.value: {
#                                                                                                 Type.Ethnic_Bottomwear.value:1
#                                                                                         },
#                                                                                         Type.Tunics.value: {
#                                                                                                 Type.Jeans.value:1,
#                                                                                                 Type.Jeggings.value: 1
#                                                                                         }
#
#                                                                 }
#
#
#                                         }
#
#                     }
#
# }
#
# scores["Pattern"] = {
#                         Category.Topwear.value: {
#                                                 Category.Bottomwear.value:{
#                                                                             Pattern.Solids.value: {
#                                                                                     Pattern.Florals.value: 1,
#                                                                                     Pattern.Stripes.value:1,
#                                                                                     Pattern.Acid_Wash.value: 1,
#                                                                                     Pattern.Embroidered.value: 1,
#                                                                                     Pattern.Printed.value: 1
#                                                                             },
#                                                                             Pattern.Florals.value:{
#                                                                                     Pattern.Solids.value: 1,
#                                                                                     Pattern.Acid_Wash.value: 1,
#                                                                                     Pattern.Florals.value: 1
#                                                                             },
#                                                                             Pattern.Stripes.value:{
#                                                                                     Pattern.Solids.value: 1
#                                                                             },
#                                                                             Pattern.Checks.value:{
#                                                                                     Pattern.Solids.value:1
#                                                                             },
#                                                                             Pattern.Embroidered.value:{
#                                                                                     Pattern.Solids.value:1
#                                                                             },
#                                                                             Pattern.Graphic_Print.value:{
#                                                                                     Pattern.Solids.value:1
#                                                                             },
#                                                                             Pattern.Printed.value:{
#                                                                                     Pattern.Acid_Wash.value:1,
#                                                                                     Pattern.Solids.value:1
#                                                                             },
#                                                                             Pattern.Acid_Wash.value:{
#                                                                                     Pattern.Solids.value:1,
#                                                                                     Pattern.Acid_Wash.value:1,
#                                                                                     Pattern.Florals.value:1
#                                                                             },
#                                                                             Pattern.Geometric_Print.value:{
#                                                                                     Pattern.Solids.value:1
#                                                                             }
#                                                 }
#                         }
# }
#
# print(scores)