# coding: utf-8

"""
Standalone file utils.

Nothing in this module should have an knowledge of config or the layout
and structure of the site and pages in the site.
"""

import os
import shutil


def copy_file(source_path, output_path):
    """
    Copy source_path to output_path, making sure any parent directories exist.
    """
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copy(source_path, output_path)


def write_file(content, output_path):
    """
    Write content to output_path, making sure any parent directories exist.
    """
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    open(output_path, 'w').write(content)


def copy_media_files(from_dir, to_dir, exclude_extensions):
    """
    Recursively copy all files except markdown and HTML into another directory.
    """
    for (source_dir, dirnames, filenames) in os.walk(from_dir):
        relative_path = os.path.relpath(source_dir, from_dir)
        output_dir = os.path.normpath(os.path.join(to_dir, relative_path))

        for filename in filenames:
            # if not is_markdown_file(filename) and not is_html_file(filename):
            if not has_extension(filename, exclude_extensions):
                source_path = os.path.join(source_dir, filename)
                output_path = os.path.join(output_dir, filename)
                copy_file(source_path, output_path)


def get_html_path(path):
    """
    Map a source file path to an output html path.

    Paths like 'index.md' will be converted to 'index.html'
    Paths like 'about.md' will be converted to 'about/index.html'
    Paths like 'api-guide/core.md' will be converted to 'api-guide/core/index.html'
    """
    
    path = os.path.splitext(path)[0]
    return path + '.html'
    
    if os.path.basename(path) == 'index':
        return path + '.html'
    return os.path.join(path, 'index.html')


def get_url_path(path, use_directory_urls=True):
    """
    Map a source file path to an output html path.

    Paths like 'index.md' will be converted to '/'
    Paths like 'about.md' will be converted to '/about/'
    Paths like 'api-guide/core.md' will be converted to '/api-guide/core/'

    If `use_directory_urls` is `False`, returned URLs will include the a trailing
    `index.html` rather than just returning the directory path.
    """
    path = get_html_path(path)
    url = '/' + path.replace(os.path.sep, '/')
    if use_directory_urls:
        return url[:-len('index.html')]
    return url

def has_extension(path, extesions):
    ext = os.path.splitext(path)[1].lower()
    return ext in extesions

def markdown_extensions():
    return [
        '.markdown',
        '.mdown',
        '.mkdn',
        '.mkd',
        '.md',
    ]

def html_extensions():
    return [
        '.html',
        '.htm',
    ]

def is_markdown_file(path):
    """
    Return True if the given file path is a Markdown file.

    http://superuser.com/questions/249436/file-extension-for-markdown-files
    """
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.markdown',
        '.mdown',
        '.mkdn',
        '.mkd',
        '.md',
    ]


def is_css_file(path):
    """
    Return True if the given file path is a CSS file.
    """
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.css',
    ]


def is_javascript_file(path):
    """
    Return True if the given file path is a Javascript file.
    """
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.js',
        '.javascript'
    ]


def is_html_file(path):
    """
    Return True if the given file path is an HTML file.
    """
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.html',
        '.htm',
    ]
