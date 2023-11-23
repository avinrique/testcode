import os
import shutil

# Function to create a new HTML file with content from source HTML file
def create_html_file(index, source_html):
    new_html_file = f'Page-{index}.html'
    shutil.copy(source_html, new_html_file)
    return new_html_file

# Function to create a new CSS file with content from source CSS file
def create_css_file(index, source_css):
    new_css_file = f'Page-{index}.css'
    shutil.copy(source_css, new_css_file)
    return new_css_file

# Replace 'source.html' and 'styles.css' with your actual source files
source_html = 'test.html'
source_css = 'Page.css'

# Create 18 HTML and CSS files
for i in range(1, 19):
    new_html_file = create_html_file(i, source_html)
    new_css_file = create_css_file(i, source_css)
    print(f'Created {new_html_file} and {new_css_file}')

print('Files creation and content copy completed.')
