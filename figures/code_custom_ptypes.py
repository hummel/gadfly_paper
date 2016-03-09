Loading a non-standard particle field:
>>> snap.define_ptype('gas', 0, gdf.sph.PartTypeSPH)
>>> snap.gas.load_quantity('Adiabatic index')
>>> snap.gas.info()
<class 'gadfly.sph.PartTypeSPH'>
Int64Index: 13347573 entries, 23325038 to 23308525
Data columns (total 1 columns):
Adiabatic index    float64
dtypes: float64(1)
memory usage: 203.7 MB

Loading a dataset using a custom class:
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