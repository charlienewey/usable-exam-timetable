# The *Actually Usable* Aberystwyth Exam Timetable

## How was this done?

* Use [tabula][1] to extract data from the PDF that was handed out.
* Use [this Python script][2] to extract data from the CSV and dump it into a JSON file that AJAX
  can use.
* That's it - now serve the main folder from an HTTP server, and you're golden.

This took about 15 minutes to create (and I can't be bothered to make it look pretty), so if
something goes wrong or it doesn't work, pull requests are welcome!

[1]: http://tabula.technology
[2]: https://github.com/charlienewey/usable-exam-timetable/blob/gh-pages/extract-exams.py
