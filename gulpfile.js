var { watch, parallel } = require("gulp");
var { exec } = require("child_process");
var browserSync = require('browser-sync').create();
var fs = require("fs");
var path = require("path");

const content_404 = fs.readFileSync(
  path.join(__dirname, "output/404.html")
);

const invoke_buildAll = () => exec("invoke build");
const make_AllHtml = () => exec("make html");
const invoke_publishAll = () => exec("invoke publish");

const reload = cb => {
  browserSync.init(
    {
      ui: {
        port: 9002
      },
      server: {
        baseDir: "output",
        serveStaticOptions: {
          extensions: ["html"]
        }
      },
      files: "output/*.html",
      port: 9001
    },
    (_, bs) => {
      bs.addMiddleware("*", (_, res) => {
        res.write(content_404);
        res.end();
      });
    }
  );
  cb();
};

const watchInvokeFiles = () => {
  watch(
    [
      "content/**/*.md",
      "content/**/*.markdown",
      "content/**/*.rest",
      "content/**/*.rst",
      "content/**/*.css",
      "content/img/*.jpg",
      "content/img/*.png",
      "gulpfile.babel.js",
      "pelicanconf.py",
      "themes/Flex/templates/**/*.html",
      "themes/Flex/static/**/*.css",
      "themes/Flex/static/**/*.js"
    ],
    { ignoreInitial: false },
    invoke_buildAll
  );
};

const watchMakeFiles = () => {
  watch(
    [
      "content/**/*.md",
      "content/**/*.markdown",
      "content/**/*.rest",
      "content/**/*.rst",
      "content/**/*.css",
      "content/img/*.jpg",
      "content/img/*.png",
      "gulpfile.babel.js",
      "pelicanconf.py",
      "themes/Flex/templates/**/*.html",
      "themes/Flex/static/**/*.css",
      "themes/Flex/static/**/*.js"
    ],
    { ignoreInitial: false },
    make_AllHtml
  );
};

const watchPublishFiles = () => {
  watch(
    [
      "content/**/*.md",
      "content/**/*.markdown",
      "content/**/*.rest",
      "content/**/*.rst",
      "content/**/*.css",
      "content/img/*.jpg",
      "content/img/*.png",
      "gulpfile.babel.js",
      "pelicanconf.py",
      "publishconf.py",
      "themes/Flex/templates/**/*.html",
      "themes/Flex/static/**/*.css",
      "themes/Flex/static/**/*.js"
    ],
    { ignoreInitial: false },
    invoke_publishAll
  );
};

const invoke_build = parallel(watchInvokeFiles, reload);
const make_html = parallel(watchMakeFiles, reload);
const publish = parallel(watchPublishFiles, reload);

const _publish = publish;
const _invoke_build = invoke_build;
const _make_html = make_html;
const _default = invoke_build;
exports.publish = _publish, exports.invoke_build = _invoke_build, exports.make_html = _make_html, exports.default = _default;

