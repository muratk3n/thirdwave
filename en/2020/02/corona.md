
https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_outbreak

```python
import pandas as pd, csv

df1 = pd.read_csv('corona.csv',sep='\t')
d1 = df1[['Country','Confirmed']].set_index('Country').to_dict()
df2 = pd.read_csv('alpha3country.csv',sep=',', skipinitialspace=True)
d2 = df2[['Country','Alpha-3 code']].set_index('Country').to_dict()
print (d1)
print (d2)
```

```text
{'Confirmed': {' Macau': '10', ' Japan': '134', ' Israel': '1', ' India': '3', ' United Kingdom': '9', ' Egypt': '1', ' Nepal': '1', ' Hong Kong': '70', ' Iran': '28', ' Sri Lanka': '1', ' United States': '35', ' Sweden': '1', ' South Korea': '433', ' Russia': '2', ' Taiwan': '26', ' Lebanon': '1', ' United Arab Emirates': '13', ' Others': '634', ' Philippines': '3', ' Vietnam': '16', ' Singapore': '89', ' Australia': '21', ' France': '12', ' Germany': '16', ' Belgium': '1', ' Spain': '2', ' China': '76,291', ' Malaysia': '22', ' Cambodia': '1', ' Finland': '1', ' Thailand': '35', ' Canada': '9', ' Italy': '62'}}
{'Alpha-3 code': {'Timor-Leste': 'TLS', 'Bouvet Island': 'BVT', 'Korea, Republic of': 'KOR', 'Taiwan': 'TWN', 'Colombia': 'COL', 'Switzerland': 'CHE', 'French Polynesia': 'PYF', 'Mali': 'MLI', 'Vietnam': 'VNM', 'Costa Rica': 'CRI', 'Madagascar': 'MDG', 'Saint Helena, Ascension and Tristan da Cunha': 'SHN', 'Czech Republic': 'CZE', 'United Kingdom': 'GBR', 'Argentina': 'ARG', 'Montenegro': 'MNE', 'Bermuda': 'BMU', 'Tanzania, United Republic of': 'TZA', 'Uruguay': 'URY', 'Papua New Guinea': 'PNG', 'Cambodia': 'KHM', 'Grenada': 'GRD', 'Netherlands Antilles': 'ANT', 'Somalia': 'SOM', 'Jersey': 'JEY', 'Cyprus': 'CYP', 'Belarus': 'BLR', 'Falkland Islands (Malvinas)': 'FLK', 'Iran, Islamic Republic of': 'IRN', 'Honduras': 'HND', 'Uzbekistan': 'UZB', 'South Georgia and the South Sandwich Islands': 'SGS', 'Kuwait': 'KWT', 'Dominica': 'DMA', 'Vanuatu': 'VUT', 'Norfolk Island': 'NFK', 'Thailand': 'THA', 'Brunei': 'BRN', 'Morocco': 'MAR', 'Bhutan': 'BTN', 'Zambia': 'ZMB', 'Svalbard and Jan Mayen': 'SJM', 'Malta': 'MLT', 'Trinidad and Tobago': 'TTO', 'Estonia': 'EST', 'Syrian Arab Republic': 'SYR', 'Armenia': 'ARM', 'Mayotte': 'MYT', 'Angola': 'AGO', 'Kazakhstan': 'KAZ', 'Mauritania': 'MRT', 'Micronesia, Federated States of': 'FSM', 'Latvia': 'LVA', 'Yemen': 'YEM', 'Belize': 'BLZ', 'Iraq': 'IRQ', 'Guadeloupe': 'GLP', 'Peru': 'PER', 'French Guiana': 'GUF', 'Seychelles': 'SYC', 'Zimbabwe': 'ZWE', 'Norway': 'NOR', 'Libyan Arab Jamahiriya': 'LBY', 'Ivory Coast': 'CIV', 'Gibraltar': 'GIB', 'China': 'CHN', 'Sri Lanka': 'LKA', 'St. Vincent and the Grenadines': 'VCT', 'British Indian Ocean Territory': 'IOT', 'Malawi': 'MWI', 'Macao': 'MAC', 'Niue': 'NIU', 'Tajikistan': 'TJK', "Côte d'Ivoire": 'CIV', 'Georgia': 'GEO', 'Martinique': 'MTQ', 'Saudi Arabia': 'SAU', 'Equatorial Guinea': 'GNQ', 'Mongolia': 'MNG', 'Réunion': 'REU', 'Saint Kitts and Nevis': 'KNA', 'Virgin Islands, U.S.': 'VIR', 'Cayman Islands': 'CYM', 'Tokelau': 'TKL', 'Solomon Islands': 'SLB', 'Aruba': 'ABW', 'Liechtenstein': 'LIE', 'Venezuela': 'VEN', 'Qatar': 'QAT', 'South Africa': 'ZAF', 'Hong Kong': 'HKG', 'Viet Nam': 'VNM', 'Denmark': 'DNK', 'Mauritius': 'MUS', 'Chad': 'TCD', 'Senegal': 'SEN', 'Myanmar': 'MMR', 'Bosnia and Herzegovina': 'BIH', 'Comoros': 'COM', 'Congo, the Democratic Republic of the': 'COD', 'Holy See (Vatican City State)': 'VAT', 'Pitcairn': 'PCN', 'Sweden': 'SWE', 'Bolivia': 'BOL', 'Virgin Islands, British': 'VGB', 'New Zealand': 'NZL', 'Philippines': 'PHL', 'Libya': 'LBY', 'Australia': 'AUS', 'Cameroon': 'CMR', 'Nepal': 'NPL', 'Mexico': 'MEX', 'Kyrgyzstan': 'KGZ', 'Belgium': 'BEL', 'Antigua and Barbuda': 'ATG', 'Ghana': 'GHA', 'Algeria': 'DZA', 'Gambia': 'GMB', 'Russia': 'RUS', 'Monaco': 'MCO', 'Ethiopia': 'ETH', 'Bangladesh': 'BGD', 'Cook Islands': 'COK', "Korea, Democratic People's Republic of": 'PRK', 'Benin': 'BEN', 'Nigeria': 'NGA', "Lao People's Democratic Republic": 'LAO', 'Maldives': 'MDV', 'Bolivia, Plurinational State of': 'BOL', 'Albania': 'ALB', 'Andorra': 'AND', 'Fiji': 'FJI', 'Puerto Rico': 'PRI', 'Slovakia': 'SVK', 'Ukraine': 'UKR', 'Jordan': 'JOR', 'Pakistan': 'PAK', 'United Arab Emirates': 'ARE', 'Botswana': 'BWA', 'Nauru': 'NRU', 'Slovenia': 'SVN', 'Marshall Islands': 'MHL', 'Guatemala': 'GTM', 'Burundi': 'BDI', 'Brazil': 'BRA', 'Japan': 'JPN', 'Lithuania': 'LTU', 'Saint Pierre and Miquelon': 'SPM', 'Togo': 'TGO', 'Macedonia, the former Yugoslav Republic of': 'MKD', 'Sierra Leone': 'SLE', 'Sao Tome and Principe': 'STP', 'Palestinian Territory, Occupied': 'PSE', 'Rwanda': 'RWA', 'Liberia': 'LBR', 'Cape Verde': 'CPV', 'Turkey': 'TUR', 'Ireland': 'IRL', 'American Samoa': 'ASM', 'Austria': 'AUT', 'Nicaragua': 'NIC', 'San Marino': 'SMR', 'Guinea-Bissau': 'GNB', 'Canada': 'CAN', 'France': 'FRA', 'Bahrain': 'BHR', 'Swaziland': 'SWZ', 'Western Sahara': 'ESH', 'Portugal': 'PRT', 'Taiwan, Province of China': 'TWN', 'Malaysia': 'MYS', 'Saint Lucia': 'LCA', 'Azerbaijan': 'AZE', 'Bahamas': 'BHS', 'Italy': 'ITA', 'Israel': 'ISR', 'Spain': 'ESP', 'South Korea': 'KOR', 'Anguilla': 'AIA', 'Guyana': 'GUY', 'Montserrat': 'MSR', 'Congo': 'COG', 'Barbados': 'BRB', 'United States': 'USA', 'French Southern Territories': 'ATF', 'Djibouti': 'DJI', 'Tuvalu': 'TUV', 'Germany': 'DEU', 'Luxembourg': 'LUX', 'Iceland': 'ISL', 'Uganda': 'UGA', 'Moldova, Republic of': 'MDA', 'Poland': 'POL', 'Hungary': 'HUN', 'Finland': 'FIN', 'Guinea': 'GIN', 'Panama': 'PAN', 'Romania': 'ROU', 'Greenland': 'GRL', 'Tunisia': 'TUN', 'Mozambique': 'MOZ', 'Jamaica': 'JAM', 'Wallis and Futuna': 'WLF', 'Dominican Republic': 'DOM', 'Suriname': 'SUR', 'India': 'IND', 'Paraguay': 'PRY', 'Indonesia': 'IDN', 'Croatia': 'HRV', 'Kenya': 'KEN', 'Tonga': 'TON', 'Haiti': 'HTI', 'Christmas Island': 'CXR', 'Guam': 'GUM', 'Palau': 'PLW', 'El Salvador': 'SLV', 'Gabon': 'GAB', 'Central African Republic': 'CAF', 'Russian Federation': 'RUS', 'Heard Island and McDonald Islands': 'HMD', 'Brunei Darussalam': 'BRN', 'Afghanistan': 'AFG', 'Egypt': 'EGY', 'Namibia': 'NAM', 'Greece': 'GRC', 'United States Minor Outlying Islands': 'UMI', 'Samoa': 'WSM', 'Bulgaria': 'BGR', 'Northern Mariana Islands': 'MNP', 'Singapore': 'SGP', 'Guernsey': 'GGY', 'Cuba': 'CUB', 'Turkmenistan': 'TKM', 'New Caledonia': 'NCL', 'Serbia': 'SRB', 'Saint Vincent & the Grenadines': 'VCT', 'Venezuela, Bolivarian Republic of': 'VEN', 'Faroe Islands': 'FRO', 'Saint Vincent and the Grenadines': 'VCT', 'Lesotho': 'LSO', 'Antarctica': 'ATA', 'Oman': 'OMN', 'Isle of Man': 'IMN', 'Eritrea': 'ERI', 'Trinidad & Tobago': 'TTO', 'Niger': 'NER', 'Burkina Faso': 'BFA', 'Chile': 'CHL', 'Netherlands': 'NLD', 'Burma': 'MMR', 'Lebanon': 'LBN', 'Ecuador': 'ECU', 'Cocos (Keeling) Islands': 'CCK', 'Turks and Caicos Islands': 'TCA', 'Kiribati': 'KIR', 'Sudan': 'SDN'}}
```



























