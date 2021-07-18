import sys
import glob
import os.path
import shutil
import subprocess


class NotATrailDirectoryError(Exception):
    def __init__(self):
        pass


def _get_script_directory():
    return os.path.abspath(os.path.dirname(os.path.realpath(__file__)))


class PublicFilesGenerator:
    source_directory = ''
    target_directory = ''

    def __init__(self, source_directory):
        try:
            self.source_directory = self._set_valid_source_directory(source_directory)
            self.target_directory = self._set_valid_target_directory()
        except NotADirectoryError:
            print('Please provide a valid trail source directory!')
        except NotATrailDirectoryError:
            print('No gpx files found. Please provide a valid trail directory.')

    def _get_gpx_file(self):
        return glob.glob(self.source_directory + "/*.gpx")[0]

    def _check_gpx_files_in_directory(self, absolute_source_directory):
        gpx_files = glob.glob(absolute_source_directory + "/*.gpx")
        if not len(gpx_files) == 1:
            raise NotATrailDirectoryError
        else:
            print("Found gpx file:" + gpx_files[0])

    def _set_valid_source_directory(self, source_directory):
        """
        :raise NotADirectoryError
        :param source_directory:
        :return: string
        """
        absolute_source_directory = os.path.abspath(source_directory)
        if not os.path.isdir(absolute_source_directory):
            raise NotADirectoryError
        self._check_gpx_files_in_directory(absolute_source_directory)
        return absolute_source_directory

    def _get_parent_of_target_directory(self):
        return os.path.join(_get_script_directory(), 'media', 'diaryFiles')

    def _set_valid_target_directory(self):
        absolute_target_directory = os.path.join(self._get_parent_of_target_directory(),
                                                 os.path.basename(self.source_directory)
                                                 )
        print("Target directory: " + absolute_target_directory)
        return absolute_target_directory

    def _delete_files_in_directory(self, directory):
        files = glob.glob(directory + '/*')
        for file in files:
            os.remove(file)

    def _initialize_target_directory(self):
        if os.path.isdir(self.target_directory):
            self._delete_files_in_directory(self.target_directory)
        else:
            os.mkdir(self.target_directory)

    def _get_all_jpg_files_in_source_directory(self):
        jpg_files = glob.glob(self.source_directory + "/*.jpg") + glob.glob(self.source_directory + "/*.JPG") + \
                    glob.glob(self.source_directory + "/*.jpeg") + glob.glob(self.source_directory + "/*.JPEG")
        return jpg_files

    def _copy_gpx_file(self):
        source_gpx_file_path = self._get_gpx_file()
        target_gpx_file_path = os.path.join(self.target_directory, os.path.basename(source_gpx_file_path))
        shutil.copy2(source_gpx_file_path, target_gpx_file_path)

    def generate(self):
        try:
            self._initialize_target_directory()
            self._generate_responsive_images()
            self._copy_gpx_file()
        except IndexError:
            print('Usage: python createPublicFiles.py /diaryFiles/source')

    def _get_target_jpg_file_name(self, base_filename, file_size):
        target_file_name = '{base_filename}_w{filesize}.jpg'.format(
            base_filename=base_filename,
            filesize=file_size
        )
        return os.path.join(self.target_directory, target_file_name)

    def _generate_responsive_images(self):
        jpg_files_in_source_directory = self._get_all_jpg_files_in_source_directory()
        file_sizes = ["0210", "0715", "1020"]
        base_filename = 1
        for jpg_file in jpg_files_in_source_directory:
            for file_size in file_sizes:
                target_file_name = self._get_target_jpg_file_name(base_filename, file_size)
                try:
                    self.generate_responsive_image(jpg_file, target_file_name, file_size)
                except subprocess.CalledProcessError:
                    print("Error")
            base_filename += 1

    def generate_responsive_image(self, source_file_name, target_file_name, file_size):
        """
        :raise subprocess.CalledProcessError
        :param source_file_name:
        :param target_file_name:
        :param file_size:
        :return:
        """
        subprocess.run([
            'convert',
            source_file_name,
            '-resize',
            file_size,
            target_file_name
        ])


if len(sys.argv) >= 2:
    PublicFilesGenerator = PublicFilesGenerator(sys.argv[1])
    PublicFilesGenerator.generate()
else:
    print('Usage: python createPublicFiles.py diaryFiles/trailDirectory')
