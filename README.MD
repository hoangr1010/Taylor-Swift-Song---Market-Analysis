# Taylor Swift Song & Market Analysis
## Project Summary

### Goal of Project 
- This project based on the data I extracted from previous project - Song Analysis, where I analyse only Taylor Swift song and its popularity currently, to give a more general and insightful on her song and market by data enrichment
- This project also provide interactive dashboard about Taylor Swift song and market. 

The project follow steps:
- Step 1: Data enrichment
- Step 2: Create Tableau interactive dashboard and static report

## Step 1: Data enrichment
There are some type of data sources I use in this project to enrich my data
#### Main dataset:
- Data collect method: https://github.com/hoangr1010/Song-Analysis
- This data set includes: song, album, album release date, song feature, popularity, song genres
- Sources: Spotify, LastFM

#### Views amount by country for last 12 months:
- Data collect method: use selenium to scrape data 
- This data set includes: Country_name, views amount for last 12 months
- Sources: Youtube Music Chart

#### Taylor Swift on Artist 100 (Billboard chart for artist)
- Data collect method: use Billboard API to request data
- This data set includes: Week, Taylor position on chart
- Source: Billboard chart - Artist 100

#### Taylor's song on Hot 100 (Billboard chart for song)
- Data collect method: use BeautifulSoup to scrape the data
- This data set includes: song name,debut date,peak position,peak date,weeks on Chart
- Source: Billboard chart - Hot 100

###### Note: all dataset I used for this project placed on dataset folder. song_df_join_hot_100 is dataset I left join between song_df and hot_100_df

## Step 2: Create Tableau interactive dashboard and static report
- Link Dashboard: https://public.tableau.com/app/profile/nguyen.huu.huy.hoang/viz/TaylorSwiftMarketandSongAnalysis/MainDashboard?publish=yes
- I also create general report, it's included on png file
/Users/hoanglui/Library/Mobile Documents/com~apple~CloudDocs/Environment/Project/Taylor Swift Song & Market Analysis/Song_Analysis(2)/TaylorSwift_Report.png
