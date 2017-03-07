from strictyaml import load

configname = "copyrules.yml"
def loader():
        data = open(configname)
        txt = data.read()
        configs = load(txt).data
        return configs