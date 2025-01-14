# Format for plot is __PLOT_PREFIX{dictionary of settings}[[x axis], [y axis]]

# Format for attribute is __ATTRIBUTE_PREFIXattribute(parameters)

__PLOT_PREFIX = '%matplotlibdata --'
__LONG_PLOT_PREFIX = '%matplotlibdatalongSTART --'
__LONG_PLOT_SUFFIX = '%matplotlibdatalongEND'
__ATTRIBUTE_PREFIX = '%matplotlib --'  # Prefix to recognize attribute

from ulab import numpy as np
import binascii


def liveplot(*args, labels=None):
    """
    """
    if labels:
        if isinstance(labels, list) and len(args) == len(labels):
            pass
        elif isinstance(labels, str) and len(args) == 1:
            pass
        else:
            raise ValueError("Please input a number of labels equal to the amount of data points to plot.")
    else:
        labels = ['l{}'.format(ii) for ii, _ in enumerate(args)]

    out = ['{} {}'.format(label, arg) for arg, label in zip(args, labels)]
    out = ' '.join(out)
    print(out)


def axhline(y=0, xmin=0, xmax=1, **kwargs):
    """
    Add a horizontal line across the axis.
    Parameters
    ----------
    y : float, default: 0
        y position in data coordinates of the horizontal line.
    xmin : float, default: 0
        Should be between 0 and 1, 0 being the far left of the plot, 1 the
        far right of the plot.
    xmax : float, default: 1
        Should be between 0 and 1, 0 being the far left of the plot, 1 the
        far right of the plot.
    Returns
    -------
    `~matplotlib.lines.Line2D`
    Other Parameters
    ----------------
    **kwargs
        Valid keyword arguments are `.Line2D` properties, with the
        exception of 'transform':
        %(Line2D:kwdoc)s
    See Also
    --------
    hlines : Add horizontal lines in data coordinates.
    axhspan : Add a horizontal span (rectangle) across the axis.
    axline : Add a line with an arbitrary slope.
    Examples
    --------
    * draw a thick red hline at 'y' = 0 that spans the xrange::
        >>> axhline(linewidth=4, color='r')
    * draw a default hline at 'y' = 1 that spans the xrange::
        >>> axhline(y=1)
    * draw a default hline at 'y' = .5 that spans the middle half of
        the xrange::
        >>> axhline(y=.5, xmin=0.25, xmax=0.75)
    """
    kwargs['y'] = y
    kwargs['xmin'] = xmin
    kwargs['xmax'] = xmax
    args = ()

    print(__ATTRIBUTE_PREFIX + 'axhline' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def axvline(x=0, ymin=0, ymax=1, **kwargs):
    """
    Add a vertical line across the Axes.
    Parameters
    ----------
    x : float, default: 0
        x position in data coordinates of the vertical line.
    ymin : float, default: 0
        Should be between 0 and 1, 0 being the bottom of the plot, 1 the
        top of the plot.
    ymax : float, default: 1
        Should be between 0 and 1, 0 being the bottom of the plot, 1 the
        top of the plot.
    Returns
    -------
    `~matplotlib.lines.Line2D`
    Other Parameters
    ----------------
    **kwargs
        Valid keyword arguments are `.Line2D` properties, with the
        exception of 'transform':
        %(Line2D:kwdoc)s
    See Also
    --------
    vlines : Add vertical lines in data coordinates.
    axvspan : Add a vertical span (rectangle) across the axis.
    axline : Add a line with an arbitrary slope.
    Examples
    --------
    * draw a thick red vline at *x* = 0 that spans the yrange::
        >>> axvline(linewidth=4, color='r')
    * draw a default vline at *x* = 1 that spans the yrange::
        >>> axvline(x=1)
    * draw a default vline at *x* = .5 that spans the middle half of
        the yrange::
        >>> axvline(x=.5, ymin=0.25, ymax=0.75)
    """
    kwargs['x'] = x
    kwargs['ymin'] = ymin
    kwargs['ymax'] = ymax
    args = ()

    print(__ATTRIBUTE_PREFIX + 'axvline' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def show():
    raise NotImplementedError('matplotlib.pyplot.show is not implemented yet for ALPACA.')


def pause():
    raise NotImplementedError('matplotlib.pyplot.pause is not implemented yet for ALPACA.')


def figure(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.figure is not implemented yet for ALPACA.')


def close(fig=None):
    """
    Close a figure window.
    """
    raise NotImplementedError('matplotlib.pyplot.close is not implemented yet for ALPACA.')


def clf():
    """Clear the current figure."""
    raise NotImplementedError('matplotlib.pyplot.clf is not implemented yet for ALPACA.')


def draw():
    raise NotImplementedError('matplotlib.pyplot.draw is not implemented yet for ALPACA.')


def savefig(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.savefig is not implemented yet for ALPACA.')


def cla():
    """Clear the current axes."""
    raise NotImplementedError('matplotlib.pyplot.cla is not implemented yet for ALPACA.')


def subplot(*args, **kwargs):
    """Add an Axes to the current figure or retrieve an existing Axes."""
    raise NotImplementedError('matplotlib.pyplot.subplot is not implemented yet for ALPACA.')


# Plotting should happen via pyplot
def subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True,
             subplot_kw=None, gridspec_kw=None, **fig_kw):
    """
    Create a figure and a set of subplots.
    """
    raise NotImplementedError(
        'matplotlib.pyplot.subplots is not implemented yet for ALPACA. Instead, please use matplotib.pyplot.plot')


def xlim(*args, **kwargs):
    """
    Get or set the x limits of the current axes.
    Call signatures::
        left, right = xlim()  # return the current xlim
        xlim((left, right))   # set the xlim to left, right
        xlim(left, right)     # set the xlim to left, right
    If you do not specify args, you can pass *left* or *right* as kwargs,
    i.e.::
        xlim(right=3)  # adjust the right leaving left unchanged
        xlim(left=1)  # adjust the left leaving right unchanged
    Setting limits turns autoscaling off for the x-axis.
    Returns
    -------
    left, right
        A tuple of the new x-axis limits.
    Notes
    -----
    Calling this function with no arguments (e.g. ``xlim()``) is the pyplot
    equivalent of calling `~.Axes.get_xlim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xlim` on the current axes. All arguments are passed though.
    """
    print(__ATTRIBUTE_PREFIX + 'xlim' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def ylim(*args, **kwargs):
    """
    Get or set the y-limits of the current axes.
    Call signatures::
        bottom, top = ylim()  # return the current ylim
        ylim((bottom, top))   # set the ylim to bottom, top
        ylim(bottom, top)     # set the ylim to bottom, top
    If you do not specify args, you can alternatively pass *bottom* or
    *top* as kwargs, i.e.::
        ylim(top=3)  # adjust the top leaving bottom unchanged
        ylim(bottom=1)  # adjust the bottom leaving top unchanged
    Setting limits turns autoscaling off for the y-axis.
    Returns
    -------
    bottom, top
        A tuple of the new y-axis limits.
    Notes
    -----
    Calling this function with no arguments (e.g. ``ylim()``) is the pyplot
    equivalent of calling `~.Axes.get_ylim` on the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_ylim` on the current axes. All arguments are passed though.
    """
    print(__ATTRIBUTE_PREFIX + 'ylim' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def xticks(ticks=None, labels=None, **kwargs):
    """
    Get or set the current tick locations and labels of the x-axis.
    Pass no arguments to return the current values without modifying them.
    Parameters
    ----------
    ticks : array-like, optional
        The list of xtick locations.  Passing an empty list removes all xticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.
    Returns
    -------
    locs
        The list of xtick locations.
    labels
        The list of xlabel `.Text` objects.
    Notes
    -----
    Calling this function with no arguments (e.g. ``xticks()``) is the pyplot
    equivalent of calling `~.Axes.get_xticks` and `~.Axes.get_xticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_xticks` and `~.Axes.set_xticklabels` on the current axes.
    """

    kwargs['ticks'] = ticks
    kwargs['labels'] = labels
    args = ()

    print(__ATTRIBUTE_PREFIX + 'xticks' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def yticks(ticks=None, labels=None, **kwargs):
    """
    Get or set the current tick locations and labels of the y-axis.
    Pass no arguments to return the current values without modifying them.
    Parameters
    ----------
    ticks : array-like, optional
        The list of ytick locations.  Passing an empty list removes all yticks.
    labels : array-like, optional
        The labels to place at the given *ticks* locations.  This argument can
        only be passed if *ticks* is passed as well.
    **kwargs
        `.Text` properties can be used to control the appearance of the labels.
    Returns
    -------
    locs
        The list of ytick locations.
    labels
        The list of ylabel `.Text` objects.
    Notes
    -----
    Calling this function with no arguments (e.g. ``yticks()``) is the pyplot
    equivalent of calling `~.Axes.get_yticks` and `~.Axes.get_yticklabels` on
    the current axes.
    Calling this function with arguments is the pyplot equivalent of calling
    `~.Axes.set_yticks` and `~.Axes.set_yticklabels` on the current axes.
    """
    kwargs['ticks'] = ticks
    kwargs['labels'] = labels
    args = ()

    print(__ATTRIBUTE_PREFIX + 'yticks' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def polar(*args, **kwargs):
    """Make a polar plot."""
    raise NotImplementedError('matplotlib.pyplot.polar is not implemented yet for ALPACA.')


def errorbar(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.errorbar is not implemented yet for ALPACA.')


def grid(*args, **kwargs):
    print(__ATTRIBUTE_PREFIX + 'grid' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def hist(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.hist is not implemented yet for ALPACA.')


def hlines(y, xmin, xmax, colors=None, linestyles='solid', label='', data=None, **kwargs):
    kwargs['colors'] = colors
    kwargs['linestyles'] = linestyles
    kwargs['label'] = label
    kwargs['data'] = data

    args = (y, xmin, xmax)

    print(__ATTRIBUTE_PREFIX + 'hlines' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def legend(*args, **kwargs):
    print(__ATTRIBUTE_PREFIX + 'legend' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def loglog(*args, **kwargs):
    raise NotImplementedError(
        'matplotlib.pyplot.loglog is not implemented yet for ALPACA. Please use xscale and yscale.')


def pie(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.pie is not implemented yet for ALPACA.')


def plot(*args, scalex=True, scaley=True, data=None, **kwargs):
    # Format for string is {dictionary of settings}[[x axis], [y axis]]
    # xx_uc_byte = np.array(args[0], dtype=np.float).tobytes()

    good_args = _count_axes_in_args(args)

    if len(args) - good_args > 0:  # add fmt string to kwargs if present:
        kwargs['fmt'] = args[2]
    else:
        kwargs['fmt'] = ''

    kwargs['scalex'] = scalex
    kwargs['scaley'] = scaley
    kwargs['data'] = data

    _send_small_plot(kwargs, _get_x_and_y_from_args(args, good_args))



def _send_large_plot(kwargs, xx, yy):
    yy_shape = yy.shape
    data = list(_get_plot_data_as_hex(xx, yy))
    print(__LONG_PLOT_PREFIX + str(kwargs) + '[[', end='')
    stop = len(data[0])
    for ii in range(2):  # Do X then Y
        jj = 0
        while True:
            if stop - jj >= 1000:
                print(data[ii][jj:jj + 1000], end='')
                jj += 1000
            else:
                print(data[jj:], end='')
                break

        if ii == 0:
            print('], [', end='')  # Spacer between X and Y
    print(']]' + str(yy_shape) + __LONG_PLOT_SUFFIX)


def _count_axes_in_args(args):
    return sum([isinstance(arg, (np.ndarray, list)) for arg in args])


def _get_x_and_y_from_args(args, good_args):
    args = list(args)
    if not isinstance(args[0], (list, np.ndarray, tuple)):
        raise ValueError('x must be an array')

    if good_args == 1:  # Just X specified
        args[0] = np.array(args[0], dtype=_get_dtype_if_array(args[0]))
        args = args[:1]
        args.append(np.arange(len(args[0]), dtype=_get_dtype_if_array(args[0])))

    else:  # X and Y specified
        if not isinstance(args[1], (list, np.ndarray, tuple)):
            raise ValueError('y must be an array')
        if len(args[0]) != len(args[1]):
            raise ValueError('x and y must be the same size')

        args[0] = np.array(args[0], dtype=_get_dtype_if_array(args[0]))
        args[1] = np.array(args[1], dtype=_get_dtype_if_array(args[1]))
        args = args[0:2]

    return args


def _get_dtype_if_array(array):
    if isinstance(array, np.ndarray):
        yy_type = array.dtype
    else:
        yy_type = np.float
    return yy_type


def _send_small_plot(kwargs, args):
    try:
        yy_shape = args[1].shape

        string = '{}{}[[{}{}]]{}'.format(__PLOT_PREFIX, kwargs, *_get_plot_data_as_hex(args), yy_shape)
        print(string)
    except MemoryError as e:
        raise MemoryError("It seems that the plot you requested is too big for the ALPACA. Try plotting a subset of "
                          "the points. You might want to do this by slicing a numpy array every N points.") from e

def _get_plot_data_as_hex(args):
    args[0] = args[0].tobytes()
    args[1] = args[1].tobytes()

    args[0] = str(binascii.hexlify(args[0]), 'utf-8')

    args[1] = str(binascii.hexlify(args[1]), 'utf-8')

    return args


def scatter(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.scatter is not implemented yet for ALPACA.')


def violinplot(*args, **kwargs):
    raise NotImplementedError('matplotlib.pyplot.violinplot is not implemented yet for ALPACA.')


def vlines(
        x, ymin, ymax, colors=None, linestyles='solid', label='', *, data=None, **kwargs):
    args = (x, ymin, ymax)

    kwargs['colors'] = colors
    kwargs['linestyles'] = linestyles
    kwargs['label'] = label
    kwargs['data'] = data

    print(__ATTRIBUTE_PREFIX + 'vlines' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def title(label, fontdict=None, loc=None, pad=None, *, y=None, **kwargs):
    args = (label)

    kwargs['fontdict'] = fontdict
    kwargs['loc'] = loc
    kwargs['pad'] = pad
    kwargs['y'] = y

    print(__ATTRIBUTE_PREFIX + 'title' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    args = (xlabel)

    kwargs['fontdict'] = fontdict
    kwargs['labelpad'] = labelpad
    kwargs['loc'] = loc

    print(__ATTRIBUTE_PREFIX + 'xlabel' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def ylabel(ylabel, fontdict=None, labelpad=None, *, loc=None, **kwargs):
    args = (ylabel)

    kwargs['fontdict'] = fontdict
    kwargs['labelpad'] = labelpad
    kwargs['loc'] = loc

    print(__ATTRIBUTE_PREFIX + 'ylabel' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def xscale(value, **kwargs):
    args = (value)

    print(__ATTRIBUTE_PREFIX + 'xscale' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')


def yscale(value, **kwargs):
    args = (value)

    print(__ATTRIBUTE_PREFIX + 'xscale' + '(' + str(args).replace('(', '').replace(')', '') + ', ' + str(kwargs) + ')')
