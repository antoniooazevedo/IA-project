class Menu_Model:
    """
    Class that represents the model of a menu in the MVC pattern.
    
    It is responsible for storing the menu options and the selected option,
    as well as the big text at the top of the screen and the font size of the options.
    """
    def __init__(self, options, bigText, optionsFontSize):
        """
        Initializes a Menu_Model object.
        
        Args:
            options (list): The list of options in the menu.
            bigText (str): The big text at the top of the screen.
            optionsFontSize (int): The font size of the options.
        """
        self.options = options
        self.optionsFontSize = optionsFontSize
        self.bigText = bigText

        self.selected = 0
