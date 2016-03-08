Import gadfly and initialize the simulation.
>>> import gadfly as gdf
>>> sim = gdf.Simulation('path_to_simulation_directory')

Load a snapshot:
>>> snap = sim.load_snapshot(100)
>>> snap.file_id
<HDF5 file "snapshot_100.hdf5" (mode r)>
>>> snap.file_id.keys()
[u'Header', u'PartType0', u'PartType1']

Inspect the Header:
>>> snap.header.Redshift
26.663827788885538
>>> snap.header.BoxSize
100.0

Load a particle dataset:
>>> snap.define_ptype('dm', 1, gdf.nbody.PartTypeNbody)
>>> snap.dm.load_masses()
>>> snap.dm.info()
<class 'gadfly.nbody.PartTypeNbody'>
Int64Index: 13347573 entries, 25272898 to 25272897
Data columns (total 1 columns):
masses    float64
dtypes: float64(1)
memory usage: 203.7 MB

>>> snap.dm.cleanup()
>>> snap.dm.load_quantity('coordinates', 'particleIDs')
>>> snap.dm.info()
<class 'gadfly.nbody.PartTypeNbody'>
Int64Index: 13347573 entries, 25272898 to 25272897
Data columns (total 4 columns):
x              float64
y              float64
z              float64
particleIDs    uint32
dtypes: float64(3), uint32(1)
memory usage: 458.3 MB

Load non-standard particle field:
>>> snap.define_ptype('gas', 0, gdf.sph.PartTypeSPH)
>>> snap.gas.load_quantity('Adiabatic index')
>>> snap.gas.info()
<class 'gadfly.sph.PartTypeSPH'>
Int64Index: 13347573 entries, 23325038 to 23308525
Data columns (total 1 columns):
Adiabatic index    float64
dtypes: float64(1)
memory usage: 203.7 MB

Load dataset using a custom class:
>>> from custom_ptype import PartTypeCustom
>>> snap.define_ptype('gas', 0, PartTypeCustom)
>>> snap.gas.calculate_temperature()
>>> snap.gas.info()
<class 'custom_ptype.PartTypeCustom'>
Int64Index: 13347573 entries, 23325038 to 23308525
Data columns (total 3 columns):
adiabatic_index    float64
internal_energy    float64
temperature        float64
dtypes: float64(3)
memory usage: 407.3 MB