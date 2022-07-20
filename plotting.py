import pandas as pd


def get_videos_per_h_series(df, channel_name):
    df_for_channel = df.loc[df["channel_name"] == channel_name]
    # get hours from datetime
    get_hs = pd.DatetimeIndex(df_for_channel['time']).hour
    # count on how many videos you clicked and sort hours from 0 to 23
    count_videos_per_h = get_hs.value_counts().sort_index()
    hs_of_the_day = [h for h in range(0, 24)]
    # get full range of x values from 0 to 23
    series = pd.Series(count_videos_per_h, hs_of_the_day)
    # change NaN to 0
    series = series.fillna(0)
    # change dtype to int and return
    return series.astype(int)   


def one_channel_bar_plot_videos_per_h(series, channel_name):
    series = get_videos_per_h_series(series, channel_name)
    series.plot.bar(color="purple", rot=0,
                    title=f"{channel_name}",
                    xlabel="hour", ylabel="videos per hour")
