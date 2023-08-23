from __future__ import print_function, unicode_literals

import collections
import datetime
import io
import os

import jinja2
import markdown


class Post(collections.namedtuple('Post', ['title', 'slug', 'pub_date', 'update_date', 'body'])):

    def is_archive(self):
        return self.slug.startswith('posts/archive/')

    def is_draft(self):
        return self.slug.startswith('posts/drafts/')


def format_datetime(dt):
    for fmt in (
        '%Y-%m-%d %H:%M:%S.%f',
        '%Y-%m-%d %H:%M:%S',  # Legacy format
    ):
        try:
            return datetime.datetime.strptime(dt, fmt)
        except ValueError:
            continue


class Static(object):

    def __init__(self, template_path, source_path, build_dir):
        self.filters = {}
        self.globals = {}
        loader = jinja2.FileSystemLoader(searchpath=template_path)
        self.env = jinja2.Environment(loader=loader)
        self.posts = {
            'published': [],
            'archived': [],
            'drafts': [],
        }
        self.source = os.walk(source_path)
        self.build_dir = build_dir

    def update_filter_and_globals(self):
        self.env.filters.update(**self.filters)
        self.env.globals.update(**self.globals)

    def reqister_filter(self, function):
        filter_name = function.__name__.replace('filter_', '')
        self.filters[filter_name] = function
        return function

    def register_function(self, function):
        function_name = function.__name__.replace('function_', '')
        self.globals[function_name] = function
        return function

    def render(self, template_name, **context):
        template = self.env.get_template(template_name)
        output = template.render(**context)
        return output

    def render_index(self, **context):
        return self.render('blog/index.html', **context)

    def render_archive(self, **context):
        return self.render('blog/archive.html', **context)

    def render_detail(self, **context):
        return self.render('blog/detail.html', **context)

    def collect_source_files(self):
        result = []
        for root, dirs, files in self.source:
            for f in files:
                path = os.path.join(root, f)
                html_path = path.replace('.md', '.html')
                result.append(
                    # source - destination
                    (path, html_path),
                )
        return result

    def extract_post(self, source_path):
        with io.open(source_path, encoding='utf-8') as f:
            lines = f.readlines()
        title = lines[0][2:].strip()
        pub_date, update_date = lines[2].split(' | ')
        body = function_markup(''.join(lines[6:]))
        return title, pub_date.strip(), update_date.strip(), body

    def build_post(self, source_path, html_path):
        title, pub_date, update_date, body = self.extract_post(source_path)
        return Post(
            title,
            html_path,
            format_datetime(pub_date),
            format_datetime(update_date),
            body,
        )

    def sort_posts(self):
        for category, posts in self.posts.items():
            self.posts[category] = list(reversed(sorted(posts, key=lambda p: p.pub_date)))

    def build_html(self):
        self.update_filter_and_globals()

        for source_path, html_path in self.collect_source_files():
            post = self.build_post(source_path, html_path)
            if post.is_archive() and not post.is_draft():
                self.posts['archived'].append(post)
            elif post.is_draft() and not post.is_archive():
                # TODO: Don't convert draft posts for now.
                # self.posts['draft'].append(post)
                continue
            else:
                self.posts['published'].append(post)

        self.sort_posts()

        index_output = self.render_index(blogs=self.posts['published'])
        index_path = os.path.join(self.build_dir, 'index.html')

        with io.open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_output)

        archive_output = self.render_archive(blogs=self.posts['archived'])
        archive_path = os.path.join(self.build_dir, 'archive.html')

        with io.open(archive_path, 'w', encoding='utf-8') as f:
            f.write(archive_output)

        for category, posts in self.posts.items():
            print('===', category)
            for post in posts:
                print(post.title)
                post_output = self.render_detail(blog=post)
                post_path = os.path.join(self.build_dir, post.slug)
                with io.open(post_path, 'w', encoding='utf-8') as f:
                    f.write(post_output)


app = Static(
    template_path='templates',
    source_path='posts',
    build_dir='docs',
)


@app.register_function
def function_markup(string, extensions=None):
    if extensions is None:
        extensions = ['codehilite']
    else:
        extensions = [ext for ext in extensions.split(',') if ext]
    if 'safe' in extensions:
        extensions = extensions.remove('safe')
        options = {'safe_mode': True, 'enable_attributes': False}
    else:
        options = {'safe_mode': False}
    output = markdown.markdown(string, extensions=extensions, **options)
    return output


if __name__ == '__main__':
    app.build_html()
