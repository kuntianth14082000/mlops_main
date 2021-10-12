import os
import argparse
import yaml
import logging

def read_parameters(config_path):
    print(config_path)
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return  config

def main(config_path,datasource):
    config = read_parameters(config_path)
    print(config)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    #default_config_path = os.path.join("config", "parameters.yaml")
    default_config_path = r'C:\Users\knora\PycharmProjects\wafer\mlops_main\config\parameters.yaml'
    args.add_argument("--config",default=default_config_path)
    #config consits: what are the defaults paths,parameters,and default values going to use all mentioned here
    args.add_argument("--datasource",default=None)
    #if default = Null, it will choose from the config file

    parser_args = args.parse_args()
    #print(parser_args.config, parser_args.datasource)
    main(config_path = parser_args.config,datasource = parser_args.datasource)

