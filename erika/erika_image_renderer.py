class ErikaImageRenderer:
    def __init__(self, some_erika, rendering_strategy):
        self.output_device = some_erika
        self.rendering_strategy = rendering_strategy
        self.rendering_strategy.set_output_device(some_erika)

    def render_ascii_art_file(self, filePath):
        self.rendering_strategy.render_ascii_art_file(filePath)


class ErikaImageRenderingStrategy:

    def __init__(self):
        pass

    # noinspection PyAttributeOutsideInit
    def set_output_device(self, some_erika):
        self.output_device = some_erika

    def render_ascii_art_file(self, file_path):
        raise Exception('Not implemented')


class LineByLineErikaImageRenderingStrategy(ErikaImageRenderingStrategy):

    def __init__(self):
        ErikaImageRenderingStrategy.__init__(self)

    def render_ascii_art_file(self, file_path):
        with open(file_path, "r") as open_file:
            for line in open_file.readlines():
                line_without_newline = line.replace('\n', "")
                self.output_device.print_ascii(line_without_newline)
                self.output_device.crlf()
