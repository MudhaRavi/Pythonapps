import pathlib
import zipfile

def make_archive(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, 'archive.zip')
    with zipfile.ZipFile(dest_dir,'w') as zipf:
        for filepath in filepaths:
            zipf.write(filepath)


if __name__ == '__main__':
    make_archive(filepaths=["bonus8.py", "bonus11.py"], dest_dir="archive")