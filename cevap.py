minimumRequiredScore = 20
difficultyLevelsArray = [4, 7, 5, 10, 3]
difficultyLevelsSums = 0
topOfDifficultyLevel = 0

for difficultyLevel in difficultyLevelsArray:
    difficultyLevelsSums += difficultyLevel
    
    if difficultyLevel > topOfDifficultyLevel:
     topOfDifficultyLevel = difficultyLevel
        
if difficultyLevelsSums >= minimumRequiredScore:
    print("Çalışan prim alır.")
    print("Prim Miktarı: "+ str(topOfDifficultyLevel*3))
