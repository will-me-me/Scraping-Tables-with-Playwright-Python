from os import path
from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=1000)

    page = browser.new_page()
    page.goto('https://www.worldometers.info/world-population/population-by-country/', wait_until="networkidle")
    h1_selector= '//div[1]/h1'
    heading = page.query_selector(h1_selector)
    print(heading.inner_text())
    countries= page.query_selector_all('//tbody/tr/td[2]/a')
    length = len(countries)

    for country in countries:
        my_countries=country.inner_text()
        # print(my_countries)
    population = page.query_selector_all('//tbody/tr/td[3]')
    for pop in population:
        country_pop=pop.inner_text()
        # print(country_pop)

        # print(pop.inner_text())
    density = page.query_selector_all('//tbody/tr/td[6]')
    for dens in density:
        country_density=dens.inner_text()
        # print(country_density)

        # print(dens.inner_text())
    urban_pop=page.query_selector_all('//tbody/tr/td[11]')
    for urban in urban_pop:
        country_urban_pop=urban.inner_text()
        # print(country_urban_pop)

        # print(urban.inner_text())

    popilation_results=[]
    for i in range(length):
        data= {'Country': countries[i].inner_text(),
                   'Population': population[i].inner_text(),
                   'Density': density[i].inner_text(),
                   'Urban_pop': urban_pop[i].inner_text()}


        popilation_results.append(data)
        # print(popilation_results)
    df_data=pd.DataFrame(popilation_results)
    print(df_data)
    df_data.to_excel('population12.xlsx', index=False)



    browser.close()