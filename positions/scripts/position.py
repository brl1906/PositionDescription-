import click
from helper_module import get_googledrive_folderID, get_position, generate_plot, create_document, send_to_Googledocs, run_program

from tqdm import tqdm


@click.command()
@click.option('--division',
              prompt = 'Division or Office',
              default = 'bpio',
              help = """The name of the office or division in which the position will be housed. This argument expresses which office and related folder the position descrition document should be pushed to in Google Docs. Valid options include: [administration, bpio,  capitalProjects, fleet, facilities]""")

@click.option('--yaml_file',
              prompt = 'Position file',
              type = click.Path(exists=True),
              help = 'Filepath to the yaml file containing position description data. These documents exist in a folder labeled data.')

def run_program(division, yaml_file):
    """Executes sequence for the series of tasks and functions in the position description program. The function is a 
    wrapper for the core tasks of the program command line application for generating and handling standard formatted 
    position descriptions for the agency. 
    
    The function executes the following steps:
    
    1. Reads, parses a yaml file with positon data.
    2. Converts file data into dictionary object 
    3. Creates an interactive chart illustrating job responsibilities
    4. Publishes the chart to remote Plotly chart studio account, creating a unique access url
    5. Creates a directory 'data/charts' and timestamps and saves the chart as a png file to that directory
    6. Creates and saves a standard formated word document for the position description, inserting the png file to the document
    7. Logs into Google, creates or determines the existence of a folder labeled 'Position Descriptions' and pushes the word document to that Google Drive folder.
    
    
    """
    
    folderID = None
    position_description = None
    image_file = None
    word_document = None
    send = None
    
    execution_steps = [folderID,
                       position_description,
                       image_file,
                       word_document,
                       send]
    
    with tqdm(total = len(execution_steps), desc = 'Program Progress:', unit = 'tasks') as progress_bar:
        
        for step in execution_steps:
            
            if step == folderID and not step:
                folderID = get_googledrive_folderID(division)
                progress_bar.update(1)
            
            if step == position_description and not step:
                position_description = get_position(yaml_file)
                progress_bar.update(1)
            
            if step == image_file and not step:
                image_file, radarchart_url = generate_plot(position_description)
                progress_bar.update(1)
                
            if step == word_document and not step:
                word_document = create_document(position_description, image_file)
                progress_bar.update(1)
            
            if step == send and not step:
                send = send_to_Googledocs(word_document, folderID)
                progress_bar.update(1)
                                

if __name__ == "__main__":
    run_program()

 
