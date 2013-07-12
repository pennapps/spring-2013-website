import csv
import sys

from jinja2 import Environment, FileSystemLoader


def build_template(env, template_name, **kwargs):
    print "Building %s..." % template_name
    template = env.get_template(template_name)
    with open(template_name, "w") as f:
        f.write(template.render(**kwargs))


def parse_csv(filename):
    with open(filename, 'rU') as f:
        return list(csv.DictReader(f))


def build_index(env):
    sponsors = parse_csv("data/sponsors.csv")
    level_order = dict()
    level_order['ipo'] = 0
    level_order['mezzanine'] = 1
    level_order['series-a'] = 2
    level_order['seed'] = 3
    sponsor_classes = dict()
    sponsor_classes[0] = []
    sponsor_classes[1] = []
    sponsor_classes[2] = []
    sponsor_classes[3] = []
    for sponsor in sponsors:
        sponsor_classes[level_order[sponsor['level']]].append(sponsor)
    competitions = parse_csv("data/competitions.csv")
    build_template(env, 'index.html',
                   sponsors=sponsors,
                   competitions=competitions,
                   )


def build_history(env):
    build_template(env, 'history.html')


def build_sponsorship(env):
    build_template(env, 'sponsorship.html')


def build_faq(env):
    build_template(env, 'faq.html')


def build_rules(env):
    build_template(env, 'rules.html')


def build_about(env):
    build_template(env, 'about.html')

def build_penn_registration(env):
    build_template(env, 'penn-registration.html')

def build_press(env):
    stories = parse_csv("data/press.csv")
    level_order = dict()
    level_order['2010 Fall'] = 5
    level_order['2011 Spring'] = 4
    level_order['2011 Fall'] = 3
    level_order['2012 Spring'] = 2
    level_order['2012 Fall'] = 1
    level_order['2013 Spring'] = 0
    story_classes = dict()
    story_classes[0] = []
    story_classes[1] = []
    story_classes[2] = []
    story_classes[3] = []
    story_classes[4] = []
    story_classes[5] = []
    for story in stories:
        story_classes[level_order[story['competition']]].append(story)
    build_template(env, 'press.html',
                   story_classes=story_classes,
                   )


def build_venue(env):
    build_template(env, 'venue.html')


def main():
    env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    build_index(env)
    build_press(env)
    build_about(env)
    build_history(env)
    build_venue(env)
    build_rules(env)
    build_faq(env)
    build_sponsorship(env)
    build_penn_registration(env)
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
