import fs from "fs";
import path from "path";
import { watch, parallel } from "gulp";
import { exec } from "child_process";
import { create as browserSyncCreate } from "browser-sync";
const browserSync = browserSyncCreate();

const content_404 = fs.readFileSync(
  path.join(__dirname, "output/404.html")
);

const buildAll = () => exec("invoke build");
const publishAll = () => exec("invoke publish");

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

const watchFiles = () => {
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
    buildAll
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
    publishAll
  );
};

const build = parallel(watchFiles, reload);
const publish = parallel(watchPublishFiles, reload);

exports.publish = publish
exports.build = build;
exports.default = build;
