from collections import namedtuple

from jinja2 import Environment, FileSystemLoader


Sponsor = namedtuple('Sponsor', ['name', 'href'])


# TODO: Figure out a good way to show the other sponsors
SPONSORS = [
      Sponsor('facebook', 'http://facebook.com'),
      Sponsor('google', 'http://google.com'),
      Sponsor('mongodb', 'http://mongodb.com'),
      Sponsor('venmo', 'http://venmo.com'),
      Sponsor('hunch', 'http://hunch.com'),
      Sponsor('tumblr', 'http://tumblr.com'),
      Sponsor('palantir', 'http://palantir.com'),
      Sponsor('mashery', 'http://mashery.com'),
      Sponsor('yahoo', 'http://yahoo.com'),
      Sponsor('lore', 'http://lore.com'),
      #Sponsor('allsponsors', '/sponsors'),
      #Sponsor('sponsorpennapps', '#B62F2F', 'http://pennapps.com/sponsorship.pdf', '#B62F2F', 'no-opacity')
]


Competition = namedtuple('Competition', ['season', 'year', 'href'])

COMPETITIONS = [
    Competition('Spring', '2012', 'http://2012s.pennapps.com/'),
    Competition('Fall', '2011', 'http://2011f.pennapps.com/'),
    Competition('Spring', '2011', 'http://pennapps.com/spring2011/'),
    Competition('Fall', '2010', 'http://pennapps.com/2010'),
    Competition('Fall', '2009', 'http://pennapps.com/2009'),
]


def build():
    env = Environment(loader=FileSystemLoader(searchpath="./templates"))
    template = env.get_template('index.html')
    with open("index.html", "w") as f:
        f.write(template.render(
            sponsors=SPONSORS,
            competitions=COMPETITIONS,
        ))


def main():
    build()


if __name__ == "__main__":
    main()
