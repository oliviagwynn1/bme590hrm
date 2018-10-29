
def convert_json(myDictionary, f):
    """This function saves the metrics dictionary as a JSON file.

    The first line in this code imports the json package. The second
    line converts the dictionary into a json file. The last three lines
    open the json file and save it as the initial file read in the csv
    reader, removing the '.csv' from the end and replacing it with
    '.json', then saving it.

    :param myDictionary: metric dictionary
    :param f: variable the the file is saved under
    :type myDictionary: dictionary
    :type f: string
    """
    import json

    json = json.dumps(myDictionary)
    f = open(f.strip('.csv')+'.json', "w")
    f.write(json)
    f.close()





