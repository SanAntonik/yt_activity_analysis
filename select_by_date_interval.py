def select_by_date_interval(df, start, end=""):
    """
    Summary:
        Select a subset of a df based on the specified
        time interval

    Important 1:
        Input points of the interval
        must be in the year-month-day format.
        For example, 2022-07-15 that corresponds to
        July 15, 2022

    Important 2:
        Right part of the interval is not included.
        For example, if you choose interval from 2022-07-15
        to 2022-07-28, you won't get the last day (2022-07-28).
        Therefore, take one day more on the right interval edge.
        If you want to include an entire month, set your right date
        to the start of the next month. For example, to include
        entire September 2022,  set left date to 2022-09-01 and
        right date to 2022-10-01

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
    mask = (df['time'] >= start) & (df['time'] < end)
    return df.loc[mask]
