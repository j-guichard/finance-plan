
# Boucle for pour le calcul du captial fin de période Assurance Vie - Si les apports ont lieu après paiement des intérêts
def capfin(capital, annAv, netAv, annees):
    i = 0
    sumCap = capital
    logSumCap = []
    logSumCapintP = []
    while i < annees:
        logSumCap.append(sumCap)
        intP = sumCap * netAv
        sumCap += intP
        logSumCapintP.append(sumCap)
        sumCap += annAv
        i+=1
    print(logSumCap)
    print(logSumCapintP)
    print(round(sumCap,2))

capfin(1000, 1200, .018, 10)