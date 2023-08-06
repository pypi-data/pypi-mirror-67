import crdatamgt
import yaml
import os
import simplelogging


def main():
    log = simplelogging.get_logger(file_name="aithermal.log", console=False)

    def represent_none(self, _):
        return self.represent_scalar('tag:yaml.org,2002:null', '')

    yaml.add_representer(type(None), represent_none)

    try:
        with open("parameters.yaml", 'r') as stream:
            data_loaded = yaml.safe_load(stream)
            try:
                crdatamgt.project.project_load(**data_loaded)
            except TypeError as e:
                print("Please double-check your parameters.yaml document'")
                #os.startfile(os.path.join(os.getcwd(), 'parameters.yaml'))
                log.exception(e)
                log.debug(e)
    except FileNotFoundError as e:
        data_loaded = crdatamgt.helpers.write_yaml()
        with open('parameters.yaml', 'w') as outfile:
            yaml.dump(data_loaded, outfile, default_flow_style=False)
        print("Please fill out the parameter.yaml document")
        #os.startfile(os.path.join(os.getcwd(), 'parameters.yaml'))
        log.exception(e)
        log.debug(e)


if __name__ == "__main__":
    main()
