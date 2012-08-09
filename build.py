import sys
from collections import namedtuple

from jinja2 import Environment, FileSystemLoader


Sponsor = namedtuple('Sponsor', ['name', 'href'])


IPO = [
      Sponsor('venmo', 'http://venmo.com'),
]

# TODO: Mailchimp
MEZZANINE = [
      Sponsor('facebook', 'http://facebook.com'),
      Sponsor('lore', 'http://lore.com'),
      Sponsor('mongodb', 'http://mongodb.com'),
      Sponsor('yahoo', 'http://yahoo.com'),
]

# TODO: Codeacademy
SERIES_A = [
      Sponsor('hunch', 'http://hunch.com'),
      Sponsor('mashery', 'http://mashery.com'),
      Sponsor('palantir', 'http://palantir.com'),
]

SEED = [
      Sponsor('google', 'http://google.com'),
]

SPONSORS = IPO + MEZZANINE + SERIES_A + SEED

#Sponsor('allsponsors', '/sponsors'),
#Sponsor('sponsorpennapps', '#B62F2F', 'http://pennapps.com/sponsorship.pdf', '#B62F2F', 'no-opacity')

Competition = namedtuple('Competition', ['season', 'year', 'href'])

COMPETITIONS = [
    Competition('Spring', '2012', 'http://2012s.pennapps.com/'),
    Competition('Fall', '2011', 'http://2011f.pennapps.com/'),
    Competition('Spring', '2011', 'http://pennapps.com/spring2011/'),
    Competition('Fall', '2010', 'http://pennapps.com/2010'),
    Competition('Fall', '2009', 'http://pennapps.com/2009'),
]


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


def build_index(env):
    build_template(env, 'index.html',
            sponsors=SPONSORS,
            ipo=IPO,
            mezzanine=MEZZANINE,
            series_a=SERIES_A,
            seed=SEED,
            competitions=COMPETITIONS,
            stories=STORIES,
    )

def build_history(env):
    build_template(env, 'history.html')

def build_faq(env):
    build_template(env, 'faq.html')

def build_rules(env):
    build_template(env, 'rules.html')

def build_about(env):
    build_template(env, 'about.html')

def build_schedule(env):
    build_template(env, 'schedule.html')

def build_venue(env):
    build_template(env, 'venue.html')

def build_sponsorship(env):
    build_template(env, 'sponsorship.html')

def build_sponsors(env):
    build_template(env, 'sponsors.html',
            sponsors=SPONSORS,
            ipo=IPO,
            mezzanine=MEZZANINE,
            series_a=SERIES_A,
            seed=SEED,
            competitions=COMPETITIONS,
    )


def main():
    env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    build_index(env)
    build_about(env)
    build_history(env)
    build_schedule(env)
    build_venue(env)
    build_sponsorship(env)
    build_rules(env)
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
