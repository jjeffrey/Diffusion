from diffusion.models import Material

# reference: http://www.engineeringtoolbox.com/thermal-conductivity-metals-d_858.html
#make Titanium
titanium = Material(name='titanium', short_name='Ti', thermal_conductivity=21,melting_point=1668)
titanium.save()

#make Aluminum
aluminum = Material(name='aluminum', short_name='Al', thermal_conductivity=230,melting_point=660,additional_data='{{"other_names": ["aluminium"]}}')
aluminum.save()

#make Nickel
nickel = Material(name='nickel', short_name='Ni', thermal_conductivity=90,melting_point=1455)
nickel.save()

#make Gold
gold = Material(name='gold', short_name='Au', thermal_conductivity=315,melting_point=1064)
gold.save()