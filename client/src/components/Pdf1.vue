<template>
  <div>
    <p>How are ya?</p>
    <h1>pdf.pdf render in web with clickable signing block</h1>
    <canvas id="the-canvas"></canvas>
  </div>
</template>
<script>
import pdfjsLib from "pdfjs-dist/build/pdf";

export default {
  methods: {
    renderCanvas() {
      // header on that server.
      const url = "https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/examples/learning/helloworld.pdf";

      // Loaded via <script> tag, create shortcut to access PDF.js exports.
      // const pdfjsLib = window["pdfjs-dist/build/pdf"];

      // The workerSrc property shall be specified.
      pdfjsLib.GlobalWorkerOptions.workerSrc = "pdfjs-dist/build/pdf.worker.js";
      // console.log("PDF trying to load loaded");

      // Asynchronous download of PDF
      const loadingTask = pdfjsLib.getDocument(url);
      loadingTask.promise.then(
        (pdf) => {
          console.log("PDF loaded");

          // Fetch the first page
          const pageNumber = 1;
          pdf.getPage(pageNumber).then((page) => {
            console.log("Page loaded");

            const scale = 1.5;
            const viewport = page.getViewport({ scale });

            // Prepare canvas using PDF page dimensions
            const canvas = document.getElementById("the-canvas");
            const context = canvas.getContext("2d");
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            // Render PDF page into canvas context
            const renderContext = {
              canvasContext: context,
              viewport,
            };
            const renderTask = page.render(renderContext);
            renderTask.promise.then(() => {
              console.log("Page rendered");
            });
          });
        },
        (reason) => {
          // PDF loading error
          console.error(reason);
        },
      );
    },
  },
  created() {
    this.renderCanvas();
  },
};
</script>
