from urllib.request import pathname2url


class URLUtil:

    @staticmethod
    def path2url(file_path):
        return pathname2url(file_path)
