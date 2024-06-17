As part of the Istanbul Kodluyor project, I created the test automation framework for the Tobeto website following the Page Object Model design pattern for my final project in the Software Quality and Test Specialization training.

Project Structure
pages: This folder contains the classes that create page objects for the pages and components, including special methods specific to those pages and components.
constants: This folder holds the constants for the page objects.
tests: This folder contains the test classes for each of the page objects.
data: This folder stores data used for data-driven testing.
screenshots: This folder stores screenshots.
report: This folder contains test reports - pytest-html-reporter.
tests/conftest: This file is for driver configuration and fixture settings.
tests/base_test: This is the main class for tests. Other test classes inherit from this class.
pages/base_page: This class contains methods that are commonly used by all page objects. Other page objects inherit from this class.
