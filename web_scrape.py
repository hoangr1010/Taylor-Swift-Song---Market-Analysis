import pandas as pd 
import numpy as np
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import billboard
from datetime import datetime
import time

def get_hot_100():
    """
    - Scrape data from Hot 100 chart on Billboard about Taylor Swift Song only
    - Return a table of Taylor on Hot 100 Chart

    Arguments:
        None

    Returns:
        Table on this website: https://www.billboard.com/artist/taylor-swift/chart-history/hsi/
    """
    #get the soup from website
    r = requests.get('https://www.billboard.com/artist/taylor-swift/chart-history/hsi/')
    soup = BeautifulSoup(r.content,'html.parser')
    table = soup.find(attrs = {'class':'artist-chart-history-container // u-max-width-860 lrv-u-margin-lr-auto lrv-u-position-relative'})

    #Scrape header of the table
    header_soup = (
                    table
                        .find(attrs = {'class':'artist-chart-history-sticky-wrapper lrv-u-position-relative'})
                        .find(attrs = {'class':'artist-chart-history-header // lrv-u-text-align-center lrv-u-background-color-brand-primary lrv-u-color-white lrv-u-flex lrv-u-align-items-center lrv-u-text-transform-uppercase lrv-u-line-height-small'})
                        .find_all('div')
                  )
    headers = []
    for i in header_soup:
        head = (i.text
                    .replace('\n','')
                    .replace('\t','')
                    )
        headers.append(head)
    headers.remove('Billboard Hot 100')
    hot_100_df = pd.DataFrame(columns = headers)

    #get the table contents
        #get the columns of Song name
    row_soup = (
        table
            .find(attrs={'class':'artist-chart-history-items'})
            .find_all(attrs={'class':'o-chart-results-list-row // lrv-u-flex lrv-u-flex-direction-column@mobile-max u-height-100 lrv-u-background-color-white'})
    )

    name_list = []
    for i in row_soup:
        song_name = (
            i
                .find(attrs={'class':'o-chart-results-list__item // lrv-u-flex lrv-u-flex-direction-column lrv-u-flex-grow-1 lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-lr-2 lrv-u-padding-lr-1@mobile-max lrv-u-padding-tb-050@mobile-max'})
                .find(id = 'title-of-a-story')
                .text
                .replace('\n',"")
                .replace('\t','')
        )
        name_list.append(song_name)
    
        #get content of each song
    info_soup = (
                    row_soup[0]
                        .find(attrs={'class':'lrv-u-flex lrv-u-height-100p u-background-color-grey-lightest@mobile-max u-height-37@mobile-max'})
                        .find_all('div')
                )   
    for info in row_soup: 
        info_soup = (
                    info
                        .find(attrs={'class':'lrv-u-flex lrv-u-height-100p u-background-color-grey-lightest@mobile-max u-height-37@mobile-max'})
                        .find_all('div')
                    )
        row_list = []
        for i in info_soup:
            row_data = i.find('span')
            row_list.append(
                            row_data
                                .text
                                .replace('\n','')
                                .replace('\t','')    
                            )
        length = len(hot_100_df)
        hot_100_df.loc[length] = row_list
    
    #Add song name columns to main dataframe
    hot_100_df['Billboard Hot 100'] = name_list

    return hot_100_df

def get_youtube_chart():
    """
    - Scrape data from Youtube Music chart about Taylor Swift views by countries

    Arguments:
        None

    Returns:
        Table of data on this website: https://charts.youtube.com/artist/%2Fm%2F0dl567?hl=vi
    """

    #Connect to chrome driver
    driver = webdriver.Chrome('/Users/hoanglui/Library/Mobile Documents/comappleCloudDocs/Environment/chromedriver_mac_arm64.zip')

    #Execute on website
    driver.get('https://charts.youtube.com/artist/%2Fm%2F0dl567?hl=vi')
    time.sleep(13)

    list_drop = driver.find_element(
                                    'xpath',
                                    '/html/body/ytmc-app/div[3]/ytmc-insights-artist/div[1]/ytmc-dropdown/paper-dropdown-menu/paper-menu-button/div/div/paper-input/paper-input-container/div[2]/span[2]/iron-icon'
                                    )
    list_drop.click()

    last_12_month = driver.find_element(
                                    'xpath',
                                    '/html/body/ytmc-app/div[3]/ytmc-insights-artist/div[1]/ytmc-dropdown/paper-dropdown-menu/paper-menu-button/iron-dropdown/div/div/paper-listbox/paper-item[4]'
                                    )
    last_12_month.click()

    time.sleep(5)

    see_all_top_country = driver.find_element(
                                    'xpath',
                                    '/html/body/ytmc-app/div[3]/ytmc-insights-artist/div[2]/div[3]/div[3]/ytmc-rankings-card/div/div[3]/a'
                                    )
    see_all_top_country.click()

    #create dataframe
    countries_view_df = pd.DataFrame(columns = ['country', 'view_amt'])
    countries_view_df

    #add datafrom website to dataframe
    for block in range(1,101):
        row = []
        country = (
                driver.find_element(
                    'xpath',
                    '/html/body/ytmc-app/div[3]/ytmc-insights-artist/div[2]/div[3]/div[3]/ytmc-rankings-card/div/div[4]/ytmc-view-more-dialog/paper-dialog/paper-dialog-scrollable/div/div/ytmc-entity-row[{}]/div/div/div[2]/div[1]/ytmc-ellipsis-text/div/span'.format(block)
                ).text
            )
        view_amt = (
            driver.find_element(
                    'xpath',
                    '/html/body/ytmc-app/div[3]/ytmc-insights-artist/div[2]/div[3]/div[3]/ytmc-rankings-card/div/div[4]/ytmc-view-more-dialog/paper-dialog/paper-dialog-scrollable/div/div/ytmc-entity-row[{}]/div/div/div[2]/div[2]/ytmc-ellipsis-text'.format(block)
                ).get_attribute('aria-label')
                .replace('Views ','')
                .replace(',','')
            )
        row.append(country)
        row.append(int(view_amt))
        length = len(countries_view_df)
        countries_view_df.loc[length] = row

        return countries_view_df

def get_artist_100():
    """
    - Use Billboard API to retrieve Taylor Swift position on Artist 100 each week

    Arguments:
        None

    Returns:
        Table of data on this website: https://charts.youtube.com/artist/%2Fm%2F0dl567?hl=vi
    """
    #Create dataframe
    artist_100_df = pd.DataFrame(columns = ['date','taylor_pos'])
    artist_100_df

    #Create list of date
    time_range = pd.date_range(
        start = '2014-07-16', #Artist 100 start at 2014-07-16
        end = datetime.today(),
        freq = 'W-SAT'
    )
    date_range = []
    for timestamp in time_range:
        date = (str(timestamp).replace(' 00:00:00',''))
        date_range.append(date)
    
    # Extract Taylor's position in Artist 100
    for week in date_range:
        row = [week]
        chart = billboard.ChartData('artist-100', date = week)
        artist_list = []
        for pos, artist in enumerate(chart, 1):
            artist_list.append(artist.artist)
            if artist.artist == 'Taylor Swift':
                row.append(pos)
                break
        if 'Taylor Swift' not in artist_list:
            row.append(np.nan)
        length = len(artist_100_df)
        artist_100_df.loc[length] = row
    
    return artist_100_df