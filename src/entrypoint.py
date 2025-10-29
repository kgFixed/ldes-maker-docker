import os
import sys
import logging
import re


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Get the mounted volume path from an argument or environment variable
    volume_path = os.getenv("WORKSPACE", "/workspace")

    if not volume_path:
        logging.error(
            "No volume path provided. Please set the MOUNTED_VOLUME_PATH environment variable or pass it as an argument."
        )
        sys.exit(1)

    # Check if the volume path exists and is accessible
    if not os.path.exists(volume_path):
        logging.error(
            f"The specified volume path '{volume_path}' does not exist or is not accessible."
        )
        sys.exit(1)

    # Perform basic operations on the folder
    try:
        logging.info(f"Processing the volume at: {volume_path}")
        semver_pattern = re.compile(r"^v\d+\.\d+(\.\d+)?$")
        folders = [
            f
            for f in os.listdir(volume_path)
            if os.path.isdir(os.path.join(volume_path, f))
        ]

        for folder in folders:
            if semver_pattern.match(folder):
                folder_path = os.path.join(volume_path, folder)
                ttl_files = [f for f in os.listdir(folder_path) if f.endswith(".ttl")]
                logging.info(
                    f"Semver folder: {folder}, .ttl files count: {len(ttl_files)}"
                )
    except Exception as e:
        logging.error(f"An error occurred while processing the volume: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
