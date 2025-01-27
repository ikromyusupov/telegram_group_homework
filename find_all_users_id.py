from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    actor_id = []
    for i in data['messages']:
        id1 = i.get('from_id', False)
        if id1 and id1 not in actor_id:
            actor_id.append(i.get('from_id'))
    return actor_id
data = read_data("data/result.json")