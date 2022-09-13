import pandas as pd


def get_videos_per_h(df, channel_name):
    if not channel_name:
        get_hs = pd.DatetimeIndex(df['time']).hour
    else:
        df_for_channel = df.loc[df["channel_name"] == channel_name]
        # get hours from datetime
        get_hs = pd.DatetimeIndex(df_for_channel['time']).hour
    # count on how many videos you clicked and sort hours from 0 to 23
    count_videos_per_h = get_hs.value_counts().sort_index()
    # get full range of x values from 0 to 23
    hs_of_the_day = [h for h in range(0, 24)]
    series = pd.Series(count_videos_per_h, hs_of_the_day)
    # change NaN to 0
    series = series.fillna(0)
    # change dtype to int and return
    return series.astype(int)


def h_bar_plot(df, channel_name=""):
    series = get_videos_per_h(df, channel_name)
    series.plot.bar(color="purple", rot=0,
                    title=f"{channel_name}",
                    xlabel="hour", ylabel="videos per hour")


def month_bar_plot(df, channel_name=""):
    series = get_videos_per_month(df, channel_name)
    series.plot.bar(color="purple", rot=0,
                    title=f"{channel_name}",
                    xlabel="hour", ylabel="videos per month")


def get_videos_per_month(df, channel_name):
    if not channel_name:
        # Per every row get month of recording. Then count values
        videos_per_month = df['time'].dt.strftime('%b').value_counts()
    else:
        df_for_channel = df.loc[df["channel_name"] == channel_name]
        videos_per_month = df_for_channel['time'].dt.strftime('%b').value_counts()
    str_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # Add empty months
    videos_per_month = videos_per_month.reindex(str_months, axis=0)
    # Change NaN in those empty months to 0. Then change dtype to int
    return videos_per_month.fillna(0).astype(int)
