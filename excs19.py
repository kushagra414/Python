# Thourouly learning the using of functions

def party_and_games(price_money, fun_foods):
    print """Zed.A.Shaw: When will the Party start?
	Kush: The party will start at 8:00 pm on Saturday.
	Kush: Are you coming?
	Zed.A.Shaw: Definately, How can i miss a party by the greatest programmer!
	Kush: Ah! You exagarrate the things."""
    print 'Kush: Anywas just dont forget there will be a programming competition. The price money will be $%d' % (price_money)
    print 'Kush: There will be lots of fun foods like %s' % fun_foods
    print 'Kush: Goodbye, See you on Saturday'
    print "Zed.A.Shaw:I know i cant win the competition as you will be there, anways i'll try my best. Take Care."

money = 10000
foods = "Pizza, Cold Drinks, Burgers, Beer, Champane, Shakes, Exotic Fruits etc. etc."

party_and_games(money, foods)

print "Testing another argument"

party_and_games(20000+111, 'Pizza')
