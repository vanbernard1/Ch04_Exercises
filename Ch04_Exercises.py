EXERCISE 1
With the exercises/earthquakes.csv file, select all the earthquakes in Japan with a of 4.9 or greater using the mb magnitude type.

In [2]:
quakes.query(
    "parsed_place == 'Japan' and magType == 'mb' and mag >= 4.9"
)[['mag', 'magType', 'place']]
Out[2]:
mag	magType	place
1563	4.9	mb	293km ESE of Iwo Jima, Japan
2576	5.4	mb	37km E of Tomakomai, Japan
3072	4.9	mb	15km ENE of Hasaki, Japan
3632	4.9	mb	53km ESE of Hitachi, Japan

EXERCISE
 2
Create bins for each full number of magnitude (for example, the first bin is (0, 1], the second is (1, 2], and so on) with the ml magnitude type and count how many are in each bin.

In [3]:
quakes.query("magType == 'ml'").assign(
    mag_bin=lambda x: pd.cut(x.mag, np.arange(0, 10))
).mag_bin.value_counts()
Out[3]:
(1, 2]    3105
(0, 1]    2207
(2, 3]     862
(3, 4]     122
(4, 5]       2
(5, 6]       1
(6, 7]       0
(7, 8]       0
(8, 9]       0
Name: mag_bin, dtype: int64

EXERCISE 3
Using the exercises/faang.csv file, group by the ticker and resample to monthly frequency. Aggregate the open and close prices with the mean, the high price with the max, the low price with the min, and the volume with the sum.

In [4]:
faang.groupby('ticker').resample('1M').agg(
    {
        'open': np.mean,
        'high': np.max,
        'low': np.min,
        'close': np.mean,
        'volume': np.sum
    }
)
Out[4]:
                    open	high	low	close	volume
ticker	date					

AAPL	2018-01-31	43.505357	45.025002	41.174999	43.501309	2.638718e+09
        2018-02-28	41.819079	45.154999	37.560001	41.909737	3.711577e+09
        2018-03-31	43.761786	45.875000	41.235001	43.624048	2.854911e+09
        2018-04-30	42.441310	44.735001	40.157501	42.458572	2.664617e+09
        2018-05-31	46.239091	47.592499	41.317501	46.384205	2.483905e+09
        2018-06-30	47.180119	48.549999	45.182499	47.155357	2.110498e+09
        2018-07-31	47.549048	48.990002	45.855000	47.577857	1.574766e+09
        2018-08-31	53.121739	57.217499	49.327499	53.336522	2.801276e+09
        2018-09-30	55.582763	57.417500	53.825001	55.518421	2.715888e+09
        2018-10-31	55.300000	58.367500	51.522499	55.211413	3.158994e+09
        2018-11-30	47.954881	55.590000	42.564999	47.808929	3.845306e+09
        2018-12-31	41.310789	46.235001	36.647499	41.066579	3.595690e+09

AMZN	2018-01-31	1301.377151	1472.579956	1170.510010	1309.010946	9.637120e+07
        2018-02-28	1447.113159	1528.699951	1265.930054	1442.363146	1.377840e+08
        2018-03-31	1542.160464	1617.540039	1365.199951	1540.367629	1.304001e+08
        2018-04-30	1475.841902	1638.099976	1352.880005	1468.220471	1.299196e+08
        2018-05-31	1590.474543	1635.000000	1546.020020	1594.903637	7.161550e+07
        2018-06-30	1699.088582	1763.099976	1635.089966	1698.823812	8.594130e+07
        2018-07-31	1786.305716	1880.050049	1678.060059	1784.649042	9.752110e+07
        2018-08-31	1891.957833	2025.569946	1776.020020	1897.851308	9.657580e+07
        2018-09-30	1969.239476	2050.500000	1865.000000	1966.077900	9.444550e+07
        2018-10-31	1799.630865	2033.189941	1476.359985	1782.058265	1.832208e+08
        2018-11-30	1622.323806	1784.000000	1420.000000	1625.483823	1.392900e+08
        2018-12-31	1572.922100	1778.339966	1307.000000	1559.443154	1.548127e+08

FB	    2018-01-31	184.584284	190.660004	175.800003	184.962856	4.956557e+08
        2018-02-28	180.721578	195.320007	167.179993	180.269473	5.162516e+08
        2018-03-31	173.449524	186.100006	149.020004	173.489522	9.962017e+08
        2018-04-30	164.163332	177.100006	150.509995	163.810476	7.500727e+08
        2018-05-31	181.910909	192.720001	170.229996	182.930000	4.011441e+08
        2018-06-30	194.974763	203.550003	186.429993	195.267620	3.872656e+08
        2018-07-31	199.332381	218.619995	166.559998	199.967142	6.470307e+08
        2018-08-31	177.598695	188.300003	170.270004	177.492172	5.488327e+08
        2018-09-30	164.233158	173.889999	158.869995	164.377368	5.004688e+08
        2018-10-31	154.873479	165.880005	139.029999	154.187826	6.224463e+08
        2018-11-30	141.762857	154.130005	126.849998	141.635715	5.181517e+08
        2018-12-31	137.529475	147.190002	123.019997	137.161052	5.587862e+08

GOOG	2018-01-31	1127.200945	1186.890015	1045.229980	1130.770467	2.873840e+07
        2018-02-28	1088.629472	1174.000000	992.559998	1088.206839	4.238200e+07
        2018-03-31	1096.108085	1177.050049	980.640015	1091.490479	4.535330e+07
        2018-04-30	1038.415237	1094.165039	990.369995	1035.696187	4.171590e+07
        2018-05-31	1064.021376	1110.750000	1006.289978	1069.275901	3.184940e+07
        2018-06-30	1136.396182	1186.286011	1096.010010	1137.626668	3.209600e+07
        2018-07-31	1183.464280	1273.890015	1093.800049	1187.590472	3.194010e+07
        2018-08-31	1226.156951	1256.500000	1188.239990	1225.671732	2.880840e+07
        2018-09-30	1176.878424	1212.989990	1146.910034	1175.808934	2.886240e+07
        2018-10-31	1116.082172	1209.959961	995.830017	1110.940411	4.849470e+07
        2018-11-30	1054.971424	1095.569946	996.020020	1056.162394	3.673510e+07
        2018-12-31	1042.619998	1124.650024	970.109985	1037.420519	4.025760e+07

NFLX	2018-01-31	231.269525	286.809998	195.419998	232.908096	2.383776e+08
        2018-02-28	270.873158	297.359985	236.110001	271.443683	1.845858e+08
        2018-03-31	312.712859	333.980011	275.899994	312.228097	2.634494e+08
        2018-04-30	309.129524	338.820007	271.220001	307.466192	2.620060e+08
        2018-05-31	329.779541	356.100006	305.730011	331.536819	1.420508e+08
        2018-06-30	384.557143	423.209991	352.820007	384.133336	2.440318e+08
        2018-07-31	380.969526	419.769989	328.000000	381.515238	3.053938e+08
        2018-08-31	345.410001	376.809998	310.929993	346.257824	2.131223e+08
        2018-09-30	363.326843	383.200012	335.829987	362.641576	1.708321e+08
        2018-10-31	340.025218	386.799988	271.209991	335.445652	3.635898e+08
        2018-11-30	290.643335	332.049988	250.000000	290.344764	2.571264e+08
        2018-12-31	266.309474	298.720001	231.229996	265.302630	2.343100e+08

EXERCISE 4
Build a crosstab with the earthquake data between the tsunami column and the magType column. Rather than showing the frequency count, show the maximum magnitude that was observed for each combination. Put the magnitude type along the columns.

In [5]:
pd.crosstab(quakes.tsunami, quakes.magType, values=quakes.mag, aggfunc='max')
Out[5]:
magType     mb	    mb_lg	md	    mh	    ml	    ms_20   mw      mwb     mwr     mww
tsunami										
0	        5.6	    3.5	    4.11	1.1	    4.2	    NaN	    3.83	5.8	    4.8	    6.0
1	        6.1	    NaN	    NaN	    NaN	    5.1	    5.7	    4.41	NaN	    NaN	    7.5

EXERCISE 5
Calculate the rolling 60-day aggregations of the OHLC data by ticker for the FAANG data. Use the same aggregations as exercise 3.

In [6]:
faang.groupby('ticker').rolling('60D').agg(
    {
        'open': np.mean,
        'high': np.max,
        'low': np.min,
        'close': np.mean,
        'volume': np.sum
    }
)
Out[6]:
                        open	    high	    low	        close	    volume
ticker	date					
AAPL	2018-01-02	    42.540001	43.075001	42.314999	43.064999	102223600.0
        2018-01-03	    42.836250	43.637501	42.314999	43.061249	220295200.0
        2018-01-04	    42.935833	43.637501	42.314999	43.126666	310033600.0
        2018-01-05	    43.041875	43.842499	42.314999	43.282499	404673600.0
        2018-01-08	    43.151000	43.902500	42.314999	43.343500	486944800.0
...	...	...	...	...	...	...
NFLX	2018-12-24	    283.509251	332.049988	233.679993	281.931750	525657600.0
        2018-12-26	    281.844501	332.049988	231.229996	280.777750	520444300.0
        2018-12-27	    281.070489	332.049988	231.229996	280.162927	532679500.0
        2018-12-28	    279.916342	332.049988	231.229996	279.461464	521973500.0
        2018-12-31  	278.430770	332.049988	231.229996	277.451539	476314900.0
1255 rows × 5 columns

EXERCISE 6
Create a pivot table of the FAANG data that compares the stocks. Put the ticker in the rows and and show the averages of the OHLC and volume traded data.

In [7]:
faang.pivot_table(index='ticker')
Out[7]:
                close	        high	        low	            open            volume
ticker					
AAPL	        47.263357	    47.748526	    46.795877	    47.277859	    1.360803e+08
AMZN	        1641.726176	    1662.839839	    1619.840519	    1644.072709	    5.648994e+06
FB	            171.510956	    173.613347	    169.303148	    171.472948	    2.765860e+07
GOOG	        1113.225134	    1125.777606	    1101.001658	    1113.554101	    1.741965e+06
NFLX	        319.290319	    325.219322	    313.187330	    319.620558	    1.146962e+07

EXERCISE 7
Calculate the Z-scores of Amazon's data (ticker: AMZN) using apply().

In [8]:
faang.loc['2018-Q4'].query("ticker == 'AMZN'").drop(columns='ticker').apply(
    lambda x: x.sub(x.mean()).div(x.std())
).head()
Out[8]:
                high	low	open	close	volume
date					
2018-10-01	    2.368006	2.502113	2.337813	2.385848	-1.630411
2018-10-02	    2.227302	2.247433	2.190795	2.155037	-0.861879
2018-10-03	    2.058955	2.139987	2.068570	2.025489	-0.920345
2018-10-04	    1.819474	1.781561	1.850048	1.722816	-0.126582
2018-10-05	    1.628173	1.554416	1.642819	1.584748	-0.298771

EXERCISE 8
Adding event descriptions:

Create a dataframe with three columns: ticker, date, and event.
ticker will be 'FB'.
date will be datetimes ['2018-07-25', '2018-03-19', '2018-03-20']
event will be ['Disappointing user growth announced after close.', 'Cambridge Analytica story', 'FTC investigation'].
Set the index to ['date', 'ticker']
Merge this data to the FAANG data with a outer join.
In [9]:
events = pd.DataFrame({
    'ticker': 'FB',
    'date': pd.to_datetime(
         ['2018-07-25', '2018-03-19', '2018-03-20']
    ), 
    'event': [
         'Disappointing user growth announced after close.',
         'Cambridge Analytica story',
         'FTC investigation'
    ]
}).set_index(['date', 'ticker'])

faang.reset_index().set_index(['date', 'ticker']).join(
    events, how='outer'
).sample(10, random_state=0)
Out[9]:
                        high	        low	            open	        close	        volume	        event
date	    ticker						
2018-01-03	AAPL	    43.637501	    42.990002	    43.132500	    43.057499	    118071600.0	    NaN
2018-05-23	NFLX	    345.000000	    328.089996	    329.040009	    344.720001	    10049100.0	    NaN
2018-01-17	FB	        179.320007	    175.800003	    179.259995	    177.600006	    27992400.0	    NaN
2018-10-17	AMZN	    1845.000000	    1807.000000	    1842.790039	    1831.729980	    5295200.0	    NaN
2018-02-26	AMZN	    1522.839966	    1507.000000	    1509.199951	    1521.949951	    4955000.0	    NaN
2018-01-05	GOOG	    1104.250000	    1092.000000	    1094.000000	    1102.229980	    1279100.0	    NaN
2018-04-04	FB	        155.559998	    150.509995	    152.029999	    155.100006	    49885600.0	    NaN
2018-05-30	AMZN	    1626.000000	    1612.930054	    1618.099976	    1624.890015	    2907400.0	    NaN
2018-04-17	NFLX	    338.619995	    323.769989	    329.660004	    336.059998	    33866500.0	    NaN
2018-06-15	AMZN	    1720.869995	    1708.520020	    1714.000000	    1715.969971	    4777600.0	    NaN

EXERCISE 9
Use the transform() method on the FAANG data to represent all the values in terms of the first date in the data. To do so, divide all values for each ticker by the values of the first date in the data for that ticker. This is referred to as an index, and the data for the first date is the base. More information. When data is in this format, we can easily see growth over time. Hint: transform() can take a function name.

In [10]:
faang = faang.reset_index().set_index(['ticker', 'date'])
faang_index = (faang / faang.groupby(level='ticker').transform('first'))

# view 3 rows of the result per ticker
faang_index.groupby(level='ticker').agg('head', 3)
Out[10]:
                        high	    low	        open	    close	    volume
ticker	    date					
FB	        2018-01-02	1.000000	1.000000	1.000000	1.000000	1.000000
            2018-01-03	1.017623	1.021290	1.023638	1.017914	0.930294
            2018-01-04	1.025498	1.036891	1.040635	1.016040	0.764708

AAPL	    2018-01-02	1.000000	1.000000	1.000000	1.000000	1.000000
            2018-01-03	1.013059	1.015952	1.013928	0.999826	1.155033
            2018-01-04	1.006790	1.016661	1.013987	1.004470	0.877864

AMZN	    2018-01-02	1.000000	1.000000	1.000000	1.000000	1.000000
            2018-01-03	1.013017	1.015199	1.013908	1.012775	1.153758
            2018-01-04	1.021739	1.029175	1.028157	1.017308	1.121581

NFLX	    2018-01-02	1.000000	1.000000	1.000000	1.000000	1.000000
            2018-01-03	1.022614	1.031112	1.030342	1.019794	0.783394
            2018-01-04	1.026779	1.043905	1.051504	1.022679	0.549800

GOOG	    2018-01-02	1.000000	1.000000	1.000000	1.000000	1.000000
            2018-01-03	1.018136	1.017202	1.015234	1.016413	1.155624
            2018-01-04	1.024959	1.037094	1.037831	1.020094	0.811732

EXERCISE 10
Part 1
Read in the data in the exercises/covid19_cases.csv file
Create a date column by parsing the dateRep column into a datetime
Set the date column as the index
Use the replace() method to update all occurrences of United_States_of_America and United Kingdom to USA and UK, respectively
Sort the index
In [11]:
covid = pd.read_csv('../../ch_04/exercises/covid19_cases.csv')\
    .assign(date=lambda x: pd.to_datetime(x.dateRep, format='%d/%m/%Y'))\
    .set_index('date')\
    .replace('United_States_of_America', 'USA')\
    .replace('United_Kingdom', 'UK')\
    .sort_index()
Part 2
For the 5 countries with the most cases (cumulative), find the day with the largest number of cases.

In [12]:
top_five_countries = covid\
    .groupby('countriesAndTerritories').cases.sum()\
    .nlargest(5).index

covid[covid.countriesAndTerritories.isin(top_five_countries)]\
    .groupby('countriesAndTerritories').cases.idxmax()
Out[12]:
countriesAndTerritories

Brazil   2020-07-30
India    2020-09-17
Peru     2020-08-17
Russia   2020-07-18
USA      2020-07-25

Name: cases, dtype: datetime64[ns]
Part 3
Find the 7-day average change in COVID-19 cases for the last week in the data for the countries found in part 2.

In [13]:
covid\
    .groupby(['countriesAndTerritories', pd.Grouper(freq='1D')]).cases.sum()\
    .unstack(0).diff().rolling(7).mean().last('1W')[top_five_countries]
Out[13]:
countriesAndTerritories	      USA           India           Brazil          Russia          Peru
date					
2020-09-14	                  473.714286	181.285714	    35.285714	    36.285714	    73.142857
2020-09-15	                  1513.000000	1142.857143	    697.428571	    46.285714	    377.571429
2020-09-16	                  3478.714286	59.571429	    3196.285714	    61.428571	    -65.000000
2020-09-17	                  -1047.000000	308.428571	    143.428571	    810.000000	    -29.428571
2020-09-18	                  865.714286	-18.142857	    -607.714286	    -688.428571	    -227.571429
2020-09-19	                  306.857143	-604.714286	    -560.142857	    57.285714	    -41.285714
Part 4
Find the first date that each country other than China had cases:

In [14]:
covid.reset_index()\
    .pivot(index='date', columns='countriesAndTerritories', values='cases')\
    .drop(columns='China')\
    .fillna(0)\
    .apply(lambda x: x[(x > 0)].idxmin())\
    .sort_values()\
    .rename(lambda x: x.replace('_', ' '))
Out[14]:
countriesAndTerritories
Thailand         2020-01-13
Japan            2020-01-15
South Korea      2020-01-20
USA              2020-01-21
Taiwan           2020-01-21
                    ...    
Lesotho          2020-05-15
Uruguay          2020-05-17
Western Sahara   2020-06-20
Mali             2020-07-07
Puerto Rico      2020-09-10

Length: 209, dtype: datetime64[ns]
Part 5
Rank the countries by total cases using percentiles.

In [15]:
covid\
    .pivot_table(columns='countriesAndTerritories', values='cases', aggfunc='sum')\
    .T\
    .transform('rank', method='max', pct=True)\
    .sort_values('cases', ascending=False)\
    .rename(lambda x: x.replace('_', ' '))
Out[15]:
cases
countriesAndTerritories	
USA	        1.000000
India	    0.995238
Brazil	    0.990476
Russia	    0.985714
Peru	    0.980952
...	...
Greenland	0.023810
Montserrat	0.019048
Falkland Islands (Malvinas)	0.019048
Holy See	0.009524
Anguilla	0.004762
210 rows × 1 columns