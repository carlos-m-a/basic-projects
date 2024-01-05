# JS-HTML-CSS UI examples

## Purpose

Good UI examples to be used, whitout using a css framework, only pure css-javascript-html.


## Keep in mind

* You should edit the repository name (`html-css-js-examples`)
* To check the web, run a local server pointing to this repository and navigate to your localhost with your browser. Simplest options for running a local server:
  * python: `python -m http.server -b 127.0.0.1 8080`
  * node.js: `npx http-server -a 127.0.0.1 -p 8080` (install node and http-server before)
* Paths in html files only work if you run a local server. Paths won't work if you open the html files directly (`file:///` in the address bar of your browser)


## Folders and Files

[Folder structure doc](https://appcropolis.com/blog/organize-html-css-javascript-files)
[Basic HTML5 template doc](https://www.sitepoint.com/a-basic-html5-template/)

Folders:
* **/examples-conponent**: Examples for some specific components normally used in html UIs (panels, tables, forms, etc)
* **/examples-layout**: Examples of whole web UIs

Files:
* **index.html**: Main entry point for navigate to every example


## Basic html-css-javascript project structure:

```bash
html-css-js-basic
├── assets
│   ├── css
│   │   ├── dark-theme.css
│   │   └── main.css
│   ├── data
│   │   ├── data.json
│   │   └── data-table-1.csv
│   ├── fonts
│   │   └── some-font.ttf
│   ├── images
│   │   ├── favicon.ico
│   │   └── logo.png
│   ├── js
│   │   ├── functions.js
│   │   └── main.js
│   └── vendors
│       ├── bootstrap.bundle.min.js
│       ├── bootstrap.min.css
│       ├── materialize.min.css
│       └── matierialize.min.js
├── components
│   ├── footer.html
│   └── navbar.html
├── folder1
│   ├── other1.html
│   └── other2.html
├── folder2
│   └── other-html.html
├── index.html
└── README.md

```
