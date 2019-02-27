#from connect_to_erika import Erika


class ErikaImageRenderer:
    def __init__(self, some_erika, rendering_strategy):
        self.output_device = some_erika
        self.rendering_strategy = rendering_strategy
        self.rendering_strategy.setOutputDevice(some_erika)

    def renderAsciiArtFile(self, filePath):
        self.rendering_strategy.renderAsciiArtFile(filePath)


class LineByLineErikaImageRenderingStrategy():

    def renderAsciiArtFile(self, file_path):
        with open(file_path, "r") as open_file:
            for line in open_file.readlines():
                line_without_newline = line.replace('\n', "")
                self.output_device.print_ascii(line_without_newline)
                self.output_device.crlf()

    def setOutputDevice(self, some_erika):
            self.output_device = some_erika


