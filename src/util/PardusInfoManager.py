import socket
import platform

class PardusInfoManager:
    pardus_info = None

    def __init__(self):
        self.prepare_data()

    def prepare_data(self):
        self.pardus_info = {}
        hostname = socket.gethostname()
        self.pardus_info["hostname"] = hostname.capitalize()

        os_info = platform.freedesktop_os_release()
        self.pardus_info["pardus"] = os_info.get("PRETTY_NAME")
        self.pardus_info["os_name"] = os_info.get("NAME")
        self.pardus_info["os_version"] = os_info.get("VERSION")
        self.pardus_info["os_codename"] = os_info.get("VERSION_CODENAME")

        self.pardus_info["kernel"] = platform.release()
        self.pardus_info["architecture"] = platform.machine()

    def get_info(self):
        return self.pardus_info