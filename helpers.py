"""
"""

import yaml

class Position:
    """The object contains the core common elements of a work position to be advertised and recruited for.
    
    Attributes
    ----------
    title (str): The name of the position or job title
    
    about_job (str): The descriptive or background text about the position.
    
    about_org (str): The description and background about the agency or office.
    
    workplan (dict): Dictionary with key, value pairs for the job task or compentency area and 
            the percentage of time anticipated or necessary to be spent in that area to successfully  
            execute the job.
    
    """
    def __init__(self, title, about_job, workplan):
        """The constructor for the job position class.
        
        Attributes
        ----------
        title (str): The name of the position or job title

        about_job (str): The descriptive or background text about the position.

        about_org (str): The description and background about the agency or office.

        workplan (dict): Dictionary with key, value pairs for the job task or compentency area and 
                the percentage of time anticipated or necessary to be spent in that area to successfully  
                execute the job.
        
        division (str): The name of the work unit or division in which the position is located.
        """
        self.title = title
        self.about_job = about_job
        self.workplan = workplan
        self.division = 'BPIO: Business Process Improvement Office'
        self.about_org = """
As an agency the Department of General Services manages the vertical and mobile assets for the City of Baltimore, 
providing the critical infrastructure for the operation of government agencies, including those providing direct 
public services to citizens.   Organizational units are organized around these core responsibilities. 
The Business Process Improvement Office (BPIO) is a unit of the Department of General Services. We are a performance 
management consultancy to organizational units and services within the agency.  BPIO drives continuous process 
improvement for service delivery helping across a range of domains and tasks including but not limited to: research, 
policy development, key performance indicator development, project implementation, statistical analysis and task 
automation. We help create and communicate quantifiable advancements in government efficiency, improving operating 
time, capital and human resource allocations or requirements.  BPIO has three core focus areas: 1) completely reducing 
the agency’s dependency on paper, making all processes paperless by 2024, 2) furthering the BPIO Extension Project via 
partnerships with relevant private industry, public sector and academic entities to promote low cost process, 
information technology or project-based policy solutions or experiments and information sharing to create a sustainable 
highly skilled pipeline to public service that exponentially increases problem solving capacity, and 3) automating, 
to the maximum extent possible, all repetitive analysis, communications and administrative tasks throughout the agency 
and establishing Python as the lingua franca for municipal government process improvement. 
"""

def get_position_data(file):
    """Parse yaml document containing data on each available position.
    Function parses a yaml document into stream and laods into a Python object.
    
    Parameters
    ----------
    file: Str
        Yaml file containing the information on each position. Each position in 
        the Yaml file has an attribute corresponding to the attributes for the 
        Position class. 
        
    Returns
    -------
    dict:  Returns dictionary of the parsed Yaml file. The dictionary has key value 
           pairs for the position as keys and the corresponding attirbutes for the 
           position as values. 
           
    Example
    -------
    >>> get_position_data(file='data/position_data.yaml') # returns dict of positions & attributes
    """
    stream = open(file, mode='r')
    data = yaml.safe_load(stream)
    
    return data
    

def generate_jobs(data):
    """Generate new instance of the Position class for each job found in the data.
    
    Function uses the parsed data from yaml file containing positions and position data
    and for each job it creates an instance of the Position class, storing each 
    instances in a dictionary.
    
    Parameters
    ----------
    data:   dict
         dictionary of the parsed Yaml file. The dictionary has key value pairs for 
         the position as keys and the corresponding attirbutes for the position as values.
         
    Returns
    -------
    dict:  Returns dictionary with key value pairs for the job and attributes of the job.
    
    Example
    -------
    >>> generate_jobs(data=position_data)
    
    >>> generate_jobs(get_position_data(file='data/position_data.yaml'))
    """
   
    jobs = {}
    for job in data:
        jobs[job] = Position(title=data[job]['title'],
                            about_job=data[job]['description'],
                            workplan=data[job]['workplan'])
    
    return jobs

def show_jobs(file):
    """Return list of all positions available.
    
    Parameters
    ----------
    file:  Str
        Yaml file containing the information on each position. Each position in 
        the Yaml file has an attribute corresponding to the attributes for the 
        Position class. 
    
    Returns
    -------
    list:  Returns list of positions available in Yaml file containing positions. 
    
    Example
    -------
    >>> show_all_positions(file='data/positions_data.yaml')
        
    """
    
    try:
        data = get_position_data(file)
    
    except Exception as e:
        return e
    
    try:
        positions = []
        for position in data.keys():
            positions.append(position)
    
        return positions
    
    except Exception as e:
        return e
    

def show_position_titles(file):
    """Return list of all position job titles.
    
    Parameters
    ----------
    file:  Str
        Yaml file containing the information on each position. Each position in 
        the Yaml file has an attribute corresponding to the attributes for the 
        Position class. 
    
    Returns
    -------
    list:  Returns list of job titles for each position available in the Yaml file 
    containing positions. 
    
    Example
    -------
    >>> show_position_titles(file='data/positions_data.yaml')
        
    """
    
    try:
        data = get_position_data(file)
        
    except Exception as e:
        return e
    
    try:
        jobs = generate_jobs(data)
    
    except Exception as e:
        return e
    
    try:
        titles = []
        for job in jobs:
            titles.append(jobs[job].title)
            
        return titles
    
    except Exception as e:
        return e
    


        


        
#########################################################################
#########################################################################
                  ## Program Variables ##
#########################################################################
#########################################################################   
data = get_position_data(file='data/position_data.yaml')
jobs = generate_jobs(data=data)