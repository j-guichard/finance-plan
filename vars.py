#investissement
capital = 1000
mensualite = 100
annualite = mensualite*12
annees = 10

#répartition
partAv = .4
partBourse = .4
partCrowdF = .2
annAv = partAv*annualite
annBourse = partBourse*annualite
annAv = partCrowdF*annualite

#intérêts brut
intAv = .028
intBourse = .06
intCrowdF = .08

#frais de gestion
fgAv = .01
fgBourse = .01
fgCrowdF = .01

#intérêts net
netAv = intAv - fgAv
netBourse = intBourse - fgBourse
netCrowdF = intCrowdF - fgCrowdF