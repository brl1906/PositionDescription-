import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

class Error(Exception):
    """Base class for throwing exceptions"""
    pass

class ValuesDontSumTo100(Error):
    """Workplan values fail to sum to 100."""
    pass

class ValuesNotTypeInt(Error):
    """Workplan values not all type int."""
    pass

class InvalidParameterType(Error):
    """Value passed to workplan parameter not type dict."""
    pass

def validate_workplan(workplan):
    """Checks whether the percentages associated with job tasks total to 100. 
    
    Parameters
    ----------
    workplan:  Dict
            Dictionary with key, value pairs for the job task or compentency area and 
            the percentage of time anticipated or necessary to be spent in tha area for the 
            job.  Example: {'memo writing':20, 'answering phones':20, 'drinking coffee':60}
    
    Returns
    -------
    Boolean:  Returns True if sum of values is 100, Raises error if not. 
    """
    
    if isinstance(workplan, dict):
        
        if all(type(value) is int for value in workplan.values()):
            
            if sum(workplan.values()) == 100:
                return True
   
            else:
                error_msg = 'The workplan parameter values should total 100, instead sums to {}.'.format(sum(workplan.values()))
                raise ValuesDontSumTo100(error_msg)
        else:
            
            error_msg = ('All workplan values must be integers, instead received type(s): {}.'
                         .format([type(value) for value in workplan.values() if not isinstance(value, int)]))
            raise ValuesNotTypeInt(error_msg)
    
    else:
        error_msg = 'The workplan parameter expects a dictionary, but received {}.'.format(type(workplan))
        raise InvalidParameterType(error_msg)
        


        
## TODO: style hovertext to show workarea: BPM <br> pct: 23%  formatting

def position_radarchart(job_title, workplan):
    """Creates radar chart for a position to visualize the percentage of time 
    and effort required to be spent in each competency or task area for a job.
    
    Parameters
    ----------
    position: str
            Job title. Name of position to be advertised. For example: Auto Mechanic II, 
            Energy Analyst I or Grant Specialist
    
    workplan: dict
            Dictionary with key, value pairs for the job task or compentency area and 
            the percentage of time anticipated or necessary to be spent in that area to successfully  
            execute the job. 
             
        
    Returns
    -------
    Dict:   Plotly figure dictionary with keys: 'data' and 'layout'

    
    Example
    -------
    >>> position_radarchart(position='Secretary II', workplan=work_tasks)
    
    >>> position_radarchart(job, responsibilities)
    """
    
    if validate_workplan(workplan):
        
        try:
            
            responsibilities = list(workplan.keys())
            r_values = list(workplan.values())
            axis_range = [0,(max(r_values) + 5)]


            data = [go.Scatterpolar(
            r = r_values,
            theta = responsibilities,
            fill = 'toself',
            fillcolor = '#a1d99b',
            line = {'color':'#a1d99b'},
            #hoverinfo = 'r+theta'
            )]

            layout = {
                'title':'{}<br>Responsibilities'.format(job_title),
                'font':{'color':'#a1d99b'},
                'polar':{
                    'radialaxis':{'visible':True,
                                 'color':'black',
                                 'linecolor':'green',
                                 'range': axis_range} 
                },
                'showlegend':False,
                'hovermode':'closest'
            }

            fig = {'data':data, 'layout':layout}
            return fig
        
        except Exception as e:
            return e
    
    else:
        error_msg = 'The workplan parameter expects a dictionary, but received {}.'.format(type(workplan))
        raise InvalidParameterType(error_msg)

        

def publish_chart(job, fileoption='overwrite'):
    """Generates Plotly chart, pushing to account and returning the chart url as a string.
    
    Parameters 
    ----------
    job:        instance of class Position  
            The object contains the core common elements of a work position to be advertised and recruited for.
    
    fileoption: str
            The option for how Plotly should handle future calls to the function for the same chart. Valid
            values include: 'new', 'overwrite', 'extend', and 'append'. They have the following actions: 
            ('new' | 'overwrite' | 'extend' | 'append') -- 'new' creates a
            'new': create a new, unique url for this plot
            'overwrite': overwrite the file associated with `filename` with this
            'extend': add additional numbers (data) to existing traces
            'append': add additional traces to existing data lists        
    
    Returns
    -------
    str:    Returns the url to the generated Plotly chart.  
    
    Example
    -------
    >>>  publish_chart(executive_fellowship)
    
    >>>  publish_chart(job=grant_specialist, fileoption='new')
    """
    
    try:
        figure = position_radarchart(job.title, job.workplan)
        filename = '{}-posting'.format(job.title.lower().replace(' ','-'))
    
        return py.plot(figure, filename, fileopt=fileoption, auto_open=False)
    
    except Exception as e:
        raise e
