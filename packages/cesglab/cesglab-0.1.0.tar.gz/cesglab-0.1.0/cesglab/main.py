from microapp import Project

class CESGlab(Project):
    _name_ = "cesglab"
    _version_ = "0.1.0"
    _description_ = "Computational Earth Science Group Analysis Utilities"
    _long_description_ = "Computational Earth Science Group Analysis Utilities"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"
    _url_ = "https://github.com/grnydawn/cesglab"

    def __init__(self):
        self.add_argument("--test", help="test argument")
