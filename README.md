# Xie Lab website

Static site for the **Xie Lab** at Princess Margaret Cancer Centre and the University of Toronto (Department of Medical Biophysics). It presents the group’s work on inflammatory and metabolic stress in human hematopoietic stem cells, clonal hematopoiesis, and leukemia, along with people, selected publications, and contact information.

**Stack:** HTML and CSS only. Each page includes its own `<style>` block (Fraunces + DM Sans via Google Fonts). No build step or package manager. The `css/styles.css` file is not linked from the HTML; styles are maintained per page.

## Pages

| File | Content |
|------|---------|
| `index.html` | Home |
| `research.html` | Research themes |
| `people.html` | Principal investigator and lab members |
| `publications.html` | Selected publications (full list via Google Scholar) |
| `contact.html` | Address, email, joining the lab |

Assets such as `xie_logo.png`, faculty and trainee photos, and `images/` sit beside these files at the repo root.

## Local preview

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy

Push to GitHub and use **Settings → Pages** with branch `main` and `/ (root)`, or upload the folder to any static host.
