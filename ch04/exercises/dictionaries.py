#
#
text_tourism = "Thanks to a long history defined by major ancient civilizations, Peru is home to more than 5000 archaeological sites. Many of these remain shrouded in mystery, but are still capable of transporting visitors to the periods when such societies flourished. For example, a visit to Machu Picchu reveals the perfection of the Inca empire; this sacred city can be reached onboard the luxurious trains that run through imposing mountain scenery dotted with colorful Andean villages. Peru is synonymous with natural beauty and it is one of the world’s ten most biologically diverse countries. With more than 200 protected natural areas, it possesses 84 of the planet’s 117 life zones. Peru has created 14 national parks, 15 national reserves, 9 national sanctuaries and 11 reserved zones. It is home to more than 1800 species of birds and 10% of all the reptile, mammal and fish species that exist on Earth. It also has 3 500 varieties of orchids. Peru is also a paradise for lovers of adventure, offering a range of outdoor sporting activities for the curious, beginners, amateurs and experts, including trekking, climbing, mountain biking, surfing, paragliding, hang gliding, camping, canoeing and kayaking. These are just some of the most popular activities that form part of the host of possibilities offered by the varied geography of Peru."
#
print("Original:" +  str(text_tourism))
#
#
look_dictionary = { 
    'civilizations,':'communities,', 
   'empire;':'kingdom;' , 
   'luxurious':'great',
    'Andean':'cultural and green',
    'synonymous' : 'linked',
    'sanctuaries': 'manantials',
   'Earth.':'Peruvian territory.',   
   'paradise':'heaven',           
   'experts,':'every people,' 
}

print()


substitution = text_tourism.split()
Replace = []
for i in substitution:
  Replace.append(look_dictionary.get(i, i))
  
Replace = ' '.join(Replace)
print("Replaced article: " +  str(Replace))

# 
#