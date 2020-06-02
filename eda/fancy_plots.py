# -*- coding: utf-8 -*-
"""
Functions to produce fancy(er) charts with Seaborn,
created by Gabor on 2 Feb 2020.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def hist_plot(data, x, title=None, custom_labels=None):
    """ Create a fancy histogram plot

    Parameters
    ----------
    data : pandas DataFrame or list
    x : str or list of strings
        Column name(s)
    title : str, optional
        Chart title
    custom_labels : list, optional

    Returns
    -------
    plot

    """
    sns.set(font_scale=1.3)
    f, (ax) = plt.subplots(1, 1, figsize=(15, 6))
    f.suptitle(title, fontsize=18)

    if isinstance(data, pd.DataFrame):

        if isinstance(x, str):
            sns.distplot(data[x], kde=False)

        elif isinstance(x, list):
            for i in x:
                sns.distplot(data[i], kde=False, label=i)

            plt.legend()

    if isinstance(data, list):

        if isinstance(x, str):

            if custom_labels is not None:
                for d, lab in zip(data, custom_labels):
                    sns.distplot(d[x], kde=False, label=lab)

                plt.legend()

            else:
                sns.distplot(data[x], kde=False)

        elif isinstance(x, list):

            if custom_labels is not None:
                for d, lab in zip(data, custom_labels):
                    for i in x:
                        sns.distplot(d[i], kde=False, label="{i} for {lab}".format(i=i, lab=lab))

                plt.legend()


def box_plot(data, x, y=None, title=None, axis_max=None, rotate_labels=False, rotation=45, orient='v'):
    """ Create a fancy box plot

    Parameters
    ----------
    data : pandas DataFrame
    x : str
        column name
    y : str, optional
        Categorical column name
    title : str, optional
        Chart title
    axis_max : int, optional
        Maximum number on each axis
    rotate_labels : bool, optional
        Rotate labels on x axis or not
    rotation : int, optional
        Degree of rotation
    orient : str, optional
        'v' for vertical, 'h' for horizontal chart

    Returns
    -------
    plot

    """
    sns.set(font_scale=1.3)  # Bigger font size
    f, (ax) = plt.subplots(1, 1, figsize=(15, 6))
    f.suptitle(title, fontsize=18)

    sns.boxplot(x=x, y=y, data=data, ax=ax, orient=orient)

    # Cut the extreme outliers if needed
    if axis_max is not None:
        if orient == 'v':
            plt.ylim(0, axis_max)
        elif orient == 'h':
            plt.xlim(0, axis_max)

    # Rotate x axis labels
    if rotate_labels:
        for label in ax.get_xticklabels():
            label.set_rotation(rotation)


def scatter_plot(data, x, y, title=None):
    """ Create a fancy scatter plot

    Parameters
    ----------
    data : pandas DataFrame
    x : str
        x axis column name
    y : str
        y axis column name
    title: str, optional
        Chart title

    Returns
    -------
    plot

    """
    sns.set(font_scale=1.3)  # Bigger font size
    f, (ax) = plt.subplots(1, 1, figsize=(15, 6))
    f.suptitle(title, fontsize=18)

    sns.scatterplot(data[x], data[y])
