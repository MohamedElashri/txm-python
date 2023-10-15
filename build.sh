#!/bin/bash

# Function to display help information
display_help() {
    echo "Usage: $0 [options]"
    echo "  -v, --version      Set the package version"
    echo "  -p, --publish      Publish to PyPI ('y' or 'n')"
    echo "  -e, --env          Location of .env file"
    echo "  -h, --help         Display this help and exit"
}

# Initialize the PUBLISH variable as empty
PUBLISH=""

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
        -p|--publish)
        PUBLISH="$2"
        shift # past argument
        shift # past value
        ;;
        -e|--env)
        source "$2"
        # Update internal variables from environment variables
        VERSION="${VERSION:-$VERSION}"
        PUBLISH="${PUBLISH:-$PUBLISH}"
        TOKEN="${TOKEN:-$TOKEN}"
        shift # past argument
        shift # past value
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

# Ask user if they want to publish, but only if the --publish flag or .env file didn't set it
if [[ -z $PUBLISH ]]; then
    echo "Do you want to publish the package? (y/n)"
    read PUBLISH
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