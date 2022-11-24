# JS-HTML-CSS Basic Project Structure


## Keep in mind:

* You should edit repository name (`html-css-js-basic`)
* Remove every file in `vendors` and `fonts` folders. They are mock files to make clearer where to place that type of files, so they are useless. Replace them with the real ones if necessary.
* When the html is loaded. the entry point of the execution of javascript is in `/js/main.js`, in the `main()` function, So every code that should be executed automatically depends on `main()`. Don't change the last line of `main.js` or the main function name.
* To check the web, just open index.html with a browser


## Folders and Files

[Folder structure doc](https://appcropolis.com/blog/organize-html-css-javascript-files)
[Basic HTML5 template doc](https://www.sitepoint.com/a-basic-html5-template/)

Folders:
* **vendor**: 3rd party CSS-JS libraries and frameworks, like Bootstrap, Materialize or any other
* **data**: It’s a central location for any files with data that your application will ingest or produce. JSON, XML, CSV or TXT
* **components**: HTML parts that will be repeatedly included in HTML files, like the header, navbar, footer, etc.
* **css**: Your css code (except 3rd party libraries)
* **js**: Your javascript code (except 3rd party libraries)
* **images**: Every image. PNG recommended for everything but photos, JPG for photos.
* **fonts**: Every imported font you use (TTF or OTF files)

Other folders (create them according to your need):
* **scss**: For SASS files

Files:
* **index.html**: Main entry point of your web
* **other-html-file.html**: Every other html file must be in the same folder, the project one.
* **js/main.js**: Entry point js file
* **css/main.css**: Entry point css file



## Basic html-css-javascript project structure:

```bash
html-css-js-basic
├── components
│   ├── footer.html
│   └── navbar.html
├── css
│   ├── dark-theme.css
│   └── main.css
├── data
│   ├── data.json
│   └── data-table.csv
├── fonts
│   └── some-font.ttf
├── images
│   ├── logo.png
│   └── favicon.ico
├── js
│   ├── functions.js
│   └── main.js
├── vendors
│   ├── bootstrap.bundle.min.js
│   ├── bootstrap.min.css
│   ├── materialize.min.css
│   └── matierialize.min.js
├── index.html
├── other-html-file.html
└── README.md
```
