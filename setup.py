from setuptools import setup, find_packages

setup(
    name = 'positions',
    version = '0.1',
    author = 'Babila R. Lima',
    author_email = 'babila.lima30@gmail.com',
    description = ('A project to standardize and automate the generation of concise position descriptions and job postings for the Business Process Improvement Office of the Department of General Serivces.'),
    keywords = 'job description generator',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'Click', 'chart-studio', 'PyDrive', 'PyYAML', 'plotly', 'python-docx', 'tqdm'
    ],
    entry_points = """
        [console_scripts]
        position = positions.scripts.position:cli
        """,
)