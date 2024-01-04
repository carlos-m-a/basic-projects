# JS-HTML-CSS Basic Project Structure


## Keep in mind:

* You should edit the repository name (`html-css-js-basic`)
* Remove every file in `/assets/vendors` and `/assets/fonts` folders. They are mock files to make clearer where to place that type of files, so they are useless. Replace them with the real ones if necessary, or remove them.
* You should remove or rename folder1 and folder2
* When the html is loaded. the entry point of the execution of javascript is in `/assets/js/main.js`, in the `main()` function, So every code that should be executed automatically depends on `main()`. Don't change the last line of `main.js` or the `main()` function name.
* To check the web, run a local server pointing to this repository and navigate to your localhost with your browser. Simplest options for running a local server:
  * python: `python -m http.server -b 127.0.0.1 8080`
  * node.js: `npx http-server -a 127.0.0.1 -p 8080` (install node and http-server before)
* Paths in html files only work if you run a local server. Paths won't work if you open the html files directly (`file:///` in the address bar of your browser)


## Folders and Files

[Folder structure doc](https://appcropolis.com/blog/organize-html-css-javascript-files)
[Basic HTML5 template doc](https://www.sitepoint.com/a-basic-html5-template/)

Folders:
* **/assets**: Where every resource used by html files will be located
* **/assets/css**: Your css code (except 3rd party libraries).
* **/assets/data**: It’s a central location for any files with data that your application will ingest or produce. JSON, XML, CSV or TXT.
* **/assets/fonts**: Every imported font that you use (TTF or OTF files).
* **/assets/images**: Every image. PNG recommended for everything but photos, JPG for photos.
* **/assets/js**: Your javascript code (except 3rd party libraries).
* **/assets/vendors**: 3rd party CSS-JS libraries and frameworks, like Bootstrap, Materialize or any other.
* **/components**: HTML parts that will be repeatedly included in HTML files, like the header, navbar, footer, etc.
* **/folder1**, **/folder2**: Example folders where new html files must be placed. Organize new html files in different folders, with the name of the different parts of the web. Remove 'folder1' and 'folder2' or rename them according your necessities.

Other folders (create them according to your need):
* **/assets/scss**: For SASS files

Files:
* **index.html**: Main entry point of your web
* **/folder1/other1.html**: Example of a new html file
* **/assets/js/main.js**: Entry point js file
* **/assets/js/functions.js**: Functions library for every function called by a event (with a good example for calling APIs using Javascript).
* **/assets/css/main.css**: Entry point css file


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
