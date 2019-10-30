
# Boucle for pour le calcul du captial fin de période Assurance Vie - Si les apports ont lieu avant paiement des intérêts (donc dès le début)
def capfin(capital, annAv, netAv, annees):
    i = 0
    sumCap = capital
    logSumCap = []
    logSumCapintP = []
    while i < annees:
        sumCap += annAv
        logSumCap.append(sumCap)
        intP = sumCap * netAv
        sumCap += intP
        logSumCapintP.append(sumCap)
        i+=1
    print(logSumCap)
    print(logSumCapintP)
    print(round(sumCap,2))

capfin(0, 1200, .018, 10)