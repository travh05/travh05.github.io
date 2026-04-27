# [Lab Name] Lab Website

A clean, academic-styled lab website inspired by joneslab.org. Static HTML/CSS — no build step, no dependencies. Hosts free on GitHub Pages.

## File structure

```
.
├── index.html           # Homepage
├── research.html        # Research themes
├── people.html          # Team
├── publications.html    # Publication list
├── contact.html         # Contact + join the lab
├── css/
│   └── styles.css       # Shared stylesheet
├── images/              # Drop your photos here
└── README.md
```

## Customizing the site

Search-and-replace these placeholders across all `.html` files:

| Placeholder              | Replace with                                   |
|--------------------------|------------------------------------------------|
| `[Lab Name]`             | Your lab name (e.g. `Smith`)                   |
| `[LabName]`              | Same, no space, used in the logo              |
| `[Institution]`          | University or hospital                         |
| `[Department]`           | Department name                                |
| `[email protected]`        | Lab contact email                              |
| `[PI Name]`              | PI's full name                                 |
| `[Tagline]`              | Hero tagline (e.g. "Targeting cancer at its root") |

Then edit each page's content blocks (paragraphs in square brackets) directly.

### Adding images

1. Drop image files into the `images/` folder.
2. In any HTML file, replace placeholder `<div class="hero-image">` or `<div class="photo">` blocks with `<img>` tags. Each placeholder block has a comment showing the exact replacement.

Example for the hero image (`index.html`):
```html
<div class="hero-image">
  <img src="images/hero.jpg" alt="Lab at work" style="width:100%;height:100%;object-fit:cover;">
</div>
```

### Changing colors

Edit the `:root` block at the top of `css/styles.css`. Most of the visual identity is controlled by these variables:

```css
--bg: #FBF9F4;        /* page background */
--brand: #1E4D4A;     /* deep teal — primary brand color */
--accent: #C8553D;    /* warm rust — accent / stat color */
--ink: #1A1A1A;       /* main text */
```

### Changing fonts

Both fonts come from Google Fonts and are loaded in the `<head>` of each HTML file. To swap:
1. Pick new fonts at [fonts.google.com](https://fonts.google.com) and copy their `<link>` tag.
2. Replace the existing Google Fonts `<link>` line in every HTML file.
3. Update `font-family` in `css/styles.css` (`'Fraunces'` for headings, `'DM Sans'` for body).

---

## Deploying to GitHub Pages (free)

You have two options. Option A is the easiest if you only have one website to host.

### Option A — User site (becomes `https://YOURUSERNAME.github.io`)

1. **Create a GitHub account** at [github.com](https://github.com) if you don't have one.
2. **Create a new repository** named exactly `YOURUSERNAME.github.io` (replace with your actual GitHub username). Make it Public.
3. **Upload the files**: on the new repo's page, click "uploading an existing file" and drag in everything from this folder (`index.html`, `research.html`, etc., plus the `css/` and `images/` folders). Click "Commit changes".
4. **Wait 1–2 minutes**. Visit `https://YOURUSERNAME.github.io` — your site is live.

### Option B — Project site (becomes `https://YOURUSERNAME.github.io/REPO-NAME`)

Use this if you already have a `username.github.io` repo, or you want the lab site under a sub-path.

1. Create a new public repo with any name (e.g. `lab-site`).
2. Upload the files (same as step 3 above).
3. Go to the repo's **Settings → Pages** in the left sidebar.
4. Under "Build and deployment", set Source = "Deploy from a branch", Branch = `main`, folder = `/ (root)`. Save.
5. Wait 1–2 minutes. Your site is at `https://YOURUSERNAME.github.io/lab-site`.

### Using the GitHub Desktop app (no command line)

If you'd rather not touch the terminal:
1. Install [GitHub Desktop](https://desktop.github.com).
2. File → New repository → point it at this folder.
3. Publish to GitHub (make sure "Keep this code private" is unchecked).
4. Then follow the Pages setup in Option B, step 3 onwards.

### Using the command line

```bash
cd path/to/this/folder
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/REPO-NAME.git
git push -u origin main
```
Then enable Pages in repo Settings.

---

## Using a custom domain (e.g. `yourlab.org`)

1. Buy the domain from any registrar (Namecheap, Cloudflare, Porkbun, etc.).
2. In your GitHub repo: Settings → Pages → Custom domain → enter `yourlab.org` and save.
3. At your registrar, set DNS records to point at GitHub:
   - Four `A` records on `@` pointing to: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - One `CNAME` record on `www` pointing to `YOURUSERNAME.github.io`
4. Wait up to an hour for DNS to propagate, then check "Enforce HTTPS" in Pages settings.

---

## Working locally

To preview the site on your own machine, just open `index.html` in any browser. No server needed for static HTML.

If you'd prefer a local server (so things like relative paths behave exactly as they will on GitHub Pages):

```bash
# Python 3
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## License

Use freely. Attribution appreciated but not required.
