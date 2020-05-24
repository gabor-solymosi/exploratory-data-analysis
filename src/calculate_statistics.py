# -*- coding: utf-8 -*-
"""
A function calculating simple statistics from a data frame,
created by Gabor on 2 Feb 2020.
"""

import pandas as pd


def calculate_statistics(data):
    """ Calculate statistics for every column in the data set and output the resulting stats data frame

    Parameters
    ----------
    data : pandas DataFrame

    Returns
    -------
    stats : pandas DataFrame

    """
    stats = pd.DataFrame()

    stats_cols = ["column", "dtype", "min", "max", "mean", "sd", "cardinality"]

    for column in data:
        print("Calculating statistics of column:", column)

        stats_col = pd.DataFrame()

        desc = data[column].describe()

        try:
            if data[column].dtype == "object":

                if ("date" in column.lower()) or ("time" in column.lower()):
                    desc = pd.to_datetime(data[column]).describe()

                    stats_col = pd.DataFrame.from_records([{"column": column,
                                                            "dtype": data[column].dtype,
                                                            "min": desc["first"],
                                                            "max": desc["last"],
                                                            "mean": "NA",
                                                            "sd": "NA",
                                                            "cardinality": desc["unique"]}])

                else:
                    stats_col = pd.DataFrame.from_records([{"column": column,
                                                            "dtype": data[column].dtype,
                                                            "min": "NA",
                                                            "max": "NA",
                                                            "mean": "NA",
                                                            "sd": "NA",
                                                            "cardinality": desc["unique"]}],
                                                          columns=stats_cols)

            elif data[column].dtype in ["int64", "float64", "bool"]:

                stats_col = pd.DataFrame.from_records([{"column": column,
                                                        "dtype": data[column].dtype,
                                                        "min": desc["min"],
                                                        "max": desc["max"],
                                                        "mean": desc["mean"],
                                                        "sd": desc["std"],
                                                        "cardinality": desc["unique"]}],
                                                      columns=stats_cols)

            else:
                stats_col = pd.DataFrame.from_records([{"column": column,
                                                        "dtype": data[column].dtype,
                                                        "min": "NA",
                                                        "max": "NA",
                                                        "mean": "NA",
                                                        "sd": "NA",
                                                        "cardinality": "NA"}],
                                                      columns=stats_cols)

        except:
            stats_col = pd.DataFrame.from_records([{"column": column,
                                                    "dtype": data[column].dtype,
                                                    "min": "NA",
                                                    "max": "NA",
                                                    "mean": "NA",
                                                    "sd": "NA",
                                                    "cardinality": "NA"}],
                                                  columns=stats_cols)

        stats = stats.append(stats_col, ignore_index=True)[stats_cols]

        print("\n")

    return stats
