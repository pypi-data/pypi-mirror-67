import os
import yaml
import datetime


def touch_dir(dir_path):
    if not (os.path.exists(dir_path)):
        os.makedirs(dir_path)


def datetime_4_directory_string():
    now = datetime.datetime.now()
    return "{}-{}-{}_{}-{}-{}".format(
        str(now.year).zfill(4),
        str(now.month).zfill(2),
        str(now.day).zfill(2),
        str(now.hour).zfill(2),
        str(now.minute).zfill(2),
        str(now.second).zfill(2))


def time_string():
    now = datetime.datetime.now()
    return "{}:{}:{}".format(
        str(now.hour).zfill(2),
        str(now.minute).zfill(2),
        str(now.second).zfill(2))


def date_string():
    now = datetime.datetime.now()
    return "{}-{}-{}".format(
        str(now.year).zfill(4),
        str(now.month).zfill(2),
        str(now.day).zfill(2))


def datetime_string():
    return f"{date_string()} {time_string()}"


class PyLogger(object):
    def __init__(self, log_path="log.bin",
                 console_only_flag=False, print_timestamp_flag=True):
        # validating inputs
        self.__log_path, \
        self.console_only_flag, self.print_timestamp_flag = \
            self._validate_inputs(
                log_path,
                console_only_flag, print_timestamp_flag)

        # pre-allocating the log stream
        self.__log_stream = None

        # starting the logging procedure
        self.start()

    def __repr__(self):
        return f"PyLogger instance pointing to {self.log_name}"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def _validate_inputs(log_path: str,
                         console_only_flag: bool, print_timestamp_flag: bool):
        # checking log_path data type and creating the entire path if needed
        if not isinstance(log_path, str):
            raise TypeError("Input 'log_path' must be of type 'str', got "
                            f"{type(log_path)} instead.")
        elif os.path.split(log_path)[0] == "":
            log_path = os.path.join(os.getcwd(), log_path)
        if not isinstance(console_only_flag, bool):
            raise TypeError("Input 'console_only_flag' must be of type "
                            f"'bool', got {type(console_only_flag)} instead.")
        if not isinstance(print_timestamp_flag, bool):
            raise TypeError("Input 'print_timestamp_bool' must be of type "
                            f"'bool', got {type(print_timestamp_flag)} "
                            f"instead.")
        return log_path, console_only_flag, print_timestamp_flag

    @property
    def file_path(self):
        return self.__log_path

    @property
    def file_dir(self):
        return os.path.split(self.file_path)[0]

    @property
    def file_name(self):
        return os.path.split(self.file_path)[1]

    @property
    def file_ext(self):
        return os.path.splitext(self.file_name)[1]

    @property
    def log_path(self):
        return self.__log_path

    @property
    def log_dir(self):
        return self.file_dir

    @property
    def log_name(self):
        return self.file_name

    @property
    def log_ext(self):
        return self.file_ext

    def start(self):
        # creating and / or opening a new log file
        if not self.console_only_flag:
            self.__log_stream = open(self.log_path, "a")

    def stop(self):
        # closing the log file
        if not self.console_only_flag:
            self.__log_stream.close()

    def _check_status(self):
        # opening the log file if necessary
        if self.__log_stream is None:
            self.start()
        elif self.__log_stream.closed:
            self.start()

    def print(self,
              inp_text: str,
              style="",
              up_extra_lines=0,
              dw_extra_lines=0,
              timestamp_flag=None):
        """
        :param inp_text: input text to be shown
        :param style: specify the dash style; it can be:
            "" (normal, no dash at all);
            "u" (upper dashed);
            "d" (down dashed);
            "ud" (upper and down dashed)
        :param up_extra_lines: number of empty lines above the print
        :param dw_extra_lines: number of empty lines below the print
        :param timestamp_flag: specify if the timestamp has to be printed
        """
        # checking the log file status
        if not self.console_only_flag:
            self._check_status()

        # adding the timestamp to input_text if required
        if timestamp_flag is None:
            timestamp_flag = self.print_timestamp_flag
        if timestamp_flag:
            inp_text = time_string() + " | " + inp_text

        # pre-allocating output text
        out_text = "\n" * up_extra_lines

        # writing output text
        if style.__contains__("u"):
            out_text += self.dash(inp_text) + "\n"
        out_text += inp_text + "\n"
        if style.__contains__("d"):
            out_text += self.dash(inp_text) + "\n"

        # printing extra lines
        out_text += "\n" * dw_extra_lines

        # printing on console
        print(out_text, end="")

        # printing on log file
        if not self.console_only_flag:
            self.__log_stream.write(out_text)

    @staticmethod
    def dash(text):
        return "=" * len(text)


class PyConfig(object):
    def __init__(self, file_path="config.yml"):
        # validating inputs
        self.__file_path = self._validate_inputs(file_path)

        # loading routine
        self._data = self._load()

    def __repr__(self):
        return f"PyConfig instance pointing to {self.file_name}"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def _validate_inputs(file_path: str):
        # checking file_path data type and creating the entire path if needed
        if not isinstance(file_path, str):
            raise TypeError("Input must be of type 'str'")
        elif os.path.split(file_path)[0] == "":
            file_path = os.path.join(os.getcwd(), file_path)

        # checking file existence
        try:
            open(file_path)
        except FileExistsError:
            raise FileNotFoundError(f"Input file {file_path} does not exist")

        # returning validated input
        return file_path

    def _load(self):
        # checking for the config file extension
        if self.file_ext in [".yml", ".yaml"]:
            # loading as yaml file
            data = yaml.safe_load(open(self.__file_path))
        elif self.file_ext == ".json":
            # loading as json file
            # TODO: create a loading routine for json files
            data = None
        elif self.file_ext in [".ini", ".bin", ".txt"]:
            # loading with the configparser
            # TODO: create a loading routine with the configparser
            data = None
        else:
            # raising exception for unrecognized extension
            raise ValueError(f"Unrecognized extension: {self.file_ext}")
        # returning data
        return data

    @property
    def file_path(self):
        return self.__file_path

    @property
    def file_dir(self):
        return os.path.split(self.__file_path)[0]

    @property
    def file_name(self):
        return os.path.split(self.__file_path)[1]

    @property
    def file_ext(self):
        return os.path.splitext(self.file_name)[1]

    @property
    def data(self):
        return self._data

    def reset(self):
        self.__init__(self.file_path)

    def reset_inputs(self, file_path="config.yml"):
        self.__init__(file_path)

    def write(self):
        # TODO: writing routine for all file types
        pass
