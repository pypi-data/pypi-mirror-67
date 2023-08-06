# -*- coding: utf-8 -*-
# whatsapp-stats
# Copyright (C) 2016  Lucas Rodés

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This import makes Python use 'print' as in Python 3.x
from __future__ import print_function

import plotly.graph_objs as go


def vis(user_data, title):
    """Obtain Figure to plot using plotly.

    Does not work if you use date_mode='hourweekday'.

    Args:
        user_data (pandas.DataFrame): Input data.
        title (str): Title of figure.
    
    Returns:
        dict: Figure.

    Example:

        ```python
        >>> from whatstk import WhatsAppChat, interventions
        >>> filename = 'path/to/samplechat.txt'
        >>> chat = WhatsAppChat.from_txt(filename)
        >>> counts = interventions(chat=chat, date_mode='date', msg_length=False)
        >>> counts_cumsum = counts.cumsum()
        >>> from plotly.offline import plot
        >>> from whatstk.plot import vis
        >>> plot(vis(counts_cumsum, 'cumulative number of messages sent per day'))
        ```

    """
    # Create a trace
    data = []

    for username in user_data:
        trace = go.Scatter(
            x=user_data.index,
            y=user_data[username],
            showlegend=True,
            name=username,
            text=user_data.index
        )
        data.append(trace)

    layout = dict(title=title, xaxis=dict(title = 'Date'))

    return dict(data=data, layout=layout)