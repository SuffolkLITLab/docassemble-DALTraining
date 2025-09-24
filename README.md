# Document Assembly Line training resources

This repository contains resources for the [Suffolk LIT Lab](https://suffolklitlab.org/)'s Document Assembly Line trainings for volunteers. (If you are interested in volunteering, you can [learn more and sign up on the Document Assembly Line website ](https://assemblyline.suffolklitlab.org/docs/volunteer).)

## General teaching tips

* Pause frequently and ask everyone to give a thumbs up when they are caught up
* Encourage questions, and occasionally pause (long enough for it to get awkward!) so people have time to consider what questions they might have and speak up

## New interview builder training

This training is built around 3 90-minute sessions.

### Session 1: Hello, world!

This session is an introduction to “vanilla” Docassemble. At the end of this session, you will be able to create simple interviews that ask for information in different ways, from simple text fields to checkboxes and date fields. You'll also be able to customize questions based on the user's previous answers.

Before this session, attendees should:

1. Register an account on the [LIT Lab development server](https://apps-dev.suffolklitlab.org/)
2. Email [litlab@suffolk.edu](mailto:litlab@suffolk.edu) to request developer privileges (include the email you used to register)
3. Join the Microsoft Teams Document Assembly Line team (if you haven't gotten an invitation, just ask!)

Outline:

1. Introductions
2. Make sure everyone can access the Playground
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

### Session 2: Document assembly

This session is an introduction to assembling documents based on the user's answers. At the end of this session you'll be able to assemble documents based on DOCX and PDF templates.

Before this session, you should have a working interview based on [this code](https://github.com/SuffolkLITLab/docassemble-DALTraining/blob/main/docassemble/DALTraining/data/questions/1_5_dynamic_questions.yml).

Outline:

1. Recap the first session
2. Make sure nobody is lost or stuck
3. Open the Playground and get started!
   1. Basic document assembly using Markdown
   2. Document assembly using Word templates
   3. Document assembly using Acrobat templates

### Session 3: The Weaver and the GitHub workflow

This session is an introduction to the Document Assembly Line Weaver, a tool for generating draft interviews from an existing DOCX or PDF template. We'll also go over the [GitHub workflow](https://assemblyline.suffolklitlab.org/docs/authoring/github), for saving your work and collaborating with others.

At the end of this session you will be able to use the Weaver to generate a draft Docassemble interview from an existing form, and you will be able to work on interview updates following the GitHub workflow.

*Note: this session does not have example YAML files because we will be using the Weaver to generate them from PDF and DOCX templates.*

Outline:

1. Prepare `affidavit_template.pdf` using Adobe Acrobat or the [free Gavel PDF tool](https://start.gavel.io/pdf) by changing variable names to match [AssemblyLine field labels](https://assemblyline.suffolklitlab.org/docs/authoring/label_variables)
   * Change `full_name` to `users1_name_full` and subsequent occurrences to `users1_name_full__1`, `users1_name_full__2`, and so on
   * Change `signature` to `users1_signature`
2. Run the PDF through the Weaver, then upload the package to the Playground
3. Locate familiar blocks in the Weaver-generated YAML:
   * Interview order
   * Questions (note questions that are "missing" because they are pulled in from the question library)
   * Attachment
   
   (Don't ignore the rest of the file, but note that they'll be able to learn about other blocks when they need to. The documentation website also includes a helpful [guide to the Weaver-generated YAML](https://assemblyline.suffolklitlab.org/docs/authoring/generated_yaml).)
4. Run the interview
5. Demonstrate how to modify a question from the library
6. Prepare `affidavit_template.docx` by changing variables names to match AssemblyLine field labels
   * Change `full_name` to `users[1].name.full()`
   * Change `signature` to `users[1].signature`
7. Run the DOCX through the Weaver, then run the interview and note any differences
8. Discuss the differences between DOCX and PDF templates
9. Introduce the the [GitHub workflow](https://assemblyline.suffolklitlab.org/docs/authoring/github#workflow) using `github_demo.yml`
   1. Publish the interview to GitHub
   2. Create issues based on the unimproved Weaver-generated interview
   3. Walk through the GitHub workflow with one of those issues
      1. Create a new Playground project
      2. Pull the interview to the Playground
      3. Commit to a new branch
      4. Create a pull request (and close issues in the PR message)
      6. Resolve conflicts
      7. Review pull requests

## Final project

Now, apply what you have learned! Create a guided interview based on the example certificate of service (`/final-project/Certificate of Service FINAL (1).pdf`).

Requirements:

* The interview does not generate errors
* The user can correctly complete every field/blank on the form
* The interview correctly populates every field on the form
* The interview uses branching logic to skip unnecessary questions and provide a logical flow
* Compound questions are broken up into separate screens
* The user is not asked the same information twice
* The user can sign on their computer or phone screen
* Questions are written in plain language
* The interview is published to your GitHub account
* The interview uses questions from the Assembly Line question library (although you may modify them if necessary)
* The interview follows our naming conventions for the [template file name](https://assemblyline.suffolklitlab.org/docs/authoring/naming#form-files-stored-in-docassemble-snake_case), the [package/repository name](https://assemblyline.suffolklitlab.org/docs/authoring/naming/#docassemble-projects-and-packages), and [variables in templates and code](https://assemblyline.suffolklitlab.org/docs/authoring/naming/#pdf-variables--snake_case)

To turn in your final project, post the GitHub URL where it can be found to the [Volunteers channel in Teams](https://teams.microsoft.com/l/channel/19%3A51759e27ee9749c1956ad38f08560c1f%40thread.tacv2/Volunteers?groupId=eaa9bd9d-cf39-4686-8f30-e55aa9d98c75&tenantId=78733fa9-540e-4eb8-bf29-73c4eeb63412).