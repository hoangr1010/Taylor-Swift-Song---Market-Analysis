# Taylor Swift Song & Market Analysis
## Project Summary

### Project Motivation
- I am a new audience of Taylor Swift music, I find that she is really famous in music industry for a decade. because of curiosity, I decide to collect and analyse data to understand how she famous and what her music style actually is based on time series.

### Planning
#### How I decide what data to collect:
- I collect data based on hierarchical order: How Taylor Swift in the world -> music market -> her album -> her song > her song feature/genres

#### Pre-analysis questions and hypothesis
- Before analyse, I determine some of question or hypothesis about Taylor Swift:
    - She is a big music star around the world, so how her audience distribute around the world?
    - I assume that her position in Billboard chart should be affected by her new release, it means each time she release new tracks/album, she will be on top of the chart.
    - She is considered as pop star, her music is all pop or having another kind of music?
    - Because she is a big star in the industry, her tracks should mostly be on the Billboard chart, some of them are on top
    - What is her music style? (I will use song feature that describe 3 main aspects in her music: Energy, Acousticness, Musical positiveness)
- At the end of this project, all questions and hypothesis will be answer by data plotted on Tableau.


## The project follow steps:
- Step 1: collect and clean data
- Step 2: Create Tableau interactive dashboard and static report

## Step 1: Data enrichment
There are some type of data sources I use in this project to enrich my data
#### Main dataset:
- Data collect method: Read Step 1 and Step 2 in Readme.md https://github.com/hoangr1010/Song-Analysis
- This data set includes: song, album, album release date, song feature, popularity, song genres
- Sources: Spotify, LastFM

#### Views amount by country for last 12 months:
- Data collect method: use selenium to scrape data 
- This data set includes: Country_name, views amount for last 12 months
- Sources: Youtube Music Chart

#### Taylor Swift on Artist 100 (Billboard chart for artist):
- Data collect method: use Billboard API to request data
- This data set includes: Week, Taylor position on chart
- Source: Billboard chart - Artist 100

#### Taylor's song on Hot 100 (Billboard chart for song):
- Data collect method: use BeautifulSoup to scrape the data
- This data set includes: song name,debut date,peak position,peak date,weeks on Chart
- Source: Billboard chart - Hot 100

###### Note: all dataset I used for this project placed on dataset folder. song_df_join_hot_100 is dataset I left join between song_df and hot_100_df

## Step 2: Create Tableau interactive dashboard and static report
- At the end, I create a report to answer all question at outset. I store it in png file above.
- You also can explore more insight about Taylor Swift market and song through this interactive dashboard: https://public.tableau.com/app/profile/nguyen.huu.huy.hoang/viz/TaylorSwiftMarketandSongAnalysis/MainDashboard?publish=yes
