#!/bin/bash

# Function to display help information
display_help() {
    echo "Usage: $0 [options]"
    echo "  -v, --version    Set the package version"
    echo "  -n, --no-publish Skip publishing to PyPI"
    echo "  -e, --env        Location of .env file"
    echo "  -h, --help       Display this help and exit"
}

# Load from .env file if specified
if [[ "$1" == "-e" || "$1" == "--env" ]]; then
    source "$2"
    shift # past argument
    shift # past value
fi

# Retrieve the current package name and version from pyproject.toml
CURRENT_PACKAGE_NAME=$(awk -F\" '/name = /{print $(NF-1)}' pyproject.toml)
CURRENT_VERSION=$(awk -F\" '/version = /{print $(NF-1)}' pyproject.toml)

# Display the current package name and version
echo "Current package name: $CURRENT_PACKAGE_NAME"
echo "Current package version: $CURRENT_VERSION"

# Parse command-line options
while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        -v|--version)
        VERSION="$2"
        shift # past argument
        shift # past value
        ;;
        -n|--no-publish)
        NO_PUBLISH=YES
        shift # past argument
        ;;
        -h|--help)
        display_help
        exit 0
        ;;
        *)
        shift
        ;;
    esac
done

# Prompt for a new version number if not provided as an argument
if [[ -z $VERSION ]]; then
    echo "Enter the new version number:"
    read VERSION
fi

# Check if the new version matches the current version and exit if it does
if [[ "$VERSION" == "$CURRENT_VERSION" ]]; then
    echo "Version already exists. Closing the script."
    exit 0
fi

# Update version in pyproject.toml
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sed -i "s/version = \".*\"/version = \"$VERSION\"/g" pyproject.toml
elif [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' -e "s/version = \".*\"/version = \"$VERSION\"/g" pyproject.toml
fi

# Check for necessary tools
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update
        sudo apt install python3 python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    else
        echo "Unsupported OS. Exiting."
        exit 1
    fi
fi

# Build wheel
python3 setup.py sdist bdist_wheel

# Check if build is successful
if [[ $? -ne 0 ]]; then
    echo "Build failed. Exiting."
    exit 1
else
    echo "Build successful."
fi

# Ask user if they want to publish
if [[ -z $NO_PUBLISH ]]; then
    echo "Do you want to publish the package? (y/n)"
    read PUBLISH
else
    PUBLISH="n"
fi

# Publish package
if [[ "$PUBLISH" == "y" ]]; then
    if [[ -z $TOKEN ]]; then
        echo "Enter PyPI token:"
        read -s TOKEN
    fi
    echo "Publishing to PyPI..."
    echo "$TOKEN" | twine upload -u __token__ -p $TOKEN dist/*
else
    echo "Skipping publishing to PyPI."
fi
