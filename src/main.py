from apk_generator import ApkGenerator
import sys


def assert_context(context):
    pass


def read_config_file(file_name):
    pass


if __name__ == "__main__":
    context = read_config_file(sys.argv[1])
    assert_context(context)
    generator = ApkGenerator(context)
    generator.mainloop()