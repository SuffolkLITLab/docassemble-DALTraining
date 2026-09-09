import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.DALTraining',
      version='1.0.0',
      description=('New interview builder training templates'),
      long_description='# Document Assembly Line training resources\r\n\r\nThis repository contains resources for the [Suffolk LIT Lab](https://suffolklitlab.org/)\'s Document Assembly Line trainings for volunteers. (If you are interested in volunteering, you can [learn more and sign up on the Document Assembly Line website ](https://assemblyline.suffolklitlab.org/docs/volunteer).)\r\n\r\n## General teaching tips\r\n\r\n* Pause frequently and ask everyone to give a thumbs up when they are caught up\r\n* Encourage questions, and occasionally pause (long enough for it to get awkward!) so people have time to consider what questions they might have and speak up\r\n\r\n## New interview builder training\r\n\r\nThis training is built around 3 90-minute sessions.\r\n\r\n### Session 1: Hello, world!\r\n\r\nThis session is an introduction to “vanilla” Docassemble. At the end of this session, you will be able to create simple interviews that ask for information in different ways, from simple text fields to checkboxes and date fields. You\'ll also be able to customize questions based on the user\'s previous answers.\r\n\r\nBefore this session, attendees should:\r\n\r\n1. Register an account on the [LIT Lab development server](https://apps-dev.suffolklitlab.org/)\r\n2. Email [litlab@suffolk.edu](mailto:litlab@suffolk.edu) to request developer privileges (include the email you used to register)\r\n3. Join the Microsoft Teams Document Assembly Line team (if you haven\'t gotten an invitation, just ask!)\r\n\r\nOutline:\r\n\r\n1. Introductions\r\n2. Make sure everyone can access the Playground\r\n3. Highlight [resources](https://assemblyline.suffolklitlab.org/docs/get_started/resources) for interview builders\r\n   1. Weekly meetings\r\n   2. Community help forum (Teams)\r\n   3. Monthly workshops\r\n   4. Docassemble Slack\r\n4. Create a new project and get started!\r\n   1. Introduction to the Docassemble Playground (Hello, world!)\r\n   2. Create your first question\r\n   3. Working with common question types\r\n   4. Specifying the order of questions\r\n   5. Dynamic questions\r\n\r\n### Session 2: Document assembly\r\n\r\nThis session is an introduction to assembling documents based on the user\'s answers. At the end of this session you\'ll be able to assemble documents based on DOCX and PDF templates.\r\n\r\nBefore this session, you should have a working interview based on [this code](https://github.com/SuffolkLITLab/docassemble-DALTraining/blob/main/docassemble/DALTraining/data/questions/1_5_dynamic_questions.yml).\r\n\r\nOutline:\r\n\r\n1. Recap the first session\r\n2. Make sure nobody is lost or stuck\r\n3. Open the Playground and get started!\r\n   1. Basic document assembly using Markdown\r\n   2. Document assembly using Word templates\r\n   3. Document assembly using Acrobat templates\r\n\r\n### Session 3: The Weaver and the GitHub workflow\r\n\r\nThis session is an introduction to the Document Assembly Line Weaver, a tool for generating draft interviews from an existing DOCX or PDF template. We\'ll also go over the [GitHub workflow](https://assemblyline.suffolklitlab.org/docs/authoring/github), for saving your work and collaborating with others.\r\n\r\nAt the end of this session you will be able to use the Weaver to generate a draft Docassemble interview from an existing form, and you will be able to work on interview updates following the GitHub workflow.\r\n\r\n*Note: this session does not have example YAML files because we will be using the Weaver to generate them from PDF and DOCX templates.*\r\n\r\nOutline:\r\n\r\n1. Prepare `affidavit_template.pdf` using Adobe Acrobat or the [free Gavel PDF tool](https://start.gavel.io/pdf) by changing variable names to match [AssemblyLine field labels](https://assemblyline.suffolklitlab.org/docs/authoring/label_variables)\r\n   * Change `full_name` to `users1_name_full` and subsequent occurrences to `users1_name_full__1`, `users1_name_full__2`, and so on\r\n   * Change `signature` to `users1_signature`\r\n2. Run the PDF through the Weaver, then upload the package to the Playground\r\n3. Locate familiar blocks in the Weaver-generated YAML:\r\n   * Interview order\r\n   * Questions (note questions that are "missing" because they are pulled in from the question library)\r\n   * Attachment\r\n   \r\n   (Don\'t ignore the rest of the file, but note that they\'ll be able to learn about other blocks when they need to. The documentation website also includes a helpful [guide to the Weaver-generated YAML](https://assemblyline.suffolklitlab.org/docs/authoring/generated_yaml).)\r\n4. Run the interview\r\n5. Demonstrate how to modify a question from the library\r\n6. Prepare `affidavit_template.docx` by changing variables names to match AssemblyLine field labels\r\n   * Change `full_name` to `users[1].name.full()`\r\n   * Change `signature` to `users[1].signature`\r\n7. Run the DOCX through the Weaver, then run the interview and note any differences\r\n8. Discuss the differences between DOCX and PDF templates\r\n9. Introduce the the [GitHub workflow](https://assemblyline.suffolklitlab.org/docs/authoring/github#workflow) using `github_demo.yml`\r\n   1. Publish the interview to GitHub\r\n   2. Create issues based on the unimproved Weaver-generated interview\r\n   3. Walk through the GitHub workflow with one of those issues\r\n      1. Create a new Playground project\r\n      2. Pull the interview to the Playground\r\n      3. Commit to a new branch\r\n      4. Create a pull request (and close issues in the PR message)\r\n      6. Resolve conflicts\r\n      7. Review pull requests\r\n\r\n## Final project\r\n\r\nNow, apply what you have learned! Create a guided interview based on the example certificate of service (`/final-project/Certificate of Service FINAL (1).pdf`).\r\n\r\nRequirements:\r\n\r\n* The interview does not generate errors\r\n* The user can correctly complete every field/blank on the form\r\n* The interview correctly populates every field on the form\r\n* The interview uses branching logic to skip unnecessary questions and provide a logical flow\r\n* Compound questions are broken up into separate screens\r\n* The user is not asked the same information twice\r\n* The user can sign on their computer or phone screen\r\n* Questions are written in plain language\r\n* The interview is published to your GitHub account\r\n* The interview uses questions from the Assembly Line question library (although you may modify them if necessary)\r\n* The interview follows our naming conventions for the [template file name](https://assemblyline.suffolklitlab.org/docs/authoring/naming#form-files-stored-in-docassemble-snake_case), the [package/repository name](https://assemblyline.suffolklitlab.org/docs/authoring/naming/#docassemble-projects-and-packages), and [variables in templates and code](https://assemblyline.suffolklitlab.org/docs/authoring/naming/#pdf-variables--snake_case)\r\n\r\nTo turn in your final project, post the GitHub URL where it can be found to the [Volunteers channel in Teams](https://teams.microsoft.com/l/channel/19%3A51759e27ee9749c1956ad38f08560c1f%40thread.tacv2/Volunteers?groupId=eaa9bd9d-cf39-4686-8f30-e55aa9d98c75&tenantId=78733fa9-540e-4eb8-bf29-73c4eeb63412).',
      long_description_content_type='text/markdown',
      author='Sam Glover',
      author_email='sam.glover@suffolk.edu',
      license='MIT',
      url='https://assemblyline.suffolklitlab.org/',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/DALTraining/', package='docassemble.DALTraining'),
     )
