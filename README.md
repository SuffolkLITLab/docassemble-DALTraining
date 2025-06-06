# Document Assembly Line training resources

This repository contains resources for the [Suffolk LIT Lab](https://suffolklitlab.org/)'s Document Assembly Line trainings.

## General teaching tips

* Pause frequently and ask everyone to give a thumbs up when they are caught up
* Encourage questions, and occasionally pause (long enough for it to get awkward!) so people have time to consider what questions they might have and speak up

## New interview builder training

This training is built around 3 90-minute sessions.

### Session 1: Hello, world!

This session is an introduction to “vanilla” Docassemble. At the end of this session, you will be able to create simple interviews that generate completed documents.

Before this session, attendees should:

1. Register an account on the [LIT Lab development server](https://apps-dev.suffolklitlab.org/)
2. Email [litlab@suffolk.edu](mailto:litlab@suffolk.edu) to request developer privileges (include the email you used to register)
3. Be invited to the Microsoft Teams Document Assembly Line team

Outline:

1. Introductions
2. Make sure everyone can access the Playground
3. Highlight [resources](https://assemblyline.suffolklitlab.org/docs/get_started/resources) for interview builders
   1. Weekly meetings
   2. Community help forum
   3. Monthly workshops
   4. Docassemble Slack
4. Create a new project and get started!
   1. Introduction to the Docassemble Playground (Hello, world!)
   2. Create your first question
   3. Working with common question types
   4. Specifying the order of questions
   5. Dynamic questions

### Session 2: Document assembly

This session builds on the first session.

Before this session, you should have a working interview based on [this code](https://github.com/SuffolkLITLab/docassemble-DALTraining/blob/main/docassemble/DALTraining/data/questions/1_5_dynamic_questions.yml).

Outline:

1. Recap the first session
2. Make sure nobody is lost or stuck
3. Open the Playground and get started!
   1. Basic document assembly using Markdown
   2. Document assembly using Word templates
   3. Document assembly using Acrobat templates

### Session 3: The Weaver and the GitHub workflow

This session is an introduction to the Document Assembly Line Weaver. At the end of this session you will be able to use the Weaver to generate a draft Docassemble interview from an existing form.

The documentation website also includes a helpful [guide to the Weaver-generated YAML](https://assemblyline.suffolklitlab.org/docs/authoring/generated_yaml).

*Note: this session does not have example YAML files because we will be using the Weaver to generate them from PDF and DOCX templates.*

Outline:

1. Prepare `../templates/affidavit_template.pdf` using Adobe Acrobat or the [free Gavel PDF tool](https://start.gavel.io/pdf) by changing variable names to match [AssemblyLine field labels](https://assemblyline.suffolklitlab.org/docs/authoring/label_variables)
   * Change `full_name` to `users1_name_full` and subsequent occurrences to `users1_name_full__1`, `users1_name_full__2`, and so on
   * Change `signature` to `users1_signature`
2. Run the PDF through the Weaver, then upload the package to the Playground
3. Locate familiar blocks in the Weaver-generated YAML:
   * Interview order
   * Questions (note questions that are "missing" because they are pulled in from the question library)
   * Attachment
   (Don't ignore the rest of the file, but note that they'll be able to learn about other blocks when they need to.)
4. Run the interview
5. Demonstrate how to modify a question from the library
6. Prepare `../templates/affidavit_template.docx` by changing variables names to match AssemblyLine field labels
   * Change `full_name` to `users[1].name.full()`
   * Change `signature` to `users[1].signature`
7. Run the DOCX through the Weaver, then run the interview and note any differences
8. Discuss the differences between DOCX and PDF templates
9. Introduce the the [GitHub workflow](https://assemblyline.suffolklitlab.org/docs/authoring/github#workflow)
   1. Publish the interview to GitHub
   2. Create issues based on the unimproved Weaver-generated interview
   3. Walk through the GitHub workflow with one of those issues