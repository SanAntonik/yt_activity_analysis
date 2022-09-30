import pandas as pd


def prepare_data(PATH):
    """
    Summary:
        Load json data and prepare it for further actions

    Args:
        path (str): path to your data

    Returns:
        df (df): DataFrame
    """
    # Load data and convert time
    df = pd.read_json(PATH, convert_dates=['time'])
    # Change timezone from UTC to mine
    df["time"] = df["time"].dt.tz_convert('Europe/Kiev')
    # Drop unimportant columns
    df.drop(["titleUrl", "products", "activityControls",
            "description", "details"], axis=1, inplace=True)
    # Remove "Watched " from every row of column "title"
    df["title"] = [i[8:] for i in df['title']]
    # Remove rows where column 'subtitles' contains NaN
    df = df[df["subtitles"].notna()]
    # Reset df index
    df = df.reset_index(drop=True)
    # Create a new col with channels names inside based on 'subtitles' col
    df["channel_name"] = [df["subtitles"][row][0]["name"]
                          for row in range(df.shape[0])]
    # Remove ' - Topic' from the names of YouTube Mucis channels
    df["channel_name"] = df["channel_name"].str.replace(" - Topic", "")
    # Drop not needed now 'subtitles' col
    df.drop(["subtitles"], axis=1, inplace=True)
    # Change dtypes of cols 'title' and 'channel_name' from object to string
    colnames = ["title", "channel_name"]
    df[colnames] = df[colnames].astype("string")
    # Rename col 'title' to 'video_title' and col 'header' to 'app'
    df.rename(columns={"title": "video_title", "header": "app"}, inplace=True)
    # Rearrange order of columns
    cols = df.columns.tolist()
    cols = [cols[1]] + [cols[3]] + [cols[2]] + [cols[0]]
    df = df[cols]
    return df


def select_by_date_interval(df, start, end=""):
    """
    Summary:
        Select a subset of a df based on the specified
        time interval.
        Important: input points of the interval
        must be in the year-month-day format.
        For example, 2022-07-15 that corresponds to
        July 15, 2022

    Args:
        df (df): DataFrame
        start (str): start date
        end (str, optional): end date. Defaults to "".

    Returns:
        df (df): subset of input DataFrame
    """
    # check whether you passed the starting date
    if not start:
        raise ValueError("You didn't specify the starting point")
    # if you didn't pass the ending date, use the most recent one
    if not end:
        end = df["time"].iloc[0]
    mask = (df['time'] > start) & (df['time'] <= end)
    return df.loc[mask]
