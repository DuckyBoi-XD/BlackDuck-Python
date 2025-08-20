from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="blackduck-game",
    version="0.1.0",
    author="Braeden Sy Tan",
    author_email="braedenjairsytan@icloud.com",
    description="Blackjack but with ducks. And for some reason, a complex ATM system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DuckyBoi-XD/BlackJack-Ducky",
    project_urls={
        "Repository": "https://github.com/DuckyBoi-XD/BlackJack-Ducky",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment :: Board Games",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "getch>=1.0",
    ],
    entry_points={
        "console_scripts": [
            "blackduck=blackduck.game:main",
        ],
    },
    keywords="blackjack game card-game casino duck",
)