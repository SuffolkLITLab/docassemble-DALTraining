# Document Assembly Line training resources

This repository contains resources for the [Suffolk LIT Lab](https://suffolklitlab.org/)'s Document Assembly Line trainings.

## New interview builder trainings

### Session 1: Hello, world!

This session is an introduction to “vanilla” Docassemble. At the end of this session, you will be able to create simple interviews that generate completed documents.

Before this session, attendees should:

1. Register an account on the [LIT Lab dev server](https://apps-dev.suffolklitlab.org/)
2. Email [litlab@suffolk.edu](mailto:litlab@suffolk.edu) to request developer privileges (include the email you used to register)
3. Be invited to the Microsoft Teams Document Assembly Line team

Outline:

1. Introductions
2. Make sure everyone can access the Playground on the LIT Lab development server
3. Highlight [resources](https://assemblyline.suffolklitlab.org/docs/get_started/resources) for interview builders
   1. Weekly meetings
   2. Community help forum (Teams)
   3. Monthly workshops
   4. Docassemble Slack
4. Create a new project and get started!
   1. Introduction to the Docassemble Playground (Hello, world!)
   2. Create your first question
   3. Working with common question types
   4. Specifying the order of questions
   5. Dynamic questions
5. Teaser: basic document assembly

## Session 2: Document assembly

This session builds on the first session.

Before this session, attendees should have a working interview based on [this code](https://github.com/SuffolkLITLab/docassemble-DALTraining/blob/main/docassemble/DALTraining/data/questions/1_5_dynamic_questions.yml).

Outline:

1. Recap the first session
2. Make sure:
   1. Everybody has a working interview based on [this code](https://github.com/SuffolkLITLab/docassemble-DALTraining/blob/main/docassemble/DALTraining/data/questions/1_5_dynamic_questions.yml)
   2. Nobody is lost or stuck
3. Open the project from last session and get started!
   1. Basic document assembly (+ demonstration with HTML formatting)
   2. Document assembly using Word templates
   3. Document assembly using Acrobat templates

## Session 3: The Weaver and other Assembly Line tools

This session is an introduction to the Document Assembly Line tools, especially the Weaver. At the end of this session you will be able to use the Weaver to generate a draft Docassemble interview from an existing court form.

The documentation website has detailed information about [working with PDF files](https://assemblyline.suffolklitlab.org/docs/authoring/pdfs) and [working with Word/DOCX files](https://assemblyline.suffolklitlab.org/docs/authoring/docx), and why you might choose one over the other. For this session we will use both.

The documentation website also includes a helpful [guide to the Weaver-generated YAML](https://assemblyline.suffolklitlab.org/docs/authoring/generated_yaml).

*Note: this session does not have example YAML files because we will be using the Weaver to generate them from PDF and DOCX templates.*

Outline:

1. Prepare `../templates/affidavit_template.pdf` using Adobe Acrobat or the [free Gavel PDF tool](https://start.gavel.io/pdf)
2. Run the PDF through the Weaver
3. Tour the Weaver-generated YAML
4. Prepare `../templates/affidavit_template.docx`
5. Run the DOCX through the Weaver
6. Discuss the differences between DOCX and PDF templates

## Session 4: Troubleshooting

In this session we will go over common coding issues and how to solve them, plus general troubleshooting tips and a hands-on problem-solving session.