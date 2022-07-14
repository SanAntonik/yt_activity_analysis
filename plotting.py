import pandas as pd


def plot_videos_per_h(df, channel_to_plot):
    df_for_channel = df.loc[df["channel_name"] == channel_to_plot]
    # get hours from datetime
    get_hs = pd.DatetimeIndex(df_for_channel['time']).hour
    # count on how many videos you clicked and sort hours from 0 to 23
    count_videos_per_h = get_hs.value_counts().sort_index()
    hs_of_the_day = [h for h in range(0, 24)]
    # get full range of x values from 0 to 23
    series = pd.Series(count_videos_per_h, hs_of_the_day)
    # change NaN to 0
    series = series.fillna(0)
    # change dtype to int
    series = series.astype(int)
    series.plot.bar(color="purple", rot=0,
                    title=f"{channel_to_plot}",
                    xlabel="hour", ylabel="videos per hour")
