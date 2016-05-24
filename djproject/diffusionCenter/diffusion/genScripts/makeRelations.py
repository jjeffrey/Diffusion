from diffusion.models import DiffusionRelation

# reference: http://www.engineeringtoolbox.com/thermal-conductivity-metals-d_858.html
#make Titanium
titanium_aluminum = DiffusionRelation(diffusion_type='INTER', material_1='Ti', material_2='Al', additional_data='{{"D0": 0.0000}}')
titanium_aluminum.save()

#make Aluminum
titanium_gold = DiffusionRelation(diffusion_type='INTER', material_1='Ti', material_2='Au', additional_data='{{"D0": 0.0000}}')
titanium_gold.save()

#make Nickel
titanium_nickel = DiffusionRelation(diffusion_type='INTER', material_1='Ti', material_2='Ni', additional_data='{{"D0": 0.0000}}')
titanium_nickel.save()

#make Gold
nickel_gold = DiffusionRelation(diffusion_type='INTER', material_1='Ni', material_2='Au', additional_data='{{"D0": 0.0000}}')
nickel_gold.save()