Specifying code unit conversions:
>>> import gadfly as gdf
>>> sim = gdf.Simulation('path_to_simulation_directory', 
                         UnitMass_in_g = 1.989e43,
                         UnitLength_in_cm = 3.085678e21,
                         UnitVelocity_in_cm_per_s = 1e5)

Specify default units:
>>> sim = gdf.Simulation('path_to_simulation_directory', 
                         length='kpc',
                         mass = 'solar',
                         velocity = 'kms',
                         time = 'gyr')

Change default units on the fly:
>>> sim.units.length_unit
'kpc'
>>> sim.units.set_length('AU')
>>> sim.units.length_unit
'AU'

Specify units at load time:
>>> sim.units.mass_unit
'g'
>>> snap.gas.load_masses(unit='solar')
>>> sim.units.mass_unit
'solar'
