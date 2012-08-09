import csv
import sys
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader


Story = namedtuple('Story', ['headline', 'source', 'href'])

STORIES = [
    Story('Best Mashups from PennApps 2012 Hackathon',
          'programmableweb',
          'http://blog.programmableweb.com/2012/01/18/best-mashups-from-pennapps-2012-hackathon/'
          ),
    Story('Undergrad Doers Take Aim At SOPA and PIPA at PennApps',
          'Twilio',
          'http://www.twilio.com/blog/2012/01/undergrad-doers-take-aim-at-sopa-and-pipa-at-pennapps.html'
          ),
    Story('Guest Post: 2012 Spring PennApps Hackathon - Simplicity',
          'HACKCOLLEGE',
          'http://www.hackcollege.com/blog/2012/01/19/guest-post-2012-spring-pennapps-hackathon-simplicity.html'
          ),
]


def build_template(env, template_name, **kwargs):
    print "Building %s..." % template_name
    template = env.get_template(template_name)
    with open(template_name, "w") as f:
        f.write(template.render(**kwargs))


def parse_csv(filename):
    with open(filename, 'rb') as f:
        return list(csv.DictReader(f))


def build_index(env):
    sponsors = parse_csv("data/sponsors.csv")
    competitions = parse_csv("data/competitions.csv")
    build_template(env, 'index.html',
            sponsors=sponsors,
            competitions=competitions,
            stories=STORIES,
    )


def build_history(env):
    build_template(env, 'history.html')


def build_faq(env):
    build_template(env, 'faq.html')


def build_about(env):
    build_template(env, 'about.html')


def build_schedule(env):
    build_template(env, 'schedule.html')


def build_venue(env):
    build_template(env, 'venue.html')


def build_sponsorship(env):
    build_template(env, 'sponsorship.html')


def main():
    env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    build_index(env)
    build_about(env)
    build_history(env)
    build_schedule(env)
    build_venue(env)
    build_sponsorship(env)
    build_faq(env)
    print "Templates built."


if __name__ == "__main__":
    main()

    if len(sys.argv) > 1 and sys.argv[1] == '--watch':
        import time

        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        class JinjaEventHandler(FileSystemEventHandler):
            """
            Naive recompiler.
            Rebuilds all templates if anything changes in /templates.
            """
            def on_modified(self, event):
                print "Recompiling templates..."
                super(JinjaEventHandler, self).on_created(event)
                if event.src_path.endswith("/templates"):
                    main()

        # Start watching for any changes
        event_handler = JinjaEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path="./templates")
        observer.start()
        print "Watching ./templates for changes..."
        print "Press Ctrl+C to stop."
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        print "Process killed"
        observer.join()
