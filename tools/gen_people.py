#!/usr/bin/env python3
"""Generate the lab-members grid and the individual profile pages.

Single source of truth is the PEOPLE list below. Run from the repo root:

    python3 tools/gen_people.py

It rewrites the block between the members:start / members:end markers in
people.html and writes one people/<slug>.html per member who has a bio.
A member without a bio gets a plain, unlinked card so no card can lead to
an empty page.
"""

import html
import os
import re

SITE = 'https://xielab.ca'

PEOPLE = [
    dict(
        slug='jessica', name='Jessica',
        role='Lab Manager &amp; Senior Research Technician',
        photo='jess.jpg',
        bio=[
            "Jessica is the Lab Manager and Senior Research Technician in the Xie Lab, "
            "bringing over 15 years of experience in hematopoietic stem cell and leukemia "
            "research. She oversees day-to-day lab operations and supports the team’s "
            "research, training, and experimental activities. Outside the lab, Jessica "
            "enjoys music and going to concerts.",
        ],
    ),
    dict(
        slug='isabella', name='Isabella',
        role='PhD Student, Medical Biophysics',
        photo='isabella.jpg',
        bio=[],
    ),
    dict(
        slug='travis', name='Travis',
        role='Research Student',
        letter='T',
        bio=[],
    ),
    dict(
        slug='alex', name='Alex',
        role='Co-op Student',
        photo='alexandra.jpg',
        bio=[
            "Alex received her Bachelor of Science majoring in Biology from the University "
            "of Waterloo in 2026. She has been accepted to medical school and will be "
            "starting in January 2027 after she completes her work/co-op term with Dr. Xie. "
            "In 2025, Alex presented her university team’s research on urinary tract "
            "infection treatment at the international iGEM conference in Paris.",
            "When she is not in the lab, she loves to play soccer and explore all the food "
            "at the different festivals that Toronto has to offer.",
        ],
    ),
    dict(
        slug='cam', name='Cam',
        role='Postdoctoral Fellow',
        photo='cam.jpg',
        bio=[
            "Cam is a post-doctoral fellow in the Xie Lab, studying the role of inflammation "
            "in initiation and progression of clonal hematopoiesis. Cam completed his PhD in "
            "biochemistry at McMaster University in 2025, studying cellular mechanisms of "
            "leukemia relapse. Outside the lab, Cam enjoys running and spending time in the "
            "outdoors.",
        ],
    ),
    dict(
        slug='duanya', name='Duanya',
        role=None,
        letter='D',
        bio=[],
    ),
]

NAV = '''  <header class="site-header">
    <nav class="nav">
      <a href="../index.html" class="nav-logo"><img src="../xie_logo.png" alt="Xie Lab"></a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links">☰</button>
      <ul class="nav-links" id="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../research.html">Research</a></li>
        <li><a href="../people.html" class="active">People</a></li>
        <li><a href="../publications.html">Publications</a></li>
        <li><a href="../contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>'''

FOOTER = '''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <span class="footer-logo">Xie <em>Lab</em></span>
          <p style="opacity: 0.7; max-width: 40ch;">
            Princess Margaret Cancer Centre, University Health Network<br>
            Department of Medical Biophysics, University of Toronto<br>
            Toronto, Ontario, Canada
          </p>
        </div>
        <div>
          <h4>Explore</h4>
          <ul>
            <li><a href="../research.html">Research</a></li>
            <li><a href="../people.html">People</a></li>
            <li><a href="../publications.html">Publications</a></li>
            <li><a href="../contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Connect</h4>
          <ul>
            <li><a href="https://bsky.app/profile/stephxie.bsky.social">Bluesky</a></li>
            <li><a href="https://www.linkedin.com/in/stephaniexielab/">LinkedIn</a></li>
            <li><a href="https://scholar.google.com/citations?user=MbxBhZsAAAAJ">Google Scholar</a></li>
            <li><a href="https://www.uhnresearch.ca/researcher/stephanie-xie">UHN Profile</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year"></span> Xie Lab. All rights reserved.</span>
        <span>Princess Margaret Cancer Centre · Toronto</span>
      </div>
    </div>
  </footer>

  <script>
    document.querySelector('.nav-toggle').addEventListener('click', function() {
      var open = document.querySelector('.nav-links').classList.toggle('open');
      this.setAttribute('aria-expanded', open);
    });
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>'''

PAGE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} — Xie Lab</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="profile">
  <meta property="og:site_name" content="Xie Lab">
  <meta property="og:title" content="{name} — Xie Lab">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{ogimg}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,30..100;1,9..144,300..700,30..100&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="icon" type="image/png" href="../xie_logo.png">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body>

{nav}

  <section class="page-header">
    <div class="container">
      <span class="eyebrow rise">{role}</span>
      <h1 class="rise d1">{name}</h1>
    </div>
  </section>

  <section class="people-section">
    <div class="container">
      <div class="story-block">
        <div>
          <div class="person-portrait">{portrait}</div>
        </div>
        <div>
{bio}
          <p style="margin-top: 2.5rem;">
            <a href="../people.html" class="arrow-link">Back to all people</a>
          </p>
        </div>
      </div>
    </div>
  </section>

{footer}

</body>
</html>
'''

START = '      <!-- members:start -->'
END = '      <!-- members:end -->'


def card(p):
    """One grid card. Linked only when the person has a profile page."""
    if p.get('photo'):
        media = (
            '<div class="photo" style="background-image: none;">\n'
            '            <img src="%s" alt="%s" style="width:100%%;height:100%%;'
            'object-fit:cover;border-radius:2px;">\n'
            '          </div>' % (p['photo'], p['name'])
        )
    else:
        media = '<div class="photo">%s</div>' % p['letter']

    role = ('<p class="person-role">%s</p>' % p['role']) if p['role'] else \
           '<p>[Role / project]</p>'

    if p['bio']:
        return (
            '        <a class="person-card person-link" href="people/%s.html">\n'
            '          %s\n'
            '          <h4>%s</h4>\n'
            '          %s\n'
            '          <span class="person-more">Read bio</span>\n'
            '        </a>\n' % (p['slug'], media, p['name'], role)
        )
    return (
        '        <div class="person-card">\n'
        '          %s\n'
        '          <h4>%s</h4>\n'
        '          %s\n'
        '        </div>\n' % (media, p['name'], role)
    )


def profile(p):
    if p.get('photo'):
        portrait = '<img src="../%s" alt="%s">' % (p['photo'], p['name'])
        ogimg = '%s/%s' % (SITE, p['photo'])
    else:
        portrait = '<span class="portrait-letter">%s</span>' % p['letter']
        ogimg = '%s/research_diagram.png' % SITE

    role_plain = html.unescape(p['role'])
    desc = '%s, %s in the Xie Lab at Princess Margaret Cancer Centre.' % (
        p['name'], role_plain)
    bio = '\n'.join('          <p>%s</p>' % html.escape(t, quote=False)
                    for t in p['bio'])
    return PAGE.format(
        name=p['name'], role=p['role'], desc=html.escape(desc, quote=True),
        url='%s/people/%s.html' % (SITE, p['slug']), ogimg=ogimg,
        nav=NAV, footer=FOOTER, portrait=portrait, bio=bio)


def main():
    os.makedirs('people', exist_ok=True)

    written = []
    for p in PEOPLE:
        if not p['bio']:
            continue
        open('people/%s.html' % p['slug'], 'w').write(profile(p))
        written.append(p['slug'])

    src = open('people.html').read()
    if START not in src or END not in src:
        raise SystemExit('members markers missing from people.html')
    grid = '\n' + '\n'.join(card(p) for p in PEOPLE)
    new = re.sub(
        re.escape(START) + r'.*?' + re.escape(END),
        START + grid + END,
        src, flags=re.S)
    open('people.html', 'w').write(new)

    print('profile pages:', ', '.join(written))
    print('grid cards:', len(PEOPLE),
          '(%d linked)' % sum(1 for p in PEOPLE if p['bio']))


if __name__ == '__main__':
    main()
