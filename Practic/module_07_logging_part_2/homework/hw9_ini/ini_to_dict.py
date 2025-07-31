import configparser
import pprint


def ini_to_dict(filename):
    config = configparser.ConfigParser(interpolation=None)
    config.read(filename)

    result = {}
    for section in config.sections():
        result[section] = dict(config.items(section))

    return result

if __name__ == "__main__":
    ini_dict = ini_to_dict("logging_conf.ini") 
    with open('result_dict.py', 'w') as f:
        f.write("dict_config = ")
        f.write(pprint.pformat(ini_dict))
            

