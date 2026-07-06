# Deployment Notes

## Fastest options

### Netlify drag-and-drop
1. Go to Netlify.
2. Create a new site by drag-and-drop.
3. Upload this folder or the ZIP.
4. Connect the custom domain later.

### GitHub Pages
1. Create a GitHub repository.
2. Upload `index.html`, `styles.css`, `script.js`, and the `assets` folder.
3. Go to Settings → Pages.
4. Deploy from the main branch.

### GoDaddy hosting
1. Open GoDaddy hosting file manager or cPanel.
2. Upload all files into `public_html`.
3. Make sure `index.html` is at the root of `public_html`.

## Domain DNS reminder
If you use GitHub Pages for an apex/root domain, GitHub currently uses these A records:

- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

For `www`, point the CNAME to the GitHub Pages domain for the account.
