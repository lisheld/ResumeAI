import pandas as pd
import re

data = pd.read_csv('./Resume.csv')

def extract_title(text):
    """
    Given a string of text, extract the title
    of the section by getting rid of the
    remaining html tags.
    """
    for idx, char in enumerate(text):
        if char == ">":
            result = text[idx+1:]

    return result.strip()

def extract_bullet_points(text):
    """
    Given a string of text, remove all of the
    html tags that may be present, and return
    the text that is left.
    """
    result = ""
    ignore = False
    for char in text:
        if char == "<":
            ignore = True
        elif char == ">":
            ignore = False
        elif not ignore:
            result += char
    return result.strip()

def filter_section_titles(html):
    """
    Filter the section titles from the html,
    and return them as a list of strings.
    """
    section_titles = []
    pattern = r'sectiontitle(.*?)</div>'
    matches = re.findall(pattern, html)
    for match in matches:
        section_titles.append(extract_title(match))
    return section_titles

def filter_bullet_points(html):
    """
    Filter out all of the list elements in
    a string of html, and return them as a
    list of strings
    """
    bullet_points = []
    pattern = r'<li>(.*?)</li>'
    matches = re.findall(pattern, html)
    for match in matches:
        bullet_points.append(extract_bullet_points(match))
    return bullet_points

# Apply the functions to the html data and create new columns
data['Section_Titles'] = data['Resume_html'].apply(filter_section_titles)
data['Bullet_Points'] = data['Resume_html'].apply(filter_bullet_points)
data['Best_Bullet'] = data['Bullet_Points'].apply(lambda x: max(x, key=len) if x else None)

# Print the first 5 rows of the new columns
print(data['Section_Titles'].head())
print(data['Bullet_Points'].head())
print(data['Best_Bullet'].head())