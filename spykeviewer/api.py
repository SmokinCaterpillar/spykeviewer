class __ConfigOptions:
    def __init__(self, **kw):
        # Ask about plugin paths if saving a file to a path that is not
        # a plugin path
        self.ask_plugin_path = True
        # Save and reload a modified plugin before starting
        self.save_plugin_before_starting = True
        # Load selection on start
        self.load_selection_on_start = True
        # Use Enter key for code completion in console
        self.codecomplete_console_enter = True
        # Use Enter key for code completion in editor
        self.codecomplete_editor_enter = True
        # Additional parameters for remote script
        self.remote_script_parameters = []
        # Show duplicate channels (those that belong to multiple
        # channel groups) multiple times in navigation
        self.duplicate_channels = False
        # Select all visible segments in navigation by default
        self.autoselect_segments = False
        # Select all visible channel groups in navigation by default
        self.autoselect_channel_groups = False
        # Select all visible channels in navigation by default
        self.autoselect_channels = True
        # Select all visible units in navigation by default
        self.autoselect_units = False

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


config = __ConfigOptions()
window = None
app = None


def start_plugin(name):
    """ Start first plugin with given name and return result of start()
    method. Raises a SpykeException if not exactly one plugins with
    this name exist.

    :param str name: The name of the plugin. Should not include the
        directory.
    """
    return window.start_plugin(name)


def start_plugin_remote(name):
    """ Start first plugin with given name using the remote script.
    Raises a SpykeException if not exactly one plugins with
    this name exist.

    :param str name: The name of the plugin. Should not include the
        directory.
    """
    window.start_plugin_remote(name)


def get_plugin(name):
    """ Get plugin with the given name. Raises a SpykeException if
    multiple plugins with this name exist. Returns None if no such
    plugin exists.

    :param str name: The name of the plugin. Should not include the
        directory.
    """
    return window.get_plugin(name)
