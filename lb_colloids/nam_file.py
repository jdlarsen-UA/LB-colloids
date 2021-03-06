

class NamFile(object):
    """
    Class to read the nam file instance of
    a lattice boltzmann model and delegate the IO
    reading to the applicable lb_colloid config
    reading classes

    Parameters:
    ----------
    :param str nam_file: nam file name
    """
    def __init__(self, nam_file):

        self.lb_config = None
        self.colloid_config = []
        self.__read_nam_file(nam_file)

    def __read_nam_file(self, nam_file):
        """
        Nam file parser method to read and set
        file paths to the lb_config and colloid_config
        attributes

        Parameters:
            nam_file: (str) name file path
        """
        lb = False
        col = False
        with open(nam_file) as nam:

            for line in nam:
                if line.startswith("#"):
                    pass

                elif line.lower().startswith('lbmodel'):
                    lb = True

                elif lb == True:
                    if line.lower().startswith('end'):
                        lb = False

                    else:
                        self.lb_config = line.rstrip()

                elif line.lower().startswith('colloidmodel'):
                    col = True

                elif col == True:
                    if line.lower().startswith('end'):
                        col = False

                    else:
                        self.colloid_config.append(line.rstrip())
