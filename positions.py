"""
"""

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

        