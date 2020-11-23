<template>
  <div id="pageContainer">
    <div id="viewer" class="pdfViewer"></div>
  </div>
</template>

<script>
import pdfjsLib from "pdfjs-dist/build/pdf";
import { PDFViewer } from "pdfjs-dist/web/pdf_viewer";
import "pdfjs-dist/web/pdf_viewer.css";

// const pdfjsWorker = import('pdfjs-dist/build/pdf.worker.entry');

// pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdn.jsdelivr.net/npm/pdfjs-dist@2.0.943/build/pdf.worker.min.js";

export default {
  name: "PdfViewer",
  mounted() {
    this.getPdf();
  },
  methods: {
    async getPdf() {
      pdfjsLib.GlobalWorkerOptions.workerSrc = "//mozilla.github.io/pdf.js/build/pdf.worker.js";
      const container = document.getElementById("pageContainer");
      const pdfViewer = new PDFViewer({
        container,
      });
      const loadingTask = pdfjsLib.getDocument("./pdf-sample.pdf");
      const pdf = await loadingTask.promise;
      pdfViewer.setDocument(pdf);
    },
  },
};
</script>

<style>
#pageContainer {
  margin: auto;
  width: 80%;
}

div.page {
  display: inline-block;
}
</style>
