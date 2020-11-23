<template>
  <div>
    <p>{{ fileName }}</p>
    <p>{{ path }}</p>
    <!-- <iframe height="100%" width="100%" :src="`${getFilePath}`"></iframe> -->
    <iframe
      height="100%"
      width="100%"
      :src="`lib/pdfjs-2.5.207-dist/web/viewer.html?file=my-pdf-file.pdf`"
    ></iframe>
  </div>
</template>

<script>
console.log("Test 2");
export default {
  name: "PDFJSViewer",
  props: {
    fileName: String,
    path: String,
    // fileName: "my-pdf-file.pdf", // change which pdf file loads
    // path: "lib/pdfjs-2.5.207-dist/web/viewer.html",
  },

  //   data() {
  //     return {
  //       fileName: "my-pdf-file.pdf", // change which pdf file loads
  //       path: "lib/pdfjs-2.5.207-dist/web/viewer.html", // path of the PDF.js viewer.html
  //     };
  //   },
  computed: {
    getFilePath: () => {
      //   console.log(this.fileName, this.path);
      console.log("Test 5");
      //   console.log(this.path);
      //   if (this.fileName !== "") {
      //     const f = `${this.path}|?file=|${this.fileName}`;
      //     return f;
      //   }
      //   return this.path;
      return "lib/pdfjs-2.5.207-dist/web/viewer.html";
    },
  },
};
</script>
<style scoped>
div {
  padding: 50px 0 50px 0;
  margin: auto;
  width: 50%;
  height: 79vh;
  min-width: 400px;
}
</style>
