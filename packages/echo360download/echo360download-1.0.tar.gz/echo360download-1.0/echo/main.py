from . import downloader
import argparse


def main():
    parser = argparse.ArgumentParser(description='Download echo360 media files')

    parser.add_argument(
        'dest',
        help='Destination directory for the download')

    parser.add_argument(
        'cookie',
        help='Cookie file path',
    )

    args = parser.parse_args()
    echo = downloader.EchoDownloader(cookie_file=args.cookie, dest_directory=args.dest)
    echo.interactive()


if __name__ == '__main__':
    main()
