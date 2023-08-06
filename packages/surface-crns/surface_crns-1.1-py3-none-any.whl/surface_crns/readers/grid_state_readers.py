from surface_crns.readers.statements import section_ends
import numpy as np

def read_grid_state(filename):
    '''
    Read a SimGrid state from a flat text file.

    Syntax for the flat text file is as follows: rows are separated by newline
    characters; columns are separated by any kind of whitespace or commas (but
    not a mix of both); comment lines begin with either "#" or "%".

    Grid state files may optionally be ended by a line starting with the string
    "!END_INIT_STATE"
    '''
    with open(filename, 'rU') as state_file:
        return parse_grid_state_stream(state_file)

def parse_grid_state_stream(grid_state_stream, debug = False):
    '''
    Read a SimGrid state from a stream of strings, as might be contained in a
    state file.
    See documentation for read_grid_state for a description of the grid state
    format.
    '''
    if debug:
        print("Reading grid state... ", end = "")
    grid_state = []
    for line in grid_state_stream:
        if line.startswith(section_ends['init_state']):
            break
        if line.startswith('#') or line.startswith('%'):
            continue
        new_row = line.strip().split()
        if len(new_row) == 0:
            continue
        if len(new_row) == 1:
            new_row = new_row[0].split(',')
        grid_state.append(new_row)
    grid_state = np.array(grid_state).transpose()
    if debug:
        print("done.")
    return grid_state