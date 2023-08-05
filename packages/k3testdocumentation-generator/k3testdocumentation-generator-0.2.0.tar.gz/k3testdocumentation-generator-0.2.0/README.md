# k3testdocumentation-generator

Tool for generating test documentation out of a test hierarchy or test.son


##Installation (use within viruatlenv or equivalent)
```
pip install k3testdocumentation-generator
```

###Prerequisites/Limitations:
wkhtmltopdf needs to be installed when generating PDFs (required by the pdfkit library). It is available in the package managers of the common linux distributions.  
May require running a virtual X server on a headless environment.

##Usage:
```
usage: k3testdocumentation-generator [-h] [-te {jinja2}] [-to {html,latex}]
                                     [-ot {pdf,json,raw}] [-o OUTPUT]
                                     [--template TEMPLATE] [-v] [-vv]
                                     input

CLI tool for creating a test document from a test directory or JSON

Author: Joachim Kestner <joachim.kestner@khoch3.de>
Version: 0.1.3

positional arguments:
  input                 Input to generate documentation from. Can either be a
                        directory containing the specified structure or an
                        appropriate JSON

optional arguments:
  -h, --help            show this help message and exit
  -te {jinja2}, --template_engine {jinja2}
                        The templating engine. Currently only jinja2 is
                        supported.
  -to {html,latex}, --template_output {html,latex}
                        The content language within the template. Only html is
                        supported.
  -ot {pdf,json,raw}, --output_type {pdf,json,raw}
                        The output format. JSON would output the data before
                        it goes into the templating engine. Raw is the raw
                        result after the templating engine has run. Default is
                        'pdf'
  -o OUTPUT, --output OUTPUT
                        Output file path. If not set a name will be generated
                        by: basename(input) + '.' + output_type.lower()
  --template TEMPLATE   The path to an alternative template
  -v, --verbose         Enable info logging
  -vv, --extra_verbose  Enable debug logging


```
##Example:
```
Create a the test directory structure (example included in src).
This structure works with the inbuilt template. To support a different
structure create a custom template and pass it using the --template parameter.

Note: any json file will be opened and interpreted. In the default structure
all json files need contain a list of strings 

example_test_dir/
├── TC.XX.01
│   ├── precondition.md
│   ├── required_equiptment.json
│   ├── requirements_fully_tested.json
│   ├── requirements_partially_tested.json
│   ├── test_descrition.md
│   └── test_name.txt
└── TC.XX.02
    ├── test_descrition.md
    └── __test__.json (Abbreviated form allowing the direct instanciation of
                       keys in one file. Will be overwritten if the file also
                       exists)
```
__Corresponding example command:__  

```
k3testdocumentation-generator .../example_test_dir/ -v -o t.pdf
```