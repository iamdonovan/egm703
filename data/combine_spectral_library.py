from glob import glob
import pandas as pd
from scipy.interpolate import interp1d

lib_df = pd.read_csv('spectral_library.csv')

names = ['ponderosa', 'sulfate', 'mafic', 'sandstone', 'shale', 'siltstone', 'limestone']

for name in names:
    df_list = []
    for fn in glob('*.{}.*.spectrum.txt'.format(name)):
        df_list.append(pd.read_csv(fn, names=['wavelength', 'reflectance'], delimter='\t', skiprows=21))
    this_data = pd.concat(df_list)

    this_data.sort_values('wavelength', ascending=True, inplace=True)

    avg = this_data.rolling(25).mean()
    avg.dropna(inplace=True)
    
    f_ref = interp1d(avg.wavelength.values.reshape(-1) * 1000,
                     avg.reflectance.values.reshape(-1) / 100)

    lib_df[name] = f_ref(lib_df.wavelength)

lib_df.to_csv('spectral_library.csv', index=False)
