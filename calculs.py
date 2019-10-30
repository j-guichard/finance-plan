from vars import *

#///////////////////////////////////////////////////////////////////////////
#//////////////////////////// Sans annuité /////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

# Calcul valeur finale Assurance-Vie sans versement 
vfAv = (capital*partAv)*(1+netAv)**annees


print(round(vfAv,2))

# Calcul valeur finale Bourse sans versement 
vfBourse = (capital*partBourse)*(1+netBourse)**annees
print(round(vfBourse,2))

# Calcul valeur finale Crowdfunding sans versement 
vfCrowdF = (capital*partCrowdF)*(1+netCrowdF)**annees
print(round(vfCrowdF,2))

# # Calcul valeur finale Plan Investissement sans versement 
vfTot = vfAv + vfBourse + vfCrowdF
print(round(vfTot,2))

#///////////////////////////////////////////////////////////////////////////
#/////////////////////////// Avec annuité //////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

vfaAv = (annualite*partAv)*((((1+netAv)**annees)-1)/netAv)
print(round(vfaAv,2))

vfaBourse = (annualite*partBourse)*((((1+netBourse)**annees)-1)/netBourse)
print(round(vfaBourse,2))

vfaCrowdF = (annualite*partCrowdF)*((((1+netCrowdF)**annees)-1)/netCrowdF)
print(round(vfaCrowdF,2))