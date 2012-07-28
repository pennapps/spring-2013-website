from collections import namedtuple

from jinja2 import Environment, FileSystemLoader

Sponsor = namedtuple('Sponsor', ['name', 'href'])


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

ENV = Environment(loader=FileSystemLoader(searchpath="./templates"))


def build():
    template = ENV.get_template('index.html')
    with open("index.html", "w") as f:
        f.write(template.render(sponsors=SPONSORS))


def main():
    build()


if __name__ == "__main__":
    main()
