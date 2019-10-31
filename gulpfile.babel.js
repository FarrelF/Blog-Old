import fs from "fs";
import path from "path";
import { watch, parallel } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

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

exports.publish = publish
exports.invoke_build = invoke_build;
exports.make_html = make_html;
exports.default = invoke_build;
