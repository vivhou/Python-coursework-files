total_lemons = 20
rotten_lemons = 3
remaining_lemons = total_lemons - rotten_lemons
lemons_pitcher = 4
total_pitchers_lemonade=remaining_lemons / lemons_pitcher

print("I bought {} lemons to make lemonade".format(total_lemons))
print("Unfortunately, I found {} lemons that were rotten".format(rotten_lemons))
print("Now I only have {} lemons".format(remaining_lemons))
print("Since a pitcher of lemonade requires {} lemons, I can make {} pitchers of lemonade".format(lemons_pitcher, total_pitchers_lemonade))
