import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

oecd_bli = pd.read_csv("oecd_bli.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values='n/a')


def prepare_country_stats(life, gdp):
    good = gdp[(gdp["Units"] == "U.S. dollars") & (gdp["2015"].notnull())]
    a = []
    b = []
    c = []

    for country in good["Country"]:

        l = life[
            (life["Country"] == country) & (life["Indicator"] == "Life satisfaction") & (life["Inequality"] == "Total")]
        g = good[good["Country"] == country]
        if l.empty:
            continue
        a.append(country)
        b.append(float(l["Value"]))
        c.append(float(g["2015"]))

    return pd.DataFrame({"Country": a, "Life satisfaction": b, "GDP per capita": c})


country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)

print(country_stats.head(3))

X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

country_stats.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.show()


lin_reg_model = LinearRegression()
lin_reg_model.fit(X, y)

country_stats.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.plot(X, lin_reg_model.predict(X))
plt.show()

print(lin_reg_model.predict([[22587]]))
