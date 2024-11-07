# Antall KM kjørt per år 
TotalKM = 12000  

# Forsikringskostnader
FELelektronisk = 5000  
FBensin = 7500  
DFtrafikk = 8.38  
ÅFtrafikk = DFtrafikk * 365 

# Kostnader per km
KWHperKM = 0.2   
EKWH = 2.00  
BensinKM = 1.0 

# Bomavgifter per km
EBomPerKM = 0.1  
BBomPerKM = 0.3  

# Beregner årlige drivstoffkostnader
ÅrligeElektriskDrivstoffKostander = KWHperKM * EKWH * TotalKM
ÅrligBensinKostnader = BensinKM * TotalKM

# Beregner årlige bomkostnader
ÅrligBomEL = EBomPerKM * TotalKM
ÅrligBomBen = BBomPerKM * TotalKM

# Beregner totale årlige kostnader
TotalKostEL = FELelektronisk + ÅFtrafikk + ÅrligeElektriskDrivstoffKostander + ÅrligBomEL
TotalKostBen = FBensin + ÅFtrafikk + ÅrligBensinKostnader + ÅrligBomBen

# Beregner årlig kostnadsdifferanse
ÅrligKostDifferanse = TotalKostBen - TotalKostEL

# Presenterer resultatene
print("Totale årlige kostnader for elbil (kr):", TotalKostEL)
print("Totale årlige kostnader for bensinbil (kr):", TotalKostBen)
print("Årlig kostnadsdifferanse (kr):", ÅrligKostDifferanse)