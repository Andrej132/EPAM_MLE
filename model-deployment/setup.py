from setuptools import setup

setup(
    name="model_deployment",
    version="0.0.10",
    description="python project",
    url="https://github.com/Andrej132/EPAM_MLE_Course",
    author="Andrej",
    author_email="ruzicandrej9@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10", "pytest>=8.2", "scikit-learn>=1.4.2", "numpy>=1.26.4", "flask>=2.2.5",
                      "pandas>=2.2.2","requests>=2.31.0"],
    python_requires=">=3.10",
)
